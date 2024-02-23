# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import util


@dataclasses.dataclass
class InvoiceChange:
    """
    A prorated change that occurred mid-billing cycle.
    """

    #: The time the change occurred.
    time: Optional[datetime.datetime] = None
    #: The user-facing description for the change.
    description: str = ""
    #: The total amount for the change excluding
    #: taxes and discounts.
    subtotal_amount: str = ""
    #: The change discount amount.
    discount_amount: Optional[str] = None
    #: The starting quantity of the change.
    start_quantity: int = 0
    #: The ending quantity of the change.
    end_quantity: int = 0
    #: The starting (credited) item identifiers.
    start_item_ids: List[str] = dataclasses.field(default_factory=list)
    #: The ending (charged) item identifiers.
    end_item_ids: List[str] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.time is not None:
            data["time"] = util.encode_datetime(self.time)

        if self.description is not None:
            data["description"] = self.description

        if self.subtotal_amount is not None:
            data["subtotalAmount"] = self.subtotal_amount

        if self.discount_amount is not None:
            data["discountAmount"] = self.discount_amount

        if self.start_quantity is not None:
            data["startQuantity"] = self.start_quantity

        if self.end_quantity is not None:
            data["endQuantity"] = self.end_quantity

        if self.start_item_ids is not None:
            data["startItemIds"] = self.start_item_ids

        if self.end_item_ids is not None:
            data["endItemIds"] = self.end_item_ids

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "InvoiceChange":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("time") is not None:
            kwargs["time"] = util.decode_datetime(data["time"])

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("subtotalAmount") is not None:
            kwargs["subtotal_amount"] = data["subtotalAmount"]

        if data.get("discountAmount") is not None:
            kwargs["discount_amount"] = data["discountAmount"]

        if data.get("startQuantity") is not None:
            kwargs["start_quantity"] = data["startQuantity"]

        if data.get("endQuantity") is not None:
            kwargs["end_quantity"] = data["endQuantity"]

        if data.get("startItemIds") is not None:
            kwargs["start_item_ids"] = data["startItemIds"]

        if data.get("endItemIds") is not None:
            kwargs["end_item_ids"] = data["endItemIds"]

        return InvoiceChange(**kwargs)
