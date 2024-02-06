# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .. import commonv1
from .._internal import util
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
    currency_code: Optional[str] = None
    #: The billing interval for the plan.
    billing_interval: Optional[commonv1.Interval] = None
    #: The items associated with plan.
    items: Optional[List[PlanItem]] = dataclasses.field(default_factory=list)

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

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
