# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class BillingAccountCheckout:
    """
    The discount.
    """

    #: The type of checkout.
    type: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.type is not None:
            data["type"] = self.type

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "BillingAccountCheckout":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        return BillingAccountCheckout(**kwargs)
