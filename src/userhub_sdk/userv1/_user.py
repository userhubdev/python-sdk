# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class User:
    """
    Individual account.
    """

    #: The system-assigned identifier of the user.
    id: str = ""
    #: The client defined unique identifier of the user account.
    unique_id: Optional[str] = None
    #: The human-readable display name of the user.
    display_name: Optional[str] = None
    #: The email address of the user.
    email: Optional[str] = None
    #: Whether the user's email address has been verified.
    email_verified: Optional[bool] = None
    #: The photo/avatar URL of the user.
    image_url: Optional[str] = None
    #: Whether the user is disabled.
    disabled: Optional[bool] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("emailVerified") is not None:
            kwargs["email_verified"] = data["emailVerified"]

        if data.get("imageUrl") is not None:
            kwargs["image_url"] = data["imageUrl"]

        if data.get("disabled") is not None:
            kwargs["disabled"] = data["disabled"]

        return User(**kwargs)