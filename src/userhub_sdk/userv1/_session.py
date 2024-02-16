# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import util

from ._account_subscription import AccountSubscription
from ._membership import Membership
from ._user import User


@dataclasses.dataclass
class Session:
    """
    The session details.
    """

    #: The authenticated user.
    #:
    #: This will be null if the user is not authenticated.
    user: Optional[User] = None
    #: The authenticated user's organization memberships.
    memberships: Optional[List[Membership]] = dataclasses.field(default_factory=list)
    #: The user's default active individual subscription.
    #:
    #: See memberships for organization subscription and
    #: seat information.
    subscription: Optional[AccountSubscription] = None
    #: The expiration time for the current session.
    expire_time: Optional[datetime.datetime] = None
    #: The scopes available in the current session.
    scopes: List[str] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.user is not None:
            data["user"] = User.__json_encode__(self.user)

        if self.memberships is not None:
            data["memberships"] = [
                Membership.__json_encode__(v) for v in self.memberships
            ]

        if self.subscription is not None:
            data["subscription"] = AccountSubscription.__json_encode__(
                self.subscription
            )

        if self.expire_time is not None:
            data["expireTime"] = util.encode_datetime(self.expire_time)

        if self.scopes is not None:
            data["scopes"] = self.scopes

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Session":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("user") is not None:
            kwargs["user"] = User.__json_decode__(data["user"])

        if data.get("memberships") is not None:
            kwargs["memberships"] = [
                Membership.__json_decode__(v) for v in data["memberships"]
            ]

        if data.get("subscription") is not None:
            kwargs["subscription"] = AccountSubscription.__json_decode__(
                data["subscription"]
            )

        if data.get("expireTime") is not None:
            kwargs["expire_time"] = util.decode_datetime(data["expireTime"])

        if data.get("scopes") is not None:
            kwargs["scopes"] = data["scopes"]

        return Session(**kwargs)
