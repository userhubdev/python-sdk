# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional


@dataclasses.dataclass
class Email:
    """
    An email address.
    """

    #: The email address (e.g. `jane@example.com`).
    address: Optional[str] = None
    #: The email name (e.g. `Jane Doe`).
    display_name: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.address is not None:
            data["address"] = self.address

        if self.display_name is not None:
            data["displayName"] = self.display_name

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("address") is not None:
            kwargs["address"] = data["address"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        return Email(**kwargs)
