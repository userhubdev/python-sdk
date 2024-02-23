# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class SignupFlow:
    """
    The signup flow.
    """

    #: The email address of the invitee.
    email: str = ""
    #: The display name of the invitee.
    display_name: Optional[str] = None
    #: Whether to create an organization as part of the signup flow.
    create_organization: Optional[bool] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.email is not None:
            data["email"] = self.email

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.create_organization is not None:
            data["createOrganization"] = self.create_organization

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "SignupFlow":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("createOrganization") is not None:
            kwargs["create_organization"] = data["createOrganization"]

        return SignupFlow(**kwargs)
