# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util
from ._payment_method import PaymentMethod
from ._subscription import Subscription


@dataclasses.dataclass
class BillingAccount:
    """
    The billing account for an organization or user.
    """

    #: The status of the billing account.
    state: Optional[str] = None
    #: The balance amount for the account.
    #:
    #: A negative value indicates an amount which will be subtracted from the next
    #: invoice (credit).
    #:
    #: A positive value indicates an amount which will be added to the next
    #: invoice (debt).
    balance_amount: Optional[str] = None
    #: The ISO-4217 currency code for the account (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The default and latest 10 payment methods for the account.
    payment_methods: Optional[List[PaymentMethod]] = dataclasses.field(
        default_factory=list
    )
    #: The subscription for the account.
    subscription: Optional[Subscription] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("balanceAmount") is not None:
            kwargs["balance_amount"] = data["balanceAmount"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("paymentMethods") is not None:
            kwargs["payment_methods"] = [
                PaymentMethod.__json_decode__(v) for v in data["paymentMethods"]
            ]

        if data.get("subscription") is not None:
            kwargs["subscription"] = Subscription.__json_decode__(data["subscription"])

        return BillingAccount(**kwargs)
