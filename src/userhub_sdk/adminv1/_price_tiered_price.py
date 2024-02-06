# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util
from ._tiered_price_tier import TieredPriceTier


@dataclasses.dataclass
class PriceTieredPrice:
    """
    A pricing strategy that dynamically sets the price for a given
    quantity range.
    """

    #: The strategy for evaluating the tiers.
    mode: str = ""
    #: The tiers for the price.
    tiers: Optional[List[TieredPriceTier]] = dataclasses.field(default_factory=list)

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("mode") is not None:
            kwargs["mode"] = data["mode"]

        if data.get("tiers") is not None:
            kwargs["tiers"] = [
                TieredPriceTier.__json_decode__(v) for v in data["tiers"]
            ]

        return PriceTieredPrice(**kwargs)
