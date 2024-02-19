# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import constants, util

from ._payment_method import PaymentMethod
from ._plan import Plan
from ._subscription_current_period import SubscriptionCurrentPeriod
from ._subscription_item import SubscriptionItem
from ._subscription_seat_info import SubscriptionSeatInfo
from ._subscription_trial import SubscriptionTrial


@dataclasses.dataclass
class Subscription:
    """
    The user's or organization's subscription.
    """

    #: The system-assigned identifier of the subscription.
    id: str = ""
    #: The status of the subscription.
    state: str = ""
    #: The currency code for the subscription (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The subscription items.
    plan: Optional[Plan] = None
    #: The payment method.
    payment_method: Optional[PaymentMethod] = None
    #: The subscription is scheduled to be canceled at the end of the
    #: current billing period.
    cancel_period_end: Optional[bool] = None
    #: The time the subscription started.
    start_time: Optional[datetime.datetime] = None
    #: The time the subscription ends/ended.
    end_time: Optional[datetime.datetime] = None
    #: The trial information for the subscription.
    trial: Optional[SubscriptionTrial] = None
    #: The current billing period for the subscription.
    current_period: Optional[SubscriptionCurrentPeriod] = None
    #: The subscription items.
    items: Optional[List[SubscriptionItem]] = dataclasses.field(default_factory=list)
    #: The information about the various seats available in
    #: the subscription.
    seats: Optional[List[SubscriptionSeatInfo]] = dataclasses.field(
        default_factory=list
    )
    #: The creation time of the subscription.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the subscription.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.state is not None:
            data["state"] = self.state

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.plan is not None:
            data["plan"] = Plan.__json_encode__(self.plan)

        if self.payment_method is not None:
            data["paymentMethod"] = PaymentMethod.__json_encode__(self.payment_method)

        if self.cancel_period_end is not None:
            data["cancelPeriodEnd"] = self.cancel_period_end

        if self.start_time is not None:
            data["startTime"] = util.encode_datetime(self.start_time)

        if self.end_time is not None:
            data["endTime"] = util.encode_datetime(self.end_time)

        if self.trial is not None:
            data["trial"] = SubscriptionTrial.__json_encode__(self.trial)

        if self.current_period is not None:
            data["currentPeriod"] = SubscriptionCurrentPeriod.__json_encode__(
                self.current_period
            )

        if self.items is not None:
            data["items"] = [SubscriptionItem.__json_encode__(v) for v in self.items]

        if self.seats is not None:
            data["seats"] = [
                SubscriptionSeatInfo.__json_encode__(v) for v in self.seats
            ]

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Subscription":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("plan") is not None:
            kwargs["plan"] = Plan.__json_decode__(data["plan"])

        if data.get("paymentMethod") is not None:
            kwargs["payment_method"] = PaymentMethod.__json_decode__(
                data["paymentMethod"]
            )

        if data.get("cancelPeriodEnd") is not None:
            kwargs["cancel_period_end"] = data["cancelPeriodEnd"]

        if data.get("startTime") is not None:
            kwargs["start_time"] = util.decode_datetime(data["startTime"])

        if data.get("endTime") is not None:
            kwargs["end_time"] = util.decode_datetime(data["endTime"])

        if data.get("trial") is not None:
            kwargs["trial"] = SubscriptionTrial.__json_decode__(data["trial"])

        if data.get("currentPeriod") is not None:
            kwargs["current_period"] = SubscriptionCurrentPeriod.__json_decode__(
                data["currentPeriod"]
            )

        if data.get("items") is not None:
            kwargs["items"] = [
                SubscriptionItem.__json_decode__(v) for v in data["items"]
            ]

        if data.get("seats") is not None:
            kwargs["seats"] = [
                SubscriptionSeatInfo.__json_decode__(v) for v in data["seats"]
            ]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Subscription(**kwargs)
