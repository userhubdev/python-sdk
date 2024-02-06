# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


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
        return dict(user.__dict__)

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
