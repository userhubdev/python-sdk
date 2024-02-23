# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional

from ._plan import Plan
from ._plan_group_change_path import PlanGroupChangePath
from ._plan_group_trial import PlanGroupTrial


@dataclasses.dataclass
class PlanGroup:
    """
    Plan group is a collection of related plans.

    A plan group will generally describe a tier of plans offered
    (e.g. Basic vs Pro) which might contain multiple billing options
    (e.g. monthly vs yearly, USD vs EUR).
    """

    #: The system-assigned identifier of the plan group.
    id: str = ""
    #: The client defined unique identifier of the plan group (e.g. `pro`).
    unique_id: Optional[str] = None
    #: The name of the plan group.
    display_name: str = ""
    #: The user facing description of the plan group.
    description: Optional[str] = None
    #: Whether the plans are for organizations or users.
    account_type: str = ""
    #: The trial settings.
    #:
    #: For authenticated requests, this will not be set when the account
    #: isn't eligible for a trial.
    trial: Optional[PlanGroupTrial] = None
    #: Whether the plan is considered an downgrade or upgrade.
    change_path: Optional[PlanGroupChangePath] = None
    #: The plans associated with plan group.
    plans: Optional[List[Plan]] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.description is not None:
            data["description"] = self.description

        if self.account_type is not None:
            data["accountType"] = self.account_type

        if self.trial is not None:
            data["trial"] = PlanGroupTrial.__json_encode__(self.trial)

        if self.change_path is not None:
            data["changePath"] = PlanGroupChangePath.__json_encode__(self.change_path)

        if self.plans is not None:
            data["plans"] = [Plan.__json_encode__(v) for v in self.plans]

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanGroup":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("accountType") is not None:
            kwargs["account_type"] = data["accountType"]

        if data.get("trial") is not None:
            kwargs["trial"] = PlanGroupTrial.__json_decode__(data["trial"])

        if data.get("changePath") is not None:
            kwargs["change_path"] = PlanGroupChangePath.__json_decode__(
                data["changePath"]
            )

        if data.get("plans") is not None:
            kwargs["plans"] = [Plan.__json_decode__(v) for v in data["plans"]]

        return PlanGroup(**kwargs)
