# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import adminv1
from .._internal import util


@dataclasses.dataclass
class SubscriptionsChanged:
    """
    The subscriptions changed event.
    """

    #: The subscription.
    subscription: Optional[adminv1.Subscription] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("subscription") is not None:
            kwargs["subscription"] = adminv1.Subscription.__json_decode__(
                data["subscription"]
            )

        return SubscriptionsChanged(**kwargs)
