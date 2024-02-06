# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import constants
from .._internal import util
from ._flows_changed import FlowsChanged
from ._members_changed import MembersChanged
from ._organizations_changed import OrganizationsChanged
from ._subscriptions_changed import SubscriptionsChanged
from ._users_changed import UsersChanged


@dataclasses.dataclass
class Event:
    """
    The event.
    """

    #: The event identifier
    id: str = ""
    #: The event time.
    time: datetime.datetime = constants.EMPTY_DATETIME
    #: The event type.
    type: str = ""
    #: The `flows.changed` data.
    flows_changed: Optional[FlowsChanged] = None
    #: The `members.changed` data.
    members_changed: Optional[MembersChanged] = None
    #: The `organizations.changed` data.
    organizations_changed: Optional[OrganizationsChanged] = None
    #: The `subscriptions.changed` data.
    subscriptions_changed: Optional[SubscriptionsChanged] = None
    #: The `users.changed` data.
    users_changed: Optional[UsersChanged] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("time") is not None:
            kwargs["time"] = util.decode_datetime(data["time"])

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("flowsChanged") is not None:
            kwargs["flows_changed"] = FlowsChanged.__json_decode__(data["flowsChanged"])

        if data.get("membersChanged") is not None:
            kwargs["members_changed"] = MembersChanged.__json_decode__(
                data["membersChanged"]
            )

        if data.get("organizationsChanged") is not None:
            kwargs["organizations_changed"] = OrganizationsChanged.__json_decode__(
                data["organizationsChanged"]
            )

        if data.get("subscriptionsChanged") is not None:
            kwargs["subscriptions_changed"] = SubscriptionsChanged.__json_decode__(
                data["subscriptionsChanged"]
            )

        if data.get("usersChanged") is not None:
            kwargs["users_changed"] = UsersChanged.__json_decode__(data["usersChanged"])

        return Event(**kwargs)
