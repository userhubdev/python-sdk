# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._stripe_payment_intent import StripePaymentIntent


@dataclasses.dataclass
class PaymentIntent:
    """
    An object to track payments.
    """

    #: A Stripe payment intent.
    stripe: Optional[StripePaymentIntent] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("stripe") is not None:
            kwargs["stripe"] = StripePaymentIntent.__json_decode__(data["stripe"])

        return PaymentIntent(**kwargs)
