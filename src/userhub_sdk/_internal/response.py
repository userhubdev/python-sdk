import json
import re
from typing import Any, Callable, Optional, TypeVar

import httpcore

from .. import types
from . import constants
from .request import Request

T = TypeVar("T")
_WHITESPACE_RE = re.compile(r"\s+", re.MULTILINE)


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
                f"Failed to decode response{self.summarize_body(self._body)}",
                call=self._req.call,
                _res=self._res,
            ) from ex

        return decode(body)

    @staticmethod
    def summarize_body(body: Optional[str]) -> str:
        if not body:
            return ""
        body = _WHITESPACE_RE.sub(" ", body).strip()
        if not body:
            return ""
        return f": {body[:constants.SUMMARIZE_BODY_LENGTH*2]}..."
