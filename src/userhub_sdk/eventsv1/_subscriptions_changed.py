# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict

from userhub_sdk import adminv1


@dataclasses.dataclass
class SubscriptionsChanged:
    """
    The subscriptions changed event.
    """

    #: The subscription.
    subscription: adminv1.Subscription = dataclasses.field(
        default_factory=adminv1.Subscription
    )

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.subscription is not None:
            data["subscription"] = adminv1.Subscription.__json_encode__(
                self.subscription
            )

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "SubscriptionsChanged":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("subscription") is not None:
            kwargs["subscription"] = adminv1.Subscription.__json_decode__(
                data["subscription"]
            )

        return SubscriptionsChanged(**kwargs)
