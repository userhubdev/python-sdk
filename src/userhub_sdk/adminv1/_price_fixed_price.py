# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._price_transform_quantity import PriceTransformQuantity


@dataclasses.dataclass
class PriceFixedPrice:
    """
    A pricing strategy that defines a constant price per
    quantity.
    """

    #: The decimal amount for the defined currency (e.g. `9.95`).
    amount: str = ""
    #: Whether to transform the quantity before multiplying amount.
    transform_quantity: Optional[PriceTransformQuantity] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("amount") is not None:
            kwargs["amount"] = data["amount"]

        if data.get("transformQuantity") is not None:
            kwargs["transform_quantity"] = PriceTransformQuantity.__json_decode__(
                data["transformQuantity"]
            )

        return PriceFixedPrice(**kwargs)
