# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk import apiv1, commonv1
from userhub_sdk._internal import constants, util

from ._card_payment_method import CardPaymentMethod


@dataclasses.dataclass
class PaymentMethod:
    """
    A link to an external payment method (e.g. credit card, bank account).
    """

    #: The system-assigned identifier of the payment method.
    id: str = ""
    #: The external identifier of the connected payment method.
    external_id: str = ""
    #: The status of the connected payment method.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The payment method type.
    type: str = ""
    #: A human-readable description of the payment method.
    #:
    #: This can be used to show a description of the payment method
    #: when the type is UNKNOWN or not explicitly handled.
    display_name: str = ""
    #: The full name of the owner of the payment method.
    full_name: Optional[str] = None
    #: The address for the payment method.
    address: Optional[commonv1.Address] = None
    #: Whether the payment method is the default for the connected account.
    default: Optional[bool] = None
    #: The last payment error.
    #:
    #: This will be unset if the payment method is updated
    #: or if a payment succeeds.
    last_payment_error: Optional[apiv1.Status] = None
    #: The last time the payment method was pulled from the connection.
    pull_time: Optional[datetime.datetime] = None
    #: The creation time of the payment method connection.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the payment method connection.
    update_time: datetime.datetime = constants.EMPTY_DATETIME
    #: Card payment method (e.g. Visa credit card).
    card: Optional[CardPaymentMethod] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.external_id is not None:
            data["externalId"] = self.external_id

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

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

        if self.last_payment_error is not None:
            data["lastPaymentError"] = apiv1.Status.__json_encode__(
                self.last_payment_error
            )

        if self.pull_time is not None:
            data["pullTime"] = util.encode_datetime(self.pull_time)

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        if self.card is not None:
            data["card"] = CardPaymentMethod.__json_encode__(self.card)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PaymentMethod":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("externalId") is not None:
            kwargs["external_id"] = data["externalId"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

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

        if data.get("lastPaymentError") is not None:
            kwargs["last_payment_error"] = apiv1.Status.__json_decode__(
                data["lastPaymentError"]
            )

        if data.get("pullTime") is not None:
            kwargs["pull_time"] = util.decode_datetime(data["pullTime"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        if data.get("card") is not None:
            kwargs["card"] = CardPaymentMethod.__json_decode__(data["card"])

        return PaymentMethod(**kwargs)
