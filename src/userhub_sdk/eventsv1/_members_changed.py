# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import adminv1
from .._internal import util


@dataclasses.dataclass
class MembersChanged:
    """
    The members changed event.
    """

    #: The organization.
    organization: Optional[adminv1.Organization] = None
    #: The member.
    member: Optional[adminv1.Member] = None

    def __json_encode__(self):
        data = {}

        if self.organization is not None:
            data["organization"] = adminv1.Organization.__json_encode__(
                self.organization
            )

        if self.member is not None:
            data["member"] = adminv1.Member.__json_encode__(self.member)

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("organization") is not None:
            kwargs["organization"] = adminv1.Organization.__json_decode__(
                data["organization"]
            )

        if data.get("member") is not None:
            kwargs["member"] = adminv1.Member.__json_decode__(data["member"])

        return MembersChanged(**kwargs)
