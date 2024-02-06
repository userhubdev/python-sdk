# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._account_subscription_product import AccountSubscriptionProduct


@dataclasses.dataclass
class AccountSubscriptionSeat:
    """
    The user's seat information.
    """

    #: The seat product.
    product: Optional[AccountSubscriptionProduct] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("product") is not None:
            kwargs["product"] = AccountSubscriptionProduct.__json_decode__(
                data["product"]
            )

        return AccountSubscriptionSeat(**kwargs)
