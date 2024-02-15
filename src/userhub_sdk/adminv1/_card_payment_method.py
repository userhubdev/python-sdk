# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from ._card_payment_method_expiration import CardPaymentMethodExpiration


@dataclasses.dataclass
class CardPaymentMethod:
    """
    A card payment method (e.g. credit, debit, etc...).
    """

    #: The brand of the card (e.g. `VISA`).
    brand: Optional[str] = None
    #: The expiration date of the card.
    expiration: Optional[CardPaymentMethodExpiration] = None
    #: The last for digits of the card.
    last4: Optional[str] = None
    #: The funding method for the card (e.g. `DEBIT`)
    funding_type: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.brand is not None:
            data["brand"] = self.brand

        if self.expiration is not None:
            data["expiration"] = CardPaymentMethodExpiration.__json_encode__(
                self.expiration
            )

        if self.last4 is not None:
            data["last4"] = self.last4

        if self.funding_type is not None:
            data["fundingType"] = self.funding_type

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("brand") is not None:
            kwargs["brand"] = data["brand"]

        if data.get("expiration") is not None:
            kwargs["expiration"] = CardPaymentMethodExpiration.__json_decode__(
                data["expiration"]
            )

        if data.get("last4") is not None:
            kwargs["last4"] = data["last4"]

        if data.get("fundingType") is not None:
            kwargs["funding_type"] = data["fundingType"]

        return CardPaymentMethod(**kwargs)
