# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class CustomUser:
    """
    The user object for the Custom Users connection.
    """

    #: The external identifier for the user.
    id: str = ""
    #: The human-readable display name of the user.
    #:
    #: The maximum length is 200 characters.
    display_name: Optional[str] = None
    #: The email address of the user.
    #:
    #: The maximum length is 320 characters.
    email: Optional[str] = None
    #: Whether the user's email address has been verified.
    email_verified: Optional[bool] = None
    #: The E164 phone number for the user (e.g. `+12125550123`).
    phone_number: Optional[str] = None
    #: Whether the user's phone number has been verified.
    phone_number_verified: Optional[bool] = None
    #: The photo/avatar URL of the user.
    #:
    #: The maximum length is 2000 characters.
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

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("emailVerified") is not None:
            kwargs["email_verified"] = data["emailVerified"]

        if data.get("phoneNumber") is not None:
            kwargs["phone_number"] = data["phoneNumber"]

        if data.get("phoneNumberVerified") is not None:
            kwargs["phone_number_verified"] = data["phoneNumberVerified"]

        if data.get("imageUrl") is not None:
            kwargs["image_url"] = data["imageUrl"]

        if data.get("disabled") is not None:
            kwargs["disabled"] = data["disabled"]

        return CustomUser(**kwargs)
