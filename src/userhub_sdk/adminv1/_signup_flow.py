# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class SignupFlow:
    """
    The signup flow.
    """

    #: The email address of the invitee.
    email: Optional[str] = None
    #: The display name of the invitee.
    display_name: Optional[str] = None
    #: Whether to create an organization as part of the signup flow.
    create_organization: Optional[bool] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("createOrganization") is not None:
            kwargs["create_organization"] = data["createOrganization"]

        return SignupFlow(**kwargs)
