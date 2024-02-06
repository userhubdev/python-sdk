import json
import math
import time
import urllib.parse
from types import TracebackType
from typing import Dict, Optional, Type

import httpcore

from .. import apiv1
from .. import types
from . import constants
from . import util
from .response import Response
from .request import Request
from .transport import AsyncTransport, Transport
from .util import JSONEncoder


class BaseHttpTransport:
    _base_url: str
    _headers: Dict[str, str]

    def __init__(
        self, pool_class, base_url: str, headers: Optional[Dict[str, str]] = None
    ):
        super().__init__()

        self._base_url = base_url

        if headers is None:
            self._headers = {}
        else:
            self._headers = {k.lower(): v for k, v in headers.items()}

        self._headers["user-agent"] = f"UserHub-Python/{constants.VERSION}"

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

    def _setup_execute(self, req: Request):
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
                body = json.dumps(req.body, cls=JSONEncoder).encode("utf-8")
            except Exception as ex:
                raise types.UserHubError(
                    "Failed to encode request body",
                    call=req.call,
                ) from ex

        return url, headers, body

    def _build_request(
        self,
        req: Request,
        url: str,
        headers: Dict[str, str],
        body: Optional[bytes],
    ):
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

    def _build_response(
        self,
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
                        f"Failed to decode error response{Response.summarize_body(body)}",
                        call=req.call,
                        _res=res,
                    ) from ex

                raise types.UserHubError(status=status, call=req.call, _res=res)
            else:
                raise types.UserHubError(
                    f"API returned non-JSON error{Response.summarize_body(body)}",
                    call=req.call,
                    _res=res,
                )

        return Response(req=req, res=res, body=body)


class HttpTransport(BaseHttpTransport, Transport):
    _pool: httpcore.ConnectionPool

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

                raise ex

    def close(self):
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


class AsyncHttpTransport(BaseHttpTransport, AsyncTransport):
    _pool: httpcore.AsyncConnectionPool

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

                raise ex

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
