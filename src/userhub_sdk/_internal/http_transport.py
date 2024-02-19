import json
import math
import urllib.parse
from types import TracebackType
from typing import Any, Dict, Generic, Optional, Tuple, Type, TypeVar

import httpcore

from userhub_sdk import apiv1, types

from . import constants, util
from .request import Request
from .response import Response
from .transport import AsyncTransport, Transport

T = TypeVar("T", httpcore.ConnectionPool, httpcore.AsyncConnectionPool)


class BaseHttpTransport(Generic[T]):
    _base_url: str
    _headers: Dict[str, str]
    _pool: T

    def __init__(
        self,
        pool_class: Type[T],
        base_url: str,
        headers: Optional[Dict[str, str]] = None,
    ):
        super().__init__()

        self._base_url = base_url

        if headers is None:
            self._headers = {}
        else:
            self._headers = {k.lower(): v for k, v in headers.items()}

        self._headers["user-agent"] = constants.USER_AGENT

        self._pool = pool_class(
            max_connections=constants.MAX_CONNECTIONS,
            max_keepalive_connections=constants.MAX_IDLE_CONNECTIONS,
            keepalive_expiry=math.ceil(
                constants.CONNECTION_IDLE_TIMEOUT.total_seconds()
            ),
            http1=True,
            http2=False,
            retries=0,
        )

    def _setup_execute(self, req: Request) -> Tuple[str, Dict[str, str], bytes]:
        url = self._base_url + req.path
        headers = dict(self._headers)
        body = None

        if req.query:
            url += "?" + urllib.parse.urlencode(req.query)

        if req.headers:
            for key, value in req.headers.items():
                headers[key.lower()] = value

        if req.body is not None:
            headers["content-type"] = "application/json"
            try:
                body = util.encode_json(req.body)
            except Exception as ex:
                raise types.UserHubError(
                    "Failed to encode request body",
                    call=req.call,
                ) from ex

        return url, headers, body or b""

    @staticmethod
    def _build_request(
        req: Request,
        url: str,
        headers: Dict[str, str],
        body: Optional[bytes],
    ) -> Any:
        return {
            "method": req.method,
            "url": url,
            "headers": headers,
            "content": body,
            "extensions": {
                "timeout": {
                    "connect": constants.CONNECT_TIMEOUT.total_seconds(),
                    "pool": constants.CONNECT_TIMEOUT.total_seconds(),
                    "read": constants.READ_TIMEOUT.total_seconds(),
                    "write": constants.WRITE_TIMEOUT.total_seconds(),
                },
            },
        }

    @staticmethod
    def _build_response(
        req: Request,
        res: httpcore.Response,
    ) -> Response:
        body = res.content.decode("utf-8") if res.content else ""

        if res.status // 100 != 2:
            content_type = next(
                (v.lower() for k, v in res.headers if k.lower() == b"content-type"),
                None,
            )
            if content_type and b"json" in content_type:
                try:
                    status = apiv1.Status.__json_decode__(json.loads(body))
                except Exception as ex:
                    raise types.UserHubError(
                        f"Failed to decode error response{util.summarize_body(body)}",
                        call=req.call,
                        _res=res,
                    ) from ex

                raise types.UserHubError(status=status, call=req.call, _res=res)
            if res.status == 429:
                raise types.UserHubError(
                    "API call rate limited",
                    call=req.call,
                    api_code=types.Code.RESOURCE_EXHAUSTED,
                    _res=res,
                )

            raise types.UserHubError(
                f"API returned non-JSON error{util.summarize_body(body)}",
                call=req.call,
                _res=res,
            )

        return Response(req=req, res=res, body=body)


class HttpTransport(BaseHttpTransport[httpcore.ConnectionPool], Transport):
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        super().__init__(
            pool_class=httpcore.ConnectionPool,
            base_url=base_url,
            headers=headers,
        )

    def execute(self, req: Request) -> Response:
        url, headers, body = self._setup_execute(req)

        while True:
            req.attempt += 1

            try:
                try:
                    res = self._pool.request(
                        **self._build_request(req, url, headers, body)
                    )
                except Exception as ex:
                    raise types.UserHubError(
                        "Failed to execute request",
                        call=req.call,
                    ) from ex

                return self._build_response(req, res)
            except Exception as ex:
                timeout = req.retry(ex)
                if timeout is not None:
                    self._pool._network_backend.sleep(timeout.total_seconds())
                    continue

                raise

    def close(self) -> None:
        self._pool.close()

    def __enter__(self) -> "HttpTransport":
        self._pool.__enter__()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        exc_tb: Optional[TracebackType] = None,
    ) -> None:
        self._pool.__exit__(exc_type, exc_value, exc_tb)


class AsyncHttpTransport(
    BaseHttpTransport[httpcore.AsyncConnectionPool], AsyncTransport
):
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        super().__init__(
            pool_class=httpcore.AsyncConnectionPool,
            base_url=base_url,
            headers=headers,
        )

    async def execute(self, req: Request) -> Response:
        url, headers, body = self._setup_execute(req)

        while True:
            req.attempt += 1

            try:
                try:
                    res = await self._pool.request(
                        **self._build_request(req, url, headers, body)
                    )
                except Exception as ex:
                    if isinstance(ex, RuntimeError):
                        runtime_msg = str(ex)
                        if "httpcore[asyncio]" in runtime_msg:
                            raise RuntimeError(
                                "Running with asyncio requires installation of 'userhub-sdk[asyncio]'."
                            ) from None
                        if "httpcore[trio]" in runtime_msg:
                            raise RuntimeError(
                                "Running with trio requires installation of 'userhub-sdk[trio]'."
                            ) from None

                    raise types.UserHubError(
                        "Failed to execute request",
                        call=req.call,
                    ) from ex

                return self._build_response(req, res)
            except Exception as ex:
                timeout = req.retry(ex)
                if timeout is not None:
                    await self._pool._network_backend.sleep(timeout.total_seconds())
                    continue

                raise

    async def aclose(self) -> None:
        await self._pool.aclose()

    async def __aenter__(self) -> "AsyncHttpTransport":
        await self._pool.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        exc_tb: Optional[TracebackType] = None,
    ) -> None:
        await self._pool.__aexit__(exc_type, exc_value, exc_tb)
