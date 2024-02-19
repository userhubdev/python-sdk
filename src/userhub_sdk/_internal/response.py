import json
from typing import Any, Callable, Optional, TypeVar

import httpcore

from userhub_sdk import types

from .request import Request
from .util import summarize_body

T = TypeVar("T")


class Response:
    _req: Request
    _res: httpcore.Response
    _body: Optional[str] = None

    def __init__(
        self, req: Request, res: httpcore.Response, body: Optional[str] = None
    ):
        self._req = req
        self._res = res
        self._body = body

    def decode_body(self, decode: Callable[[Any], T]) -> T:
        if not self._body:
            return decode({})

        try:
            body = json.loads(self._body)
        except Exception as ex:
            raise types.UserHubError(
                f"Failed to decode response{summarize_body(self._body)}",
                call=self._req.call,
                _res=self._res,
            ) from ex

        return decode(body)
