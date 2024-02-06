import abc
from types import TracebackType
from typing import Dict, Optional, Type

from .response import Response
from .request import Request


class Transport(abc.ABC):
    @abc.abstractmethod
    def execute(self, req: Request) -> Response:
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def __enter__(self) -> "Transport":
        return self

    @abc.abstractmethod
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        pass


class AsyncTransport(abc.ABC):
    @abc.abstractmethod
    async def execute(self, req: Request) -> Response:
        pass

    @abc.abstractmethod
    async def aclose(self) -> None:
        pass

    @abc.abstractmethod
    async def __aenter__(self) -> "AsyncTransport":
        pass

    @abc.abstractmethod
    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        pass
