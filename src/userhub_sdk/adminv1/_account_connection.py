# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk import commonv1
from userhub_sdk._internal import constants, util

from ._connection import Connection
from ._payment_method import PaymentMethod


@dataclasses.dataclass
class AccountConnection:
    """
    A link between an organization/user and an external account.
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
    #: The human-readable display name of the external account.
    display_name: Optional[str] = None
    #: The email address of the external account.
    email: Optional[str] = None
    #: Whether the external account's email address has been verified.
    email_verified: Optional[bool] = None
    #: The E164 phone number for the external account (e.g. `+12125550123`).
    phone_number: Optional[str] = None
    #: Whether the external account's phone number has been verified.
    phone_number_verified: Optional[bool] = None
    #: The billing address for the external account.
    address: Optional[commonv1.Address] = None
    #: The currency code for the account.
    currency_code: Optional[str] = None
    #: The balance amount for the account.
    #:
    #: A negative value indicates an amount which will be subtracted from the next
    #: invoice (credit).
    #:
    #: A positive value indicates an amount which will be added to the next
    #: invoice (debt).
    balance_amount: Optional[str] = None
    #: The payment methods for connections that support it.
    payment_methods: Optional[List[PaymentMethod]] = dataclasses.field(
        default_factory=list
    )
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

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        if self.email_verified is not None:
            data["emailVerified"] = self.email_verified

        if self.phone_number is not None:
            data["phoneNumber"] = self.phone_number

        if self.phone_number_verified is not None:
            data["phoneNumberVerified"] = self.phone_number_verified

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.balance_amount is not None:
            data["balanceAmount"] = self.balance_amount

        if self.payment_methods is not None:
            data["paymentMethods"] = [
                PaymentMethod.__json_encode__(v) for v in self.payment_methods
            ]

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

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("emailVerified") is not None:
            kwargs["email_verified"] = data["emailVerified"]

        if data.get("phoneNumber") is not None:
            kwargs["phone_number"] = data["phoneNumber"]

        if data.get("phoneNumberVerified") is not None:
            kwargs["phone_number_verified"] = data["phoneNumberVerified"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("balanceAmount") is not None:
            kwargs["balance_amount"] = data["balanceAmount"]

        if data.get("paymentMethods") is not None:
            kwargs["payment_methods"] = [
                PaymentMethod.__json_decode__(v) for v in data["paymentMethods"]
            ]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return AccountConnection(**kwargs)
