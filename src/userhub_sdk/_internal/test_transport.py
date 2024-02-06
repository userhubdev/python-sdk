from types import TracebackType
from typing import Dict, Optional, Type

import httpcore

from .response import Response
from .request import Request
from .transport import AsyncTransport, Transport


class BaseTestTransport:
    error: Optional[BaseException] = None
    request: Optional[Request] = None
    body: str = "{}"

    def __init__(self):
        pass

    def _execute(self, req: Request) -> Response:
        self.request = req

        if self.error is not None:
            raise self.error

        return Response(
            req=req,
            res=httpcore.Response(status=200),
            body=self.body,
        )


class SyncTestTransport(BaseTestTransport, Transport):
    def execute(self, req: Request) -> Response:
        return super()._execute(req)

    def close(self):
        pass

    def __enter__(self) -> "SyncTestTransport":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        exc_tb: Optional[TracebackType] = None,
    ) -> None:
        pass


class AsyncTestTransport(BaseTestTransport, AsyncTransport):
    async def execute(self, req: Request) -> Response:
        return super()._execute(req)

    async def aclose(self) -> None:
        pass

    async def __aenter__(self) -> "AsyncTestTransport":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        exc_tb: Optional[TracebackType] = None,
    ) -> None:
        pass
