# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk import commonv1
from userhub_sdk._internal import constants, util

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
    external_id: str = ""
    #: The status of the connected price.
    state: str = ""
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
    archived: bool = False
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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.connection is not None:
            data["connection"] = Connection.__json_encode__(self.connection)

        if self.external_id is not None:
            data["externalId"] = self.external_id

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.billing_mode is not None:
            data["billingMode"] = self.billing_mode

        if self.interval is not None:
            data["interval"] = commonv1.Interval.__json_encode__(self.interval)

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.product is not None:
            data["product"] = Product.__json_encode__(self.product)

        if self.archived is not None:
            data["archived"] = self.archived

        if self.pull_time is not None:
            data["pullTime"] = util.encode_datetime(self.pull_time)

        if self.push_time is not None:
            data["pushTime"] = util.encode_datetime(self.push_time)

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

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
