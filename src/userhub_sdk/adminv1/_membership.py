# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import constants
from .._internal import util
from ._account_subscription_seat import AccountSubscriptionSeat
from ._organization import Organization
from ._role import Role


@dataclasses.dataclass
class Membership:
    """
    A user's membership in an organization.

    This is the user view, see Member for the organizational
    view.
    """

    #: The organization.
    organization: Optional[Organization] = None
    #: The user's role within the organization.
    role: Optional[Role] = None
    #: The seat associated with the membership.
    #:
    #: This will be absent if there is no active default
    #: subscription for the organization or the user
    #: has not been assigned a seat.
    seat: Optional[AccountSubscriptionSeat] = None
    #: The creation time of the membership.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the membership.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("organization") is not None:
            kwargs["organization"] = Organization.__json_decode__(data["organization"])

        if data.get("role") is not None:
            kwargs["role"] = Role.__json_decode__(data["role"])

        if data.get("seat") is not None:
            kwargs["seat"] = AccountSubscriptionSeat.__json_decode__(data["seat"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Membership(**kwargs)
