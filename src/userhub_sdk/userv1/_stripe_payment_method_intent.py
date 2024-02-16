# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.account_id is not None:
            data["accountId"] = self.account_id

        if self.live is not None:
            data["live"] = self.live

        if self.client_secret is not None:
            data["clientSecret"] = self.client_secret

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "StripePaymentMethodIntent":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("accountId") is not None:
            kwargs["account_id"] = data["accountId"]

        if data.get("live") is not None:
            kwargs["live"] = data["live"]

        if data.get("clientSecret") is not None:
            kwargs["client_secret"] = data["clientSecret"]

        return StripePaymentMethodIntent(**kwargs)
