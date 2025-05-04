# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._stripe_payment_method_intent import StripePaymentMethodIntent


@dataclasses.dataclass
class PaymentMethodIntent:
    """
    Configuration for setting up a payment method.
    """

    #: A Stripe Setup Intent.
    stripe: Optional[StripePaymentMethodIntent] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.stripe is not None:
            data["stripe"] = StripePaymentMethodIntent.__json_encode__(self.stripe)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PaymentMethodIntent":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("stripe") is not None:
            kwargs["stripe"] = StripePaymentMethodIntent.__json_decode__(data["stripe"])

        return PaymentMethodIntent(**kwargs)
