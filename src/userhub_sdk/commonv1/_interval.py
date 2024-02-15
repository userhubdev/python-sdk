# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class Interval:
    """
    A time interval.
    """

    #: The interval quantity.
    quantity: int = 0
    #: The interval unit.
    unit: str = ""

    def __json_encode__(self):
        data = {}

        if self.quantity is not None:
            data["quantity"] = self.quantity

        if self.unit is not None:
            data["unit"] = self.unit

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        if data.get("unit") is not None:
            kwargs["unit"] = data["unit"]

        return Interval(**kwargs)
