# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._product import Product


@dataclasses.dataclass
class SubscriptionSeatInfo:
    """
    The subscription seat.
    """

    #: The subscription item product.
    product: Optional[Product] = None
    #: The quantity which has been invoiced for the current billing period.
    #:
    #: This might be less than the total quantity while a subscription change
    #: is pending or if the subscription is over-provisioned.
    current_period_quantity: Optional[int] = None
    #: The quantity scheduled to appear on the next invoice.
    #:
    #: This will only be set when different from current period quantity.
    next_period_quantity: Optional[int] = None
    #: The quantity currently in use.
    assigned_quantity: Optional[int] = None
    #: The quantity not in use.
    unassigned_quantity: Optional[int] = None
    #: The sum of the assigned and unassigned quantities.
    total_quantity: Optional[int] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

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

        if data.get("totalQuantity") is not None:
            kwargs["total_quantity"] = data["totalQuantity"]

        return SubscriptionSeatInfo(**kwargs)
