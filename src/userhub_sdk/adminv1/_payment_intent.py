# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._stripe_payment_intent import StripePaymentIntent


@dataclasses.dataclass
class PaymentIntent:
    """
    An object to track payments.
    """

    #: A Stripe payment intent.
    stripe: Optional[StripePaymentIntent] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.stripe is not None:
            data["stripe"] = StripePaymentIntent.__json_encode__(self.stripe)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PaymentIntent":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("stripe") is not None:
            kwargs["stripe"] = StripePaymentIntent.__json_decode__(data["stripe"])

        return PaymentIntent(**kwargs)
