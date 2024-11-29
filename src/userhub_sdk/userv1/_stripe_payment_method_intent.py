# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


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
    #: The Stripe.js Payment Element options.
    payment_element_options: Optional[Dict[str, Any]] = dataclasses.field(
        default_factory=dict
    )

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.account_id is not None:
            data["accountId"] = self.account_id

        if self.live is not None:
            data["live"] = self.live

        if self.client_secret is not None:
            data["clientSecret"] = self.client_secret

        if self.payment_element_options is not None:
            data["paymentElementOptions"] = self.payment_element_options

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

        if data.get("paymentElementOptions") is not None:
            kwargs["payment_element_options"] = data["paymentElementOptions"]

        return StripePaymentMethodIntent(**kwargs)
