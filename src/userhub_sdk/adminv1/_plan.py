# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional

from userhub_sdk import commonv1

from ._plan_item import PlanItem
from ._plan_revision import PlanRevision
from ._plan_trial import PlanTrial


@dataclasses.dataclass
class Plan:
    """
    The plan.
    """

    #: The system-assigned identifier of the plan.
    id: str = ""
    #: The status of the plan.
    state: str = ""
    #: The client defined unique identifier of the plan.
    unique_id: Optional[str] = None
    #: The name of the plan.
    display_name: str = ""
    #: The description of the plan.
    description: Optional[str] = None
    #: The tier for the plan.
    #:
    #: This is only available in checkout and pricing.
    tier: Optional[str] = None
    #: The currency code for the plan (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The billing interval for the plan.
    interval: Optional[commonv1.Interval] = None
    #: The revision for the plan.
    revision: Optional[PlanRevision] = None
    #: Whether this is the current plan for the subscription.
    #:
    #: This is only set in checkout.
    current: Optional[bool] = None
    #: Whether this is the selected plan.
    #:
    #: This is only set in checkout.
    selected: Optional[bool] = None
    #: Whether this is the default term for the plan.
    default: Optional[bool] = None
    #: The trial settings.
    #:
    #: For authenticated requests, this will only be set for accounts that
    #: are eligible for a new trial.
    trial: Optional[PlanTrial] = None
    #: Whether the change is considered an upgrade or
    #: a downgrade.
    #:
    #: This is only set in checkout.
    change_path: Optional[str] = None
    #: The tags associated with the revision.
    tags: List[str] = dataclasses.field(default_factory=list)
    #: The items associated with plan.
    items: Optional[List[PlanItem]] = dataclasses.field(default_factory=list)
    #: The subscription view.
    view: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.state is not None:
            data["state"] = self.state

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.description is not None:
            data["description"] = self.description

        if self.tier is not None:
            data["tier"] = self.tier

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.interval is not None:
            data["interval"] = commonv1.Interval.__json_encode__(self.interval)

        if self.revision is not None:
            data["revision"] = PlanRevision.__json_encode__(self.revision)

        if self.current is not None:
            data["current"] = self.current

        if self.selected is not None:
            data["selected"] = self.selected

        if self.default is not None:
            data["default"] = self.default

        if self.trial is not None:
            data["trial"] = PlanTrial.__json_encode__(self.trial)

        if self.change_path is not None:
            data["changePath"] = self.change_path

        if self.tags is not None:
            data["tags"] = self.tags

        if self.items is not None:
            data["items"] = [PlanItem.__json_encode__(v) for v in self.items]

        if self.view is not None:
            data["view"] = self.view

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Plan":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("tier") is not None:
            kwargs["tier"] = data["tier"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("interval") is not None:
            kwargs["interval"] = commonv1.Interval.__json_decode__(data["interval"])

        if data.get("revision") is not None:
            kwargs["revision"] = PlanRevision.__json_decode__(data["revision"])

        if data.get("current") is not None:
            kwargs["current"] = data["current"]

        if data.get("selected") is not None:
            kwargs["selected"] = data["selected"]

        if data.get("default") is not None:
            kwargs["default"] = data["default"]

        if data.get("trial") is not None:
            kwargs["trial"] = PlanTrial.__json_decode__(data["trial"])

        if data.get("changePath") is not None:
            kwargs["change_path"] = data["changePath"]

        if data.get("tags") is not None:
            kwargs["tags"] = data["tags"]

        if data.get("items") is not None:
            kwargs["items"] = [PlanItem.__json_decode__(v) for v in data["items"]]

        if data.get("view") is not None:
            kwargs["view"] = data["view"]

        return Plan(**kwargs)
