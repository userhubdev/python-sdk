# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import List
from typing import Optional

from .._internal import constants
from .._internal import util
from ._connection import Connection
from ._organization import Organization
from ._payment_method import PaymentMethod
from ._plan import Plan
from ._subscription_current_period import SubscriptionCurrentPeriod
from ._subscription_item import SubscriptionItem
from ._subscription_seat_info import SubscriptionSeatInfo
from ._subscription_trial import SubscriptionTrial
from ._user import User


@dataclasses.dataclass
class Subscription:
    """
    The representation of an activated plan.
    """

    #: The system-assigned identifier of the subscription.
    id: str = ""
    #: The status of the subscription.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The billing connection.
    connection: Optional[Connection] = None
    #: The external identifier of the subscription.
    external_id: Optional[str] = None
    #: The plan.
    plan: Optional[Plan] = None
    #: The currency code for the subscription (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The subscription items.
    items: Optional[List[SubscriptionItem]] = dataclasses.field(default_factory=list)
    #: The seat information.
    seats: Optional[List[SubscriptionSeatInfo]] = dataclasses.field(
        default_factory=list
    )
    #: The payment method.
    payment_method: Optional[PaymentMethod] = None
    #: Whether the subscription is scheduled to be canceled
    #: at the end of the current billing period.
    cancel_period_end: Optional[bool] = None
    #: The anchor time for the billing cycle.
    anchor_time: Optional[datetime.datetime] = None
    #: The time the subscription started.
    start_time: Optional[datetime.datetime] = None
    #: The time the subscription ends/ended.
    end_time: Optional[datetime.datetime] = None
    #: The trial information for the subscription.
    trial: Optional[SubscriptionTrial] = None
    #: The current billing period for the subscription.
    current_period: Optional[SubscriptionCurrentPeriod] = None
    #: The organization owner of the subscription.
    #:
    #: The ID field of this object must be populated if
    #: if user isn't specified.
    organization: Optional[Organization] = None
    #: The user owner of the subscription.
    #:
    #: The ID field of this object must be populated if
    #: if organization isn't specified.
    user: Optional[User] = None
    #: Whether the subscription is the default for the account.
    default: Optional[bool] = None
    #: The last time the subscription was pulled from the connection.
    pull_time: Optional[datetime.datetime] = None
    #: The last time the subscription was pushed to the connection.
    push_time: Optional[datetime.datetime] = None
    #: The creation time of the subscription.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the subscription.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

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

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

        if data.get("connection") is not None:
            kwargs["connection"] = Connection.__json_decode__(data["connection"])

        if data.get("externalId") is not None:
            kwargs["external_id"] = data["externalId"]

        if data.get("plan") is not None:
            kwargs["plan"] = Plan.__json_decode__(data["plan"])

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("items") is not None:
            kwargs["items"] = [
                SubscriptionItem.__json_decode__(v) for v in data["items"]
            ]

        if data.get("seats") is not None:
            kwargs["seats"] = [
                SubscriptionSeatInfo.__json_decode__(v) for v in data["seats"]
            ]

        if data.get("paymentMethod") is not None:
            kwargs["payment_method"] = PaymentMethod.__json_decode__(
                data["paymentMethod"]
            )

        if data.get("cancelPeriodEnd") is not None:
            kwargs["cancel_period_end"] = data["cancelPeriodEnd"]

        if data.get("anchorTime") is not None:
            kwargs["anchor_time"] = util.decode_datetime(data["anchorTime"])

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

        if data.get("organization") is not None:
            kwargs["organization"] = Organization.__json_decode__(data["organization"])

        if data.get("user") is not None:
            kwargs["user"] = User.__json_decode__(data["user"])

        if data.get("default") is not None:
            kwargs["default"] = data["default"]

        if data.get("pullTime") is not None:
            kwargs["pull_time"] = util.decode_datetime(data["pullTime"])

        if data.get("pushTime") is not None:
            kwargs["push_time"] = util.decode_datetime(data["pushTime"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Subscription(**kwargs)
