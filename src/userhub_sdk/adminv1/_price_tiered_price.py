# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List

from ._price_tiered_price_tier import PriceTieredPriceTier


@dataclasses.dataclass
class PriceTieredPrice:
    """
    A pricing strategy that dynamically sets the price for a given
    quantity range.
    """

    #: The strategy for evaluating the tiers.
    mode: str = ""
    #: The tiers for the price.
    tiers: List[PriceTieredPriceTier] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.mode is not None:
            data["mode"] = self.mode

        if self.tiers is not None:
            data["tiers"] = [
                PriceTieredPriceTier.__json_encode__(v) for v in self.tiers
            ]

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
                PriceTieredPriceTier.__json_decode__(v) for v in data["tiers"]
            ]

        return PriceTieredPrice(**kwargs)
