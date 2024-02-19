# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import adminv1


@dataclasses.dataclass
class UsersChanged:
    """
    The users changed event.
    """

    #: The user.
    user: Optional[adminv1.User] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.user is not None:
            data["user"] = adminv1.User.__json_encode__(self.user)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "UsersChanged":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("user") is not None:
            kwargs["user"] = adminv1.User.__json_decode__(data["user"])

        return UsersChanged(**kwargs)
