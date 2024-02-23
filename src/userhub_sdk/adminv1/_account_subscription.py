# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import util

from ._account_subscription_plan import AccountSubscriptionPlan


@dataclasses.dataclass
class AccountSubscription:
    """
    The account view of the subscription.
    """

    #: The system-assigned identifier of the subscription.
    id: str = ""
    #: The state of the subscription.
    state: str = ""
    #: The anchor time of the billing cycle.
    anchor_time: Optional[datetime.datetime] = None
    #: The plan.
    plan: Optional[AccountSubscriptionPlan] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.state is not None:
            data["state"] = self.state

        if self.anchor_time is not None:
            data["anchorTime"] = util.encode_datetime(self.anchor_time)

        if self.plan is not None:
            data["plan"] = AccountSubscriptionPlan.__json_encode__(self.plan)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "AccountSubscription":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("anchorTime") is not None:
            kwargs["anchor_time"] = util.decode_datetime(data["anchorTime"])

        if data.get("plan") is not None:
            kwargs["plan"] = AccountSubscriptionPlan.__json_decode__(data["plan"])

        return AccountSubscription(**kwargs)
