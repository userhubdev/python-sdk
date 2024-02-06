# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._account_subscription_product import AccountSubscriptionProduct


@dataclasses.dataclass
class AccountSubscriptionPlan:
    """
    The plan information.
    """

    #: The identifier of the plan.
    id: Optional[str] = None
    #: The human-readable display name of the plan.
    display_name: Optional[str] = None
    #: The plan product.
    product: Optional[AccountSubscriptionProduct] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("product") is not None:
            kwargs["product"] = AccountSubscriptionProduct.__json_decode__(
                data["product"]
            )

        return AccountSubscriptionPlan(**kwargs)
