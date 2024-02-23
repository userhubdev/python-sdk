# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import commonv1

from ._price_fixed_price import PriceFixedPrice
from ._price_tiered_price import PriceTieredPrice


@dataclasses.dataclass
class Price:
    """
    Price for a product.
    """

    #: The system-assigned identifier of the price.
    id: str = ""
    #: The currency for the price.
    currency_code: str = ""
    #: The billing mode for the price.
    billing_mode: str = ""
    #: The billing interval for the price.
    interval: Optional[commonv1.Interval] = None
    #: The price is fixed per quantity.
    fixed: Optional[PriceFixedPrice] = None
    #: The price is dependent on the quantity.
    tiered: Optional[PriceTieredPrice] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.billing_mode is not None:
            data["billingMode"] = self.billing_mode

        if self.interval is not None:
            data["interval"] = commonv1.Interval.__json_encode__(self.interval)

        if self.fixed is not None:
            data["fixed"] = PriceFixedPrice.__json_encode__(self.fixed)

        if self.tiered is not None:
            data["tiered"] = PriceTieredPrice.__json_encode__(self.tiered)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Price":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("billingMode") is not None:
            kwargs["billing_mode"] = data["billingMode"]

        if data.get("interval") is not None:
            kwargs["interval"] = commonv1.Interval.__json_decode__(data["interval"])

        if data.get("fixed") is not None:
            kwargs["fixed"] = PriceFixedPrice.__json_decode__(data["fixed"])

        if data.get("tiered") is not None:
            kwargs["tiered"] = PriceTieredPrice.__json_decode__(data["tiered"])

        return Price(**kwargs)
