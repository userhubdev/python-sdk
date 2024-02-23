# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class CardPaymentMethodExpiration:
    """
    The expiration date for the card.
    """

    #: The expiration year.
    year: int = 0
    #: The expiration month.
    month: int = 0

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.year is not None:
            data["year"] = self.year

        if self.month is not None:
            data["month"] = self.month

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CardPaymentMethodExpiration":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("year") is not None:
            kwargs["year"] = data["year"]

        if data.get("month") is not None:
            kwargs["month"] = data["month"]

        return CardPaymentMethodExpiration(**kwargs)
