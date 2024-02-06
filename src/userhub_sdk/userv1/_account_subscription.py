# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import util
from ._account_subscription_plan import AccountSubscriptionPlan
from ._account_subscription_seat import AccountSubscriptionSeat


@dataclasses.dataclass
class AccountSubscription:
    """
    The account view of the subscription.
    """

    #: The system-assigned identifier of the subscription.
    id: Optional[str] = None
    #: The state of the subscription.
    state: Optional[str] = None
    #: The anchor time of the billing cycle.
    anchor_time: Optional[datetime.datetime] = None
    #: The subscription plan.
    plan: Optional[AccountSubscriptionPlan] = None
    #: The user's seat.
    #:
    #: This will only be set for organization subscriptions where
    #: the user has been assigned a seat.
    seat: Optional[AccountSubscriptionSeat] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("anchorTime") is not None:
            kwargs["anchor_time"] = util.decode_datetime(data["anchorTime"])

        if data.get("plan") is not None:
            kwargs["plan"] = AccountSubscriptionPlan.__json_decode__(data["plan"])

        if data.get("seat") is not None:
            kwargs["seat"] = AccountSubscriptionSeat.__json_decode__(data["seat"])

        return AccountSubscription(**kwargs)
