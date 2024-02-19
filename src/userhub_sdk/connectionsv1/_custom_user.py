# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        if self.email_verified is not None:
            data["emailVerified"] = self.email_verified

        if self.phone_number is not None:
            data["phoneNumber"] = self.phone_number

        if self.phone_number_verified is not None:
            data["phoneNumberVerified"] = self.phone_number_verified

        if self.image_url is not None:
            data["imageUrl"] = self.image_url

        if self.disabled is not None:
            data["disabled"] = self.disabled

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CustomUser":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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
