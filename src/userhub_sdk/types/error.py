from typing import Any, Dict, Optional, TYPE_CHECKING

from .. import apiv1


if TYPE_CHECKING:
    from httpcore import Response as HttpCoreResponse


class UserHubError(Exception):
    _api_code: Optional[str] = None
    _message: Optional[str] = None
    _reason: Optional[str] = None
    _param: Optional[str] = None
    _metadata: Optional[Dict[str, str]] = None
    _call: Optional[str] = None
    _res: Optional["HttpCoreResponse"] = None

    def __init__(
        self,
        message: str = "",
        *,
        call: Optional[str] = None,
        status: Optional[apiv1.Status] = None,
        # internal
        _res: Optional["HttpCoreResponse"] = None,
    ):
        self._message = message
        self._call = call
        self._res = _res

        if status is not None:
            if status.message and not self._message:
                self._message = status.message
            if status.code:
                self._api_code = status.code
            if status.reason:
                self._reason = status.reason
            if status.param:
                self._param = status.param
            self._metadata = status.metadata

        super()

    def __str__(self):
        parts = []

        if self._call:
            parts.append(f"call: {self._call}")

        has_api_code = self._api_code and self._api_code != "UNKNOWN"

        if has_api_code:
            parts.append(f"api_code: {self._api_code}")

        if self._reason:
            parts.append(f"reason: {self._reason}")

        if self._param:
            parts.append(f"param: {self._param}")

        if not has_api_code and self._res is not None:
            parts.append(f"status_code: {self._res.status}")

        message = self.message

        if parts:
            message += f" ({', '.join(parts)})"

        if self.__cause__:
            message += f": {self.__cause__}"

        return message

    @property
    def api_code(self) -> str:
        """
        The general error code (e.g. `INVALID_ARGUMENT`).
        """
        return self._api_code or "UNKNOWN"

    @property
    def message(self) -> str:
        """
        The developer-facing error message.
        """
        return self._message or "<no message>"

    @property
    def reason(self) -> Optional[str]:
        """
        The reason code for the error (e.g. `USER_PENDING_DELETION`).
        """
        return self._reason

    @property
    def param(self) -> Optional[str]:
        """
        The parameter path related to the error (e.g. `member.userId`).
        """
        return self._param

    @property
    def metadata(self) -> Dict[str, str]:
        """
        The additional error related data.
        """
        return dict(self._metadata) if self._metadata else {}

    @property
    def call(self) -> Optional[str]:
        """
        The method call name for the error (e.g. `admin.users.get`).
        """
        return self._call

    @property
    def status_code(self) -> Optional[int]:
        """
        The HTTP status code (e.g. 500)..
        """
        return self._res.status if self._res is not None else None
