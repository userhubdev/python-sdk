# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._payment_intent import PaymentIntent


@dataclasses.dataclass
class CheckoutCompletePaymentStep:
    """
    The complete payment step details.
    """

    #: The payment intent for the checkout.
    payment_intent: Optional[PaymentIntent] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.payment_intent is not None:
            data["paymentIntent"] = PaymentIntent.__json_encode__(self.payment_intent)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutCompletePaymentStep":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("paymentIntent") is not None:
            kwargs["payment_intent"] = PaymentIntent.__json_decode__(
                data["paymentIntent"]
            )

        return CheckoutCompletePaymentStep(**kwargs)
