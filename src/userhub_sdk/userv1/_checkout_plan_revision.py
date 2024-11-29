# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class CheckoutPlanRevision:
    """
    Revision is a collection of plans with the same revision.

    This will group plans with different billing cycles.
    """

    #: The system-assigned identifier of the plan group revision.
    id: str = ""
    #: Whether this is the current revision for the subscription.
    current: Optional[bool] = None
    #: Whether this is the selected revision for the checkout.
    selected: Optional[bool] = None
    #: Whether this is the latest revision for the plan group.
    #:
    #: This will only be set for a current or selected plan group.
    latest: Optional[bool] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.current is not None:
            data["current"] = self.current

        if self.selected is not None:
            data["selected"] = self.selected

        if self.latest is not None:
            data["latest"] = self.latest

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutPlanRevision":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("current") is not None:
            kwargs["current"] = data["current"]

        if data.get("selected") is not None:
            kwargs["selected"] = data["selected"]

        if data.get("latest") is not None:
            kwargs["latest"] = data["latest"]

        return CheckoutPlanRevision(**kwargs)
