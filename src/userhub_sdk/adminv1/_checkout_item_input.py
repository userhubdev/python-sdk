# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class CheckoutItemInput:
    """
    Checkout item input.
    """

    #: The identifier of the item.
    id: str = ""
    #: The quantity for the item.
    quantity: Optional[int] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.quantity is not None:
            data["quantity"] = self.quantity

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutItemInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        return CheckoutItemInput(**kwargs)
