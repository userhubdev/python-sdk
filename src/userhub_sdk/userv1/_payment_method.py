# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from userhub_sdk import commonv1
from userhub_sdk._internal import constants, util

from ._card_payment_method import CardPaymentMethod


@dataclasses.dataclass
class PaymentMethod:
    """
    A link to an external payment method (e.g. credit card, bank account).
    """

    #: The system-assigned identifier of the payment method.
    id: Optional[str] = None
    #: The payment method type.
    type: str = ""
    #: A human readable description of the payment method.
    #:
    #: This can be used to show a description of the payment method
    #: when the type is UNKNOWN or not explicitly handled.
    display_name: Optional[str] = None
    #: The full name of the owner of the payment method.
    full_name: Optional[str] = None
    #: The address for the payment method.
    address: Optional[commonv1.Address] = None
    #: Whether the payment method is the default for the account.
    default: Optional[bool] = None
    #: The creation time of the payment method connection.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the payment method connection.
    update_time: datetime.datetime = constants.EMPTY_DATETIME
    #: Card payment method (e.g. Visa credit card).
    card: Optional[CardPaymentMethod] = None

    def __json_encode__(self):
        data = {}

        if self.id is not None:
            data["id"] = self.id

        if self.type is not None:
            data["type"] = self.type

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.full_name is not None:
            data["fullName"] = self.full_name

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        if self.default is not None:
            data["default"] = self.default

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        if self.card is not None:
            data["card"] = CardPaymentMethod.__json_encode__(self.card)

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("fullName") is not None:
            kwargs["full_name"] = data["fullName"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        if data.get("default") is not None:
            kwargs["default"] = data["default"]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        if data.get("card") is not None:
            kwargs["card"] = CardPaymentMethod.__json_decode__(data["card"])

        return PaymentMethod(**kwargs)
