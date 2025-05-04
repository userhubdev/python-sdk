# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class CheckoutTrialStep:
    """
    The trial step details.
    """

    #: Whether to start or continue a trial.
    type: str = ""
    #: The number of days in the trial.
    days: Optional[int] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.type is not None:
            data["type"] = self.type

        if self.days is not None:
            data["days"] = self.days

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutTrialStep":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("days") is not None:
            kwargs["days"] = data["days"]

        return CheckoutTrialStep(**kwargs)
