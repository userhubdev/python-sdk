# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import apiv1
from .._internal import util
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

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("user") is not None:
            kwargs["user"] = User.__json_decode__(data["user"])

        if data.get("error") is not None:
            kwargs["error"] = apiv1.Status.__json_decode__(data["error"])

        return UserResult(**kwargs)
