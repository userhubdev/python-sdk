# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class Organization:
    """
    A group account.
    """

    #: The system-assigned identifier of the organization.
    id: str = ""
    #: The client defined unique identifier of the organization account.
    unique_id: Optional[str] = None
    #: The human-readable display name of the organization.
    display_name: Optional[str] = None
    #: The email address of the organization.
    email: Optional[str] = None
    #: Whether the organization's email address has been verified.
    email_verified: Optional[bool] = None
    #: The photo/avatar URL of the organization.
    image_url: Optional[str] = None
    #: Whether the organization is disabled.
    disabled: Optional[bool] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        if self.email_verified is not None:
            data["emailVerified"] = self.email_verified

        if self.image_url is not None:
            data["imageUrl"] = self.image_url

        if self.disabled is not None:
            data["disabled"] = self.disabled

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Organization":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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

        return Organization(**kwargs)
