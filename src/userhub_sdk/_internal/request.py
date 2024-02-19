import datetime
from typing import Any, Dict, Optional, Tuple

import httpcore

from userhub_sdk import types

from . import constants, util

_RETRY_EXCEPTIONS = (httpcore.ConnectError, httpcore.ConnectTimeout)


class Request:
    call: str
    method: str
    path: str
    headers: Optional[Dict[str, str]] = None
    query: Optional[Dict[str, str]] = None
    body: Optional[Any] = None
    attempt: int = 0
    idempotent: bool = False

    def __init__(self, call: str, method: str, path: str):
        self.call = call
        self.method = method
        self.path = path

    def set_idempotent(self, idempotent: bool) -> None:  # noqa: FBT001
        self.idempotent = idempotent

    def set_header(self, name: str, value: str) -> None:
        if self.headers is None:
            self.headers = {}
        self.headers[name] = value

    def set_query(self, name: str, value: Any) -> None:
        if self.query is None:
            self.query = {}

        if value is None:
            value = ""
        elif isinstance(value, bool):
            value = "true" if value else "false"
        elif isinstance(value, datetime.datetime):
            value = util.encode_datetime(value)
        else:
            value = str(value)

        if value:
            self.query[name] = str(value)

    def set_body(self, body: Any) -> None:
        self.body = body

    def should_retry(
        self, ex: BaseException, res: Optional[httpcore.Response] = None
    ) -> Tuple[bool, Optional[httpcore.Response]]:
        if isinstance(ex, types.UserHubError):
            res = ex._res

            if res is not None:
                if res.status == 429:
                    return True, res

                if self.idempotent and 500 <= res.status <= 599:
                    return True, res

        if self.idempotent and isinstance(ex, _RETRY_EXCEPTIONS):
            return True, res

        if ex.__cause__ is not None:
            return self.should_retry(ex.__cause__, res=res)

        return False, res

    def retry(self, ex: Exception) -> Optional[datetime.timedelta]:
        if self.attempt > constants.RETRY_MAX_ATTEMPTS:
            return None

        should_retry, res = self.should_retry(ex)
        if not should_retry:
            return None

        timeout: datetime.timedelta = (
            2 ** (self.attempt - 1) * constants.RETRY_MULTIPLIER
        )
        if timeout > constants.RETRY_MAX_SLEEP:
            timeout = constants.RETRY_MAX_SLEEP

        return timeout
