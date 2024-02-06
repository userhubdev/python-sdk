# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import adminv1
from .._internal import util


@dataclasses.dataclass
class UsersChanged:
    """
    The users changed event.
    """

    #: The user.
    user: Optional[adminv1.User] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("user") is not None:
            kwargs["user"] = adminv1.User.__json_decode__(data["user"])

        return UsersChanged(**kwargs)
