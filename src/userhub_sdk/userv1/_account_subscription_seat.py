# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._product import Product


@dataclasses.dataclass
class AccountSubscriptionSeat:
    """
    The user's seat information.
    """

    #: The seat product.
    product: Optional[Product] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.product is not None:
            data["product"] = Product.__json_encode__(self.product)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "AccountSubscriptionSeat":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        return AccountSubscriptionSeat(**kwargs)
