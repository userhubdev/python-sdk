# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import commonv1

from ._price import Price


@dataclasses.dataclass
class CheckoutItem:
    """
    The checkout item.
    """

    #: The item identifier.
    id: str = ""
    #: The type of the item.
    type: str = ""
    #: The display name for the item.
    display_name: str = ""
    #: The quantity for the item.
    price: Optional[Price] = None
    #: The quantity for the item.
    quantity: Optional[int] = None
    #: The quantity the plan is set to renew at.
    renew_quantity: Optional[int] = None
    #: The minimum quantity allowed.
    min_quantity: Optional[int] = None
    #: The maximum quantity allowed.
    max_quantity: Optional[int] = None
    #: The billing period for the item.
    period: Optional[commonv1.Period] = None
    #: The subtotal amount at checkout.
    subtotal_amount: Optional[str] = None
    #: The item-level discount amount at checkout.
    discount_amount: Optional[str] = None
    #: The item-level normal recurring amount.
    renew_amount: Optional[str] = None
    #: Whether this is a preview-only item.
    #:
    #: Preview-only items are generally prorations or other pending
    #: charges or credits.
    preview: Optional[bool] = None
    #: The parent item.
    #:
    #: This allows you to group related items and is generally set for preview
    #: items.
    parent_item_id: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.type is not None:
            data["type"] = self.type

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.price is not None:
            data["price"] = Price.__json_encode__(self.price)

        if self.quantity is not None:
            data["quantity"] = self.quantity

        if self.renew_quantity is not None:
            data["renewQuantity"] = self.renew_quantity

        if self.min_quantity is not None:
            data["minQuantity"] = self.min_quantity

        if self.max_quantity is not None:
            data["maxQuantity"] = self.max_quantity

        if self.period is not None:
            data["period"] = commonv1.Period.__json_encode__(self.period)

        if self.subtotal_amount is not None:
            data["subtotalAmount"] = self.subtotal_amount

        if self.discount_amount is not None:
            data["discountAmount"] = self.discount_amount

        if self.renew_amount is not None:
            data["renewAmount"] = self.renew_amount

        if self.preview is not None:
            data["preview"] = self.preview

        if self.parent_item_id is not None:
            data["parentItemId"] = self.parent_item_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutItem":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("price") is not None:
            kwargs["price"] = Price.__json_decode__(data["price"])

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        if data.get("renewQuantity") is not None:
            kwargs["renew_quantity"] = data["renewQuantity"]

        if data.get("minQuantity") is not None:
            kwargs["min_quantity"] = data["minQuantity"]

        if data.get("maxQuantity") is not None:
            kwargs["max_quantity"] = data["maxQuantity"]

        if data.get("period") is not None:
            kwargs["period"] = commonv1.Period.__json_decode__(data["period"])

        if data.get("subtotalAmount") is not None:
            kwargs["subtotal_amount"] = data["subtotalAmount"]

        if data.get("discountAmount") is not None:
            kwargs["discount_amount"] = data["discountAmount"]

        if data.get("renewAmount") is not None:
            kwargs["renew_amount"] = data["renewAmount"]

        if data.get("preview") is not None:
            kwargs["preview"] = data["preview"]

        if data.get("parentItemId") is not None:
            kwargs["parent_item_id"] = data["parentItemId"]

        return CheckoutItem(**kwargs)
