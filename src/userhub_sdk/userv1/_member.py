# Code generated. DO NOT EDIT.

import dataclasses
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

    #: The user.
    user: Optional[User] = None
    #: The user's role within the organization.
    role: Optional[Role] = None
    #: The seat assigned to the member.
    #:
    #: This will be absent if there is no active
    #: subscription for the organization or the user
    #: has not been assigned a seat.
    seat: Optional[AccountSubscriptionSeat] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("user") is not None:
            kwargs["user"] = User.__json_decode__(data["user"])

        if data.get("role") is not None:
            kwargs["role"] = Role.__json_decode__(data["role"])

        if data.get("seat") is not None:
            kwargs["seat"] = AccountSubscriptionSeat.__json_decode__(data["seat"])

        return Member(**kwargs)
