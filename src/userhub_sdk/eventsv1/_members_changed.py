# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict

from userhub_sdk import adminv1


@dataclasses.dataclass
class MembersChanged:
    """
    The members changed event.
    """

    #: The organization.
    organization: adminv1.Organization = dataclasses.field(
        default_factory=adminv1.Organization
    )
    #: The member.
    member: adminv1.Member = dataclasses.field(default_factory=adminv1.Member)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.organization is not None:
            data["organization"] = adminv1.Organization.__json_encode__(
                self.organization
            )

        if self.member is not None:
            data["member"] = adminv1.Member.__json_encode__(self.member)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "MembersChanged":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("organization") is not None:
            kwargs["organization"] = adminv1.Organization.__json_decode__(
                data["organization"]
            )

        if data.get("member") is not None:
            kwargs["member"] = adminv1.Member.__json_decode__(data["member"])

        return MembersChanged(**kwargs)
