# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional


@dataclasses.dataclass
class CardPaymentMethodExpiration:
    """
    The expiration date for the card.
    """

    #: The expiration year.
    year: Optional[int] = None
    #: The expiration month.
    month: Optional[int] = None

    def __json_encode__(self):
        data = {}

        if self.year is not None:
            data["year"] = self.year

        if self.month is not None:
            data["month"] = self.month

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("year") is not None:
            kwargs["year"] = data["year"]

        if data.get("month") is not None:
            kwargs["month"] = data["month"]

        return CardPaymentMethodExpiration(**kwargs)
