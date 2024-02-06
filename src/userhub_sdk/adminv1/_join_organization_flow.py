# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class JoinOrganizationFlow:
    """
    The join organization flow.
    """

    #: The display name of the invitee.
    display_name: Optional[str] = None
    #: The email address of the invitee.
    email: Optional[str] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        return JoinOrganizationFlow(**kwargs)
