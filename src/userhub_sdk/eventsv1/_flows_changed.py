# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import adminv1


@dataclasses.dataclass
class FlowsChanged:
    """
    The flows changed event.
    """

    #: The flow.
    flow: Optional[adminv1.Flow] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.flow is not None:
            data["flow"] = adminv1.Flow.__json_encode__(self.flow)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "FlowsChanged":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("flow") is not None:
            kwargs["flow"] = adminv1.Flow.__json_decode__(data["flow"])

        return FlowsChanged(**kwargs)
