# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class StripePaymentMethodIntent:
    """
    A Stripe Setup Intent.
    """

    #: The Stripe account ID (e.g. `acct_1LcUvxQYGbxD2SPK`)
    account_id: str = ""
    #: Whether the Stripe Setup Intent was created in live mode.
    live: bool = False
    #: The Stripe Setup Intent client secret.
    client_secret: str = ""

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("accountId") is not None:
            kwargs["account_id"] = data["accountId"]

        if data.get("live") is not None:
            kwargs["live"] = data["live"]

        if data.get("clientSecret") is not None:
            kwargs["client_secret"] = data["clientSecret"]

        return StripePaymentMethodIntent(**kwargs)
