# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class MemberInput:
    """
    Member input parameters.
    """

    #: The identifier of the user.
    user_id: Optional[str] = None
    #: The identifier of the role.
    #:
    #: This is currently limited to `member`, `admin`, and `owner`.
    role_id: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.user_id is not None:
            data["userId"] = self.user_id

        if self.role_id is not None:
            data["roleId"] = self.role_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "MemberInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("userId") is not None:
            kwargs["user_id"] = data["userId"]

        if data.get("roleId") is not None:
            kwargs["role_id"] = data["roleId"]

        return MemberInput(**kwargs)
