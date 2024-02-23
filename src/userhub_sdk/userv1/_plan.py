# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional

from userhub_sdk import commonv1

from ._plan_item import PlanItem


@dataclasses.dataclass
class Plan:
    """
    The plan.
    """

    #: The system-assigned identifier of the plan.
    id: str = ""
    #: The name of the plan.
    display_name: str = ""
    #: The description of the plan.
    description: Optional[str] = None
    #: The currency code for the plan (e.g. `USD`).
    currency_code: str = ""
    #: The billing interval for the plan.
    billing_interval: commonv1.Interval = dataclasses.field(
        default_factory=commonv1.Interval
    )
    #: The items associated with plan.
    items: Optional[List[PlanItem]] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.description is not None:
            data["description"] = self.description

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.billing_interval is not None:
            data["billingInterval"] = commonv1.Interval.__json_encode__(
                self.billing_interval
            )

        if self.items is not None:
            data["items"] = [PlanItem.__json_encode__(v) for v in self.items]

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Plan":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("billingInterval") is not None:
            kwargs["billing_interval"] = commonv1.Interval.__json_decode__(
                data["billingInterval"]
            )

        if data.get("items") is not None:
            kwargs["items"] = [PlanItem.__json_decode__(v) for v in data["items"]]

        return Plan(**kwargs)
