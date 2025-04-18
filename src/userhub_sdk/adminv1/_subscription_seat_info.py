# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._product import Product


@dataclasses.dataclass
class SubscriptionSeatInfo:
    """
    The subscription seat.
    """

    #: Whether a seat can be assigned or reserved.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The seat product.
    product: Optional[Product] = None
    #: The number of seats expected to be invoiced for the current billing period.
    #:
    #: This might be less than the total quantity while a subscription change
    #: is pending or if the subscription is over-provisioned.
    current_period_quantity: int = 0
    #: The number of seats scheduled to appear on the next invoice.
    #:
    #: This will only be set when different from current period quantity.
    next_period_quantity: Optional[int] = None
    #: The number of seats currently assigned.
    assigned_quantity: int = 0
    #: The number of seats not assigned.
    unassigned_quantity: int = 0
    #: The number of seats currently reserved because of pending invitations.
    #:
    #: These can be made available by cancelling outstanding invitations.
    reserved_quantity: Optional[int] = None
    #: The number of seats which can be assigned or reserved.
    available_quantity: Optional[int] = None
    #: The total number of seats for the current period.
    total_quantity: int = 0

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

        if self.product is not None:
            data["product"] = Product.__json_encode__(self.product)

        if self.current_period_quantity is not None:
            data["currentPeriodQuantity"] = self.current_period_quantity

        if self.next_period_quantity is not None:
            data["nextPeriodQuantity"] = self.next_period_quantity

        if self.assigned_quantity is not None:
            data["assignedQuantity"] = self.assigned_quantity

        if self.unassigned_quantity is not None:
            data["unassignedQuantity"] = self.unassigned_quantity

        if self.reserved_quantity is not None:
            data["reservedQuantity"] = self.reserved_quantity

        if self.available_quantity is not None:
            data["availableQuantity"] = self.available_quantity

        if self.total_quantity is not None:
            data["totalQuantity"] = self.total_quantity

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "SubscriptionSeatInfo":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        if data.get("currentPeriodQuantity") is not None:
            kwargs["current_period_quantity"] = data["currentPeriodQuantity"]

        if data.get("nextPeriodQuantity") is not None:
            kwargs["next_period_quantity"] = data["nextPeriodQuantity"]

        if data.get("assignedQuantity") is not None:
            kwargs["assigned_quantity"] = data["assignedQuantity"]

        if data.get("unassignedQuantity") is not None:
            kwargs["unassigned_quantity"] = data["unassignedQuantity"]

        if data.get("reservedQuantity") is not None:
            kwargs["reserved_quantity"] = data["reservedQuantity"]

        if data.get("availableQuantity") is not None:
            kwargs["available_quantity"] = data["availableQuantity"]

        if data.get("totalQuantity") is not None:
            kwargs["total_quantity"] = data["totalQuantity"]

        return SubscriptionSeatInfo(**kwargs)
