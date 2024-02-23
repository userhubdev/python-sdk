# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict

from ._price import Price
from ._product import Product


@dataclasses.dataclass
class PlanItem:
    """
    The plan products.
    """

    #: The product associated with the item.
    product: Product = dataclasses.field(default_factory=Product)
    #: The price associated with them item.
    price: Price = dataclasses.field(default_factory=Price)
    #: The plan item type.
    type: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.product is not None:
            data["product"] = Product.__json_encode__(self.product)

        if self.price is not None:
            data["price"] = Price.__json_encode__(self.price)

        if self.type is not None:
            data["type"] = self.type

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanItem":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        if data.get("price") is not None:
            kwargs["price"] = Price.__json_decode__(data["price"])

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        return PlanItem(**kwargs)
