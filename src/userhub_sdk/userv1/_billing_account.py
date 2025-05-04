# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional

from userhub_sdk import commonv1

from ._billing_account_checkout import BillingAccountCheckout
from ._payment_method import PaymentMethod
from ._subscription import Subscription


@dataclasses.dataclass
class BillingAccount:
    """
    The billing account for an organization or user.
    """

    #: The status of the billing account.
    state: str = ""
    #: The human-readable display name of the billing account.
    display_name: Optional[str] = None
    #: The email address of the billing account.
    email: Optional[str] = None
    #: The E164 phone number for the billing account (e.g. `+12125550123`).
    phone_number: Optional[str] = None
    #: The billing address for the billing account.
    address: Optional[commonv1.Address] = None
    #: The ISO-4217 currency code for the billing account (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The balance amount for the account.
    #:
    #: A negative value indicates an amount which will be subtracted from the next
    #: invoice (credit).
    #:
    #: A positive value indicates an amount which will be added to the next
    #: invoice (debt).
    balance_amount: Optional[str] = None
    #: The available checkouts.
    checkouts: Optional[List[BillingAccountCheckout]] = dataclasses.field(
        default_factory=list
    )
    #: The default and latest 10 payment methods for the account.
    payment_methods: Optional[List[PaymentMethod]] = dataclasses.field(
        default_factory=list
    )
    #: The subscription for the account.
    subscription: Optional[Subscription] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.state is not None:
            data["state"] = self.state

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        if self.phone_number is not None:
            data["phoneNumber"] = self.phone_number

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.balance_amount is not None:
            data["balanceAmount"] = self.balance_amount

        if self.checkouts is not None:
            data["checkouts"] = [
                BillingAccountCheckout.__json_encode__(v) for v in self.checkouts
            ]

        if self.payment_methods is not None:
            data["paymentMethods"] = [
                PaymentMethod.__json_encode__(v) for v in self.payment_methods
            ]

        if self.subscription is not None:
            data["subscription"] = Subscription.__json_encode__(self.subscription)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "BillingAccount":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("phoneNumber") is not None:
            kwargs["phone_number"] = data["phoneNumber"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("balanceAmount") is not None:
            kwargs["balance_amount"] = data["balanceAmount"]

        if data.get("checkouts") is not None:
            kwargs["checkouts"] = [
                BillingAccountCheckout.__json_decode__(v) for v in data["checkouts"]
            ]

        if data.get("paymentMethods") is not None:
            kwargs["payment_methods"] = [
                PaymentMethod.__json_decode__(v) for v in data["paymentMethods"]
            ]

        if data.get("subscription") is not None:
            kwargs["subscription"] = Subscription.__json_decode__(data["subscription"])

        return BillingAccount(**kwargs)
