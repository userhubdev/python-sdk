# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class JoinOrganizationFlow:
    """
    The join organization flow.
    """

    #: The display name of the invitee.
    display_name: Optional[str] = None
    #: The email address of the invitee.
    email: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

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

        return JoinOrganizationFlow(**kwargs)
