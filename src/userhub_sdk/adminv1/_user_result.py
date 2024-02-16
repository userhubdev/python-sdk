# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import apiv1

from ._user import User


@dataclasses.dataclass
class UserResult:
    """
    The user or error.
    """

    #: The user.
    user: Optional[User] = None
    #: The result error.
    error: Optional[apiv1.Status] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.user is not None:
            data["user"] = User.__json_encode__(self.user)

        if self.error is not None:
            data["error"] = apiv1.Status.__json_encode__(self.error)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "UserResult":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("user") is not None:
            kwargs["user"] = User.__json_decode__(data["user"])

        if data.get("error") is not None:
            kwargs["error"] = apiv1.Status.__json_decode__(data["error"])

        return UserResult(**kwargs)
