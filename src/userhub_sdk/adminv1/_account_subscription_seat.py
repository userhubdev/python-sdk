# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._account_subscription_product import AccountSubscriptionProduct


@dataclasses.dataclass
class AccountSubscriptionSeat:
    """
    The user's seat information.
    """

    #: The seat product.
    product: Optional[AccountSubscriptionProduct] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.product is not None:
            data["product"] = AccountSubscriptionProduct.__json_encode__(self.product)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "AccountSubscriptionSeat":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("product") is not None:
            kwargs["product"] = AccountSubscriptionProduct.__json_decode__(
                data["product"]
            )

        return AccountSubscriptionSeat(**kwargs)
