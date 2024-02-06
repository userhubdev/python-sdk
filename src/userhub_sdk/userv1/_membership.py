# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._account_subscription import AccountSubscription
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
    #: The subscription associated with the organization.
    subscription: Optional[AccountSubscription] = None

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

        if data.get("subscription") is not None:
            kwargs["subscription"] = AccountSubscription.__json_decode__(
                data["subscription"]
            )

        return Membership(**kwargs)
