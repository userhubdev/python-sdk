# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .. import commonv1
from .._internal import constants
from .._internal import util
from ._connection import Connection
from ._price_fixed_price import PriceFixedPrice
from ._price_tiered_price import PriceTieredPrice
from ._product import Product


@dataclasses.dataclass
class Price:
    """
    Price for a product.
    """

    #: The system-assigned identifier of the price.
    id: str = ""
    #: The connection.
    connection: Optional[Connection] = None
    #: The external identifier of the connected price.
    external_id: Optional[str] = None
    #: The status of the connected price.
    state: Optional[str] = None
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The currency for the price.
    currency_code: str = ""
    #: The billing mode for the price.
    billing_mode: str = ""
    #: The billing interval for the price.
    interval: Optional[commonv1.Interval] = None
    #: The admin-facing display name of the price.
    display_name: Optional[str] = None
    #: The product associated with the price.
    product: Optional[Product] = None
    #: The archived status of the price.
    #:
    #: It determines if the price can be used.
    archived: Optional[bool] = None
    #: The last time the price was pulled from the connection.
    pull_time: Optional[datetime.datetime] = None
    #: The last time the price was pushed to the connection.
    push_time: Optional[datetime.datetime] = None
    #: The creation time of the price.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the price.
    update_time: datetime.datetime = constants.EMPTY_DATETIME
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

        if data.get("connection") is not None:
            kwargs["connection"] = Connection.__json_decode__(data["connection"])

        if data.get("externalId") is not None:
            kwargs["external_id"] = data["externalId"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("billingMode") is not None:
            kwargs["billing_mode"] = data["billingMode"]

        if data.get("interval") is not None:
            kwargs["interval"] = commonv1.Interval.__json_decode__(data["interval"])

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        if data.get("archived") is not None:
            kwargs["archived"] = data["archived"]

        if data.get("pullTime") is not None:
            kwargs["pull_time"] = util.decode_datetime(data["pullTime"])

        if data.get("pushTime") is not None:
            kwargs["push_time"] = util.decode_datetime(data["pushTime"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        if data.get("fixed") is not None:
            kwargs["fixed"] = PriceFixedPrice.__json_decode__(data["fixed"])

        if data.get("tiered") is not None:
            kwargs["tiered"] = PriceTieredPrice.__json_decode__(data["tiered"])

        return Price(**kwargs)
