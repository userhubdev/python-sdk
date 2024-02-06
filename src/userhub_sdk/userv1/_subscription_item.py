# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
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
    product: Optional[Product] = None
    #: The details of the associated price.
    price: Optional[Price] = None
    #: The quantity for the item.
    quantity: int = 0

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        if data.get("price") is not None:
            kwargs["price"] = Price.__json_decode__(data["price"])

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        return SubscriptionItem(**kwargs)
