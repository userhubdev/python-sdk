# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.product is not None:
            data["product"] = Product.__json_encode__(self.product)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "AccountSubscriptionPlan":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        return AccountSubscriptionPlan(**kwargs)
