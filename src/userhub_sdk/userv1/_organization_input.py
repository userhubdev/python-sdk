# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


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

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        return OrganizationInput(**kwargs)
