# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class OrganizationInput:
    """
    Organization input parameters.
    """

    #: The client defined unique identifier of the organization account.
    #:
    #: It is restricted to letters, numbers, underscores, and hyphens,
    #: with the first character a letter or a number, and a 255
    #: character maximum.
    #:
    #: ID's starting with `org_` are reserved.
    unique_id: Optional[str] = None
    #: The human-readable display name of the organization.
    #:
    #: The maximum length is 200 characters.
    display_name: Optional[str] = None
    #: The email address of the organization.
    #:
    #: The maximum length is 320 characters.
    email: Optional[str] = None
    #: The flow identifier associated with the creation of the organization.
    #:
    #: The flow type must be `SIGNUP` and associated with the user creating the organization.
    flow_id: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        if self.flow_id is not None:
            data["flowId"] = self.flow_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "OrganizationInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("flowId") is not None:
            kwargs["flow_id"] = data["flowId"]

        return OrganizationInput(**kwargs)
