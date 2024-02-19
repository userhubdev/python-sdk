import contextlib
from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from userhub_sdk import apiv1

from ._code import Code
from ._undefined import UNDEFINED, Undefined

if TYPE_CHECKING:
    from httpcore import Response as HttpCoreResponse


class UserHubError(Exception):
    _api_code: Optional[Code] = None
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
        api_code: Optional[Code] = None,
        reason: Optional[str] = None,
        param: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
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
                with contextlib.suppress(ValueError):
                    self._api_code = Code(status.code)
            if status.reason:
                self._reason = status.reason
            if status.param:
                self._param = status.param
            self._metadata = status.metadata

        if api_code is not None:
            self._api_code = api_code
        if reason is not None:
            self._reason = reason
        if param is not None:
            self._param = param
        if metadata is not None:
            self._metadata = metadata

        super()

    def __str__(self) -> str:
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

    def __json_encode__(self) -> Dict[str, Any]:
        return {
            "message": self.message,
            "code": self.api_code.value,
        }

    def clone(
        self,
        *,
        message: Union[str, Undefined, None] = UNDEFINED,
        api_code: Union[Code, Undefined, None] = UNDEFINED,
        reason: Union[str, Undefined, None] = UNDEFINED,
        param: Union[str, Undefined, None] = UNDEFINED,
        metadata: Union[Dict[str, str], Undefined, None] = UNDEFINED,
        call: Union[str, Undefined, None] = UNDEFINED,
    ) -> "UserHubError":
        if not isinstance(message, str):
            message = self._message or ""
        if isinstance(api_code, Undefined):
            api_code = self._api_code
        if isinstance(reason, Undefined):
            reason = self._reason
        if isinstance(param, Undefined):
            param = self._param
        if isinstance(metadata, Undefined):
            metadata = self._metadata
        if isinstance(call, Undefined):
            call = self._call

        return UserHubError(
            message,
            api_code=api_code,
            reason=reason,
            param=param,
            metadata=metadata,
            call=call,
        )

    @property
    def api_code(self) -> Code:
        """
        The general error code (e.g. `INVALID_ARGUMENT`).
        """
        return self._api_code or Code.UNKNOWN

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
