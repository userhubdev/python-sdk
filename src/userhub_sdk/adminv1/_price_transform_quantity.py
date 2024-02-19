# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class PriceTransformQuantity:
    """
    A quantity transform for fixed prices.
    """

    #: The amount to divide the quantity by.
    divisor: int = 0
    #: Whether to round the result up or down.
    round: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.divisor is not None:
            data["divisor"] = self.divisor

        if self.round is not None:
            data["round"] = self.round

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PriceTransformQuantity":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("divisor") is not None:
            kwargs["divisor"] = data["divisor"]

        if data.get("round") is not None:
            kwargs["round"] = data["round"]

        return PriceTransformQuantity(**kwargs)
