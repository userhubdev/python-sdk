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
    #: This must be provided for organization checkouts.
    organization_id: str = ""
    #: The type of the checkout.
    type: str = ""
    #: The identifier of the plan.
    #:
    #: This allows you to specify the currently selected plan.
    plan_id: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.organization_id is not None:
            data["organizationId"] = self.organization_id

        if self.type is not None:
            data["type"] = self.type

        if self.plan_id is not None:
            data["planId"] = self.plan_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("organizationId") is not None:
            kwargs["organization_id"] = data["organizationId"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("planId") is not None:
            kwargs["plan_id"] = data["planId"]

        return CheckoutInput(**kwargs)
