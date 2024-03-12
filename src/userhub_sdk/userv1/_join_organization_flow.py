# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._role import Role


@dataclasses.dataclass
class JoinOrganizationFlow:
    """
    The join organization flow.
    """

    #: The display name of the invitee.
    display_name: Optional[str] = None
    #: The email address of the invitee.
    #:
    #: This is required if a user isn't provided
    #: or the user's email address is empty.
    email: Optional[str] = None
    #: The role to be assigned to the invitee.
    role: Optional[Role] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        if self.role is not None:
            data["role"] = Role.__json_encode__(self.role)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "JoinOrganizationFlow":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("role") is not None:
            kwargs["role"] = Role.__json_decode__(data["role"])

        return JoinOrganizationFlow(**kwargs)
