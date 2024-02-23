# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class Email:
    """
    An email address.
    """

    #: The email address (e.g. `jane@example.com`).
    address: str = ""
    #: The email name (e.g. `Jane Doe`).
    display_name: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.address is not None:
            data["address"] = self.address

        if self.display_name is not None:
            data["displayName"] = self.display_name

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Email":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("address") is not None:
            kwargs["address"] = data["address"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        return Email(**kwargs)
