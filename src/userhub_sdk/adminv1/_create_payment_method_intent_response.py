# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional


@dataclasses.dataclass
class CreatePaymentMethodIntentResponse:
    """
    Response message for CreatePaymentMethodIntent.
    """

    #: The setup token for the billing system (e.g. Stripe SetupIntent
    #: Client Secret). This is generally used by a frontend
    #: client to securely setup a payment method, the result of which
    #: can be passed to CreatePaymentMethod to complete the setup
    #: process.
    token: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.token is not None:
            data["token"] = self.token

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("token") is not None:
            kwargs["token"] = data["token"]

        return CreatePaymentMethodIntentResponse(**kwargs)
