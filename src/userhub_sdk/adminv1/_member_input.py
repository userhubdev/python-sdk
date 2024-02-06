# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


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

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("userId") is not None:
            kwargs["user_id"] = data["userId"]

        if data.get("roleId") is not None:
            kwargs["role_id"] = data["roleId"]

        return MemberInput(**kwargs)
