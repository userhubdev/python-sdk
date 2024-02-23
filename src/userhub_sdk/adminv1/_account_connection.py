# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import constants, util

from ._connection import Connection
from ._payment_method import PaymentMethod


@dataclasses.dataclass
class AccountConnection:
    """
    A link between a account and an external account.
    """

    #: The tenant connection.
    connection: Optional[Connection] = None
    #: The external identifier of the connected account.
    external_id: str = ""
    #: The external admin URL for the connected account.
    admin_url: Optional[str] = None
    #: The status of the connected account.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The balance amount for the account.
    #:
    #: A negative value indicates an amount which will be subtracted from the next
    #: invoice (credit).
    #:
    #: A positive value indicates an amount which will be added to the next
    #: invoice (debt).
    balance_amount: Optional[str] = None
    #: The currency code for the account.
    currency_code: Optional[str] = None
    #: The payment methods for connections that support it.
    payment_methods: Optional[List[PaymentMethod]] = dataclasses.field(
        default_factory=list
    )
    #: The last time the account was pulled from the connection.
    pull_time: Optional[datetime.datetime] = None
    #: The last time the account was pushed to the connection.
    push_time: Optional[datetime.datetime] = None
    #: The creation time of the account connection.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the account connection.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.connection is not None:
            data["connection"] = Connection.__json_encode__(self.connection)

        if self.external_id is not None:
            data["externalId"] = self.external_id

        if self.admin_url is not None:
            data["adminUrl"] = self.admin_url

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

        if self.balance_amount is not None:
            data["balanceAmount"] = self.balance_amount

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.payment_methods is not None:
            data["paymentMethods"] = [
                PaymentMethod.__json_encode__(v) for v in self.payment_methods
            ]

        if self.pull_time is not None:
            data["pullTime"] = util.encode_datetime(self.pull_time)

        if self.push_time is not None:
            data["pushTime"] = util.encode_datetime(self.push_time)

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "AccountConnection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("connection") is not None:
            kwargs["connection"] = Connection.__json_decode__(data["connection"])

        if data.get("externalId") is not None:
            kwargs["external_id"] = data["externalId"]

        if data.get("adminUrl") is not None:
            kwargs["admin_url"] = data["adminUrl"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

        if data.get("balanceAmount") is not None:
            kwargs["balance_amount"] = data["balanceAmount"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("paymentMethods") is not None:
            kwargs["payment_methods"] = [
                PaymentMethod.__json_decode__(v) for v in data["paymentMethods"]
            ]

        if data.get("pullTime") is not None:
            kwargs["pull_time"] = util.decode_datetime(data["pullTime"])

        if data.get("pushTime") is not None:
            kwargs["push_time"] = util.decode_datetime(data["pushTime"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return AccountConnection(**kwargs)
