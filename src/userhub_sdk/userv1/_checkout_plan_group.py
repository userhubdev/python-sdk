# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class CheckoutPlanGroup:
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
    #: Whether this is the current plan group for the subscription.
    current: Optional[bool] = None
    #: Whether this is the selected plan group for the checkout.
    selected: Optional[bool] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.current is not None:
            data["current"] = self.current

        if self.selected is not None:
            data["selected"] = self.selected

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutPlanGroup":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("current") is not None:
            kwargs["current"] = data["current"]

        if data.get("selected") is not None:
            kwargs["selected"] = data["selected"]

        return CheckoutPlanGroup(**kwargs)
