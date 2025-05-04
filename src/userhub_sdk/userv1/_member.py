# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._account_subscription_seat import AccountSubscriptionSeat
from ._role import Role
from ._user import User


@dataclasses.dataclass
class Member:
    """
    A member of an organization.
    """

    #: The user.
    user: User = dataclasses.field(default_factory=User)
    #: The user's role within the organization.
    role: Role = dataclasses.field(default_factory=Role)
    #: The seat assigned to the member.
    #:
    #: This will be absent if there is no active
    #: subscription for the organization or the user
    #: has not been assigned a seat.
    seat: Optional[AccountSubscriptionSeat] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.user is not None:
            data["user"] = User.__json_encode__(self.user)

        if self.role is not None:
            data["role"] = Role.__json_encode__(self.role)

        if self.seat is not None:
            data["seat"] = AccountSubscriptionSeat.__json_encode__(self.seat)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Member":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("user") is not None:
            kwargs["user"] = User.__json_decode__(data["user"])

        if data.get("role") is not None:
            kwargs["role"] = Role.__json_decode__(data["role"])

        if data.get("seat") is not None:
            kwargs["seat"] = AccountSubscriptionSeat.__json_decode__(data["seat"])

        return Member(**kwargs)
