# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._price import Price
from ._product import Product


@dataclasses.dataclass
class PlanItem:
    """
    The products which the plan includes.
    """

    #: The product associated with the item.
    product: Optional[Product] = None
    #: The price associated with them item.
    price: Optional[Price] = None
    #: The plan item type.
    type: str = ""

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        if data.get("price") is not None:
            kwargs["price"] = Price.__json_decode__(data["price"])

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        return PlanItem(**kwargs)
