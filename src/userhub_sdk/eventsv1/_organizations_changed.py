# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict

from userhub_sdk import adminv1


@dataclasses.dataclass
class OrganizationsChanged:
    """
    The organizations changed event.
    """

    #: The organization.
    organization: adminv1.Organization = dataclasses.field(
        default_factory=adminv1.Organization
    )

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.organization is not None:
            data["organization"] = adminv1.Organization.__json_encode__(
                self.organization
            )

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "OrganizationsChanged":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("organization") is not None:
            kwargs["organization"] = adminv1.Organization.__json_decode__(
                data["organization"]
            )

        return OrganizationsChanged(**kwargs)
