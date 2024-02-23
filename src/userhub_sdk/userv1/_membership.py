# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

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
    organization: Organization = dataclasses.field(default_factory=Organization)
    #: The user's role within the organization.
    role: Role = dataclasses.field(default_factory=Role)
    #: The subscription associated with the organization.
    subscription: Optional[AccountSubscription] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.organization is not None:
            data["organization"] = Organization.__json_encode__(self.organization)

        if self.role is not None:
            data["role"] = Role.__json_encode__(self.role)

        if self.subscription is not None:
            data["subscription"] = AccountSubscription.__json_encode__(
                self.subscription
            )

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

        if data.get("subscription") is not None:
            kwargs["subscription"] = AccountSubscription.__json_decode__(
                data["subscription"]
            )

        return Membership(**kwargs)
