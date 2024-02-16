# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.amount is not None:
            data["amount"] = self.amount

        if self.transform_quantity is not None:
            data["transformQuantity"] = PriceTransformQuantity.__json_encode__(
                self.transform_quantity
            )

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PriceFixedPrice":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("amount") is not None:
            kwargs["amount"] = data["amount"]

        if data.get("transformQuantity") is not None:
            kwargs["transform_quantity"] = PriceTransformQuantity.__json_decode__(
                data["transformQuantity"]
            )

        return PriceFixedPrice(**kwargs)
