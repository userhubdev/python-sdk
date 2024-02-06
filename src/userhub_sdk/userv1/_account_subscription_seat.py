# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._product import Product


@dataclasses.dataclass
class AccountSubscriptionSeat:
    """
    The user's seat information.
    """

    #: The seat product.
    product: Optional[Product] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        return AccountSubscriptionSeat(**kwargs)
