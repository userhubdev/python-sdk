# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from ._product import Product


@dataclasses.dataclass
class AccountSubscriptionPlan:
    """
    The plan information.
    """

    #: The identifier of the plan.
    id: Optional[str] = None
    #: The human-readable display name of the plan.
    display_name: Optional[str] = None
    #: The plan product.
    product: Optional[Product] = None

    def __json_encode__(self):
        data = {}

        if self.id is not None:
            data["id"] = self.id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.product is not None:
            data["product"] = Product.__json_encode__(self.product)

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        return AccountSubscriptionPlan(**kwargs)
