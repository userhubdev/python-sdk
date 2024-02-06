# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class PriceTransformQuantity:
    """
    A quantity transform for fixed prices.
    """

    #: The amount to divide the quantity by.
    divisor: int = 0
    #: Whether to round the result up or down.
    round: str = ""

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("divisor") is not None:
            kwargs["divisor"] = data["divisor"]

        if data.get("round") is not None:
            kwargs["round"] = data["round"]

        return PriceTransformQuantity(**kwargs)
