# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import constants, util

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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.time is not None:
            data["time"] = util.encode_datetime(self.time)

        if self.type is not None:
            data["type"] = self.type

        if self.flows_changed is not None:
            data["flowsChanged"] = FlowsChanged.__json_encode__(self.flows_changed)

        if self.members_changed is not None:
            data["membersChanged"] = MembersChanged.__json_encode__(
                self.members_changed
            )

        if self.organizations_changed is not None:
            data["organizationsChanged"] = OrganizationsChanged.__json_encode__(
                self.organizations_changed
            )

        if self.subscriptions_changed is not None:
            data["subscriptionsChanged"] = SubscriptionsChanged.__json_encode__(
                self.subscriptions_changed
            )

        if self.users_changed is not None:
            data["usersChanged"] = UsersChanged.__json_encode__(self.users_changed)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Event":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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
