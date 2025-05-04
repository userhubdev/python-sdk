# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List

from ._plan import Plan


@dataclasses.dataclass
class Pricing:
    """
    The plans available in checkout.
    """

    #: The list of plans.
    plans: List[Plan] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.plans is not None:
            data["plans"] = [Plan.__json_encode__(v) for v in self.plans]

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Pricing":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("plans") is not None:
            kwargs["plans"] = [Plan.__json_decode__(v) for v in data["plans"]]

        return Pricing(**kwargs)
