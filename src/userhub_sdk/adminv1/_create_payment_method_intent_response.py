# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class CreatePaymentMethodIntentResponse:
    """
    Response message for CreatePaymentMethodIntent.
    """

    #: The setup token for the billing system (e.g. Stripe SetupIntent
    #: Client Secret). This is generally used by a frontend
    #: client to securely set up a payment method, the result of which
    #: can be passed to CreatePaymentMethod to complete the setup
    #: process.
    token: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.token is not None:
            data["token"] = self.token

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CreatePaymentMethodIntentResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("token") is not None:
            kwargs["token"] = data["token"]

        return CreatePaymentMethodIntentResponse(**kwargs)
