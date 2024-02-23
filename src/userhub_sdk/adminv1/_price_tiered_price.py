# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List

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
    tiers: List[TieredPriceTier] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.mode is not None:
            data["mode"] = self.mode

        if self.tiers is not None:
            data["tiers"] = [TieredPriceTier.__json_encode__(v) for v in self.tiers]

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PriceTieredPrice":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("mode") is not None:
            kwargs["mode"] = data["mode"]

        if data.get("tiers") is not None:
            kwargs["tiers"] = [
                TieredPriceTier.__json_decode__(v) for v in data["tiers"]
            ]

        return PriceTieredPrice(**kwargs)
