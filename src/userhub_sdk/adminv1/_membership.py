# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import constants, util

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
    organization: Organization = dataclasses.field(default_factory=Organization)
    #: The user's role within the organization.
    role: Role = dataclasses.field(default_factory=Role)
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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.organization is not None:
            data["organization"] = Organization.__json_encode__(self.organization)

        if self.role is not None:
            data["role"] = Role.__json_encode__(self.role)

        if self.seat is not None:
            data["seat"] = AccountSubscriptionSeat.__json_encode__(self.seat)

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Membership":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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
