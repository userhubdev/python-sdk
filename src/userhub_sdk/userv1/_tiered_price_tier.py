# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class TieredPriceTier:
    """
    A quantity range within the tiered price.
    """

    #: The upper quantity for tier (inclusive).
    upper: Optional[int] = None
    #: The per quantity amount for the tier.
    unit_amount: Optional[str] = None
    #: The flat amount for the tier.
    flat_amount: Optional[str] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("upper") is not None:
            kwargs["upper"] = data["upper"]

        if data.get("unitAmount") is not None:
            kwargs["unit_amount"] = data["unitAmount"]

        if data.get("flatAmount") is not None:
            kwargs["flat_amount"] = data["flatAmount"]

        return TieredPriceTier(**kwargs)
