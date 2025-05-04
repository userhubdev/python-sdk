# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._price import Price
from ._product import Product


@dataclasses.dataclass
class SubscriptionItem:
    """
    The subscription items.
    """

    #: The identifier of the item.
    id: str = ""
    #: The details of the associated product.
    product: Product = dataclasses.field(default_factory=Product)
    #: The details of the associated price.
    price: Optional[Price] = None
    #: The quantity for the item.
    quantity: int = 0

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.product is not None:
            data["product"] = Product.__json_encode__(self.product)

        if self.price is not None:
            data["price"] = Price.__json_encode__(self.price)

        if self.quantity is not None:
            data["quantity"] = self.quantity

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "SubscriptionItem":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        if data.get("price") is not None:
            kwargs["price"] = Price.__json_decode__(data["price"])

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        return SubscriptionItem(**kwargs)
