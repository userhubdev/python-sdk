# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from userhub_sdk import adminv1


@dataclasses.dataclass
class OrganizationsChanged:
    """
    The organizations changed event.
    """

    #: The organization.
    organization: Optional[adminv1.Organization] = None

    def __json_encode__(self):
        data = {}

        if self.organization is not None:
            data["organization"] = adminv1.Organization.__json_encode__(
                self.organization
            )

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

        return OrganizationsChanged(**kwargs)
