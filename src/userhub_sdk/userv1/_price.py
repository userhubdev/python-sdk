# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import commonv1
from .._internal import util
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
    currency_code: Optional[str] = None
    #: The billing mode for the price.
    billing_mode: Optional[str] = None
    #: The billing interval for the price.
    interval: Optional[commonv1.Interval] = None
    #: The price is fixed per quantity.
    fixed: Optional[PriceFixedPrice] = None
    #: The price is dependent on the quantity.
    tiered: Optional[PriceTieredPrice] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

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
