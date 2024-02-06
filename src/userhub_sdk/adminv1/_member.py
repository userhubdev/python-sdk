# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import util
from ._account_subscription_seat import AccountSubscriptionSeat
from ._role import Role
from ._user import User


@dataclasses.dataclass
class Member:
    """
    A member of an organization.
    """

    #: Whether the membership is active.
    state: str = ""
    #: The user.
    user: Optional[User] = None
    #: The user's role within the organization.
    role: Optional[Role] = None
    #: The seat associated with the member.
    #:
    #: This will be absent if there is no active
    #: subscription for the organization or the user
    #: has not been assigned a seat.
    seat: Optional[AccountSubscriptionSeat] = None
    #: The creation time of the membership.
    create_time: Optional[datetime.datetime] = None
    #: The last update time of the membership.
    update_time: Optional[datetime.datetime] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("user") is not None:
            kwargs["user"] = User.__json_decode__(data["user"])

        if data.get("role") is not None:
            kwargs["role"] = Role.__json_decode__(data["role"])

        if data.get("seat") is not None:
            kwargs["seat"] = AccountSubscriptionSeat.__json_decode__(data["seat"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Member(**kwargs)
