# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional


@dataclasses.dataclass
class AccountSubscriptionProduct:
    """
    The subscription product.
    """

    #: The system-assigned identifier of the product.
    id: Optional[str] = None
    #: The client defined unique identifier of the product.
    unique_id: Optional[str] = None
    #: The human-readable display name of the product.
    display_name: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.id is not None:
            data["id"] = self.id

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        return AccountSubscriptionProduct(**kwargs)
