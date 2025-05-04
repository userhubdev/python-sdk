# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class CheckoutInput:
    """
    Checkout input parameters.
    """

    #: The identifier of the organization.
    #:
    #: This is required if the user identifier is not specified.
    organization_id: str = ""
    #: The identifier of the user.
    #:
    #: This is required if the organization identifier is not specified.
    user_id: str = ""
    #: The type of the checkout.
    type: str = ""
    #: The identifier of the plan.
    #:
    #: This allows you to specify the currently selected plan.
    plan_id: str = ""
    #: The identifier of the subscriptions.
    #:
    #: This allows you to specify a non-default subscription.
    subscription_id: str = ""
    #: The identifier of the connection.
    #:
    #: This allows you to specify a non-default billing connection.
    connection_id: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.organization_id is not None:
            data["organizationId"] = self.organization_id

        if self.user_id is not None:
            data["userId"] = self.user_id

        if self.type is not None:
            data["type"] = self.type

        if self.plan_id is not None:
            data["planId"] = self.plan_id

        if self.subscription_id is not None:
            data["subscriptionId"] = self.subscription_id

        if self.connection_id is not None:
            data["connectionId"] = self.connection_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("organizationId") is not None:
            kwargs["organization_id"] = data["organizationId"]

        if data.get("userId") is not None:
            kwargs["user_id"] = data["userId"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("planId") is not None:
            kwargs["plan_id"] = data["planId"]

        if data.get("subscriptionId") is not None:
            kwargs["subscription_id"] = data["subscriptionId"]

        if data.get("connectionId") is not None:
            kwargs["connection_id"] = data["connectionId"]

        return CheckoutInput(**kwargs)
