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
    #: The display name for the item.
    display_name: str = ""
    #: The input type of the item.
    input_type: str = ""
    #: The type of the item.
    type: Optional[str] = None
    #: The unit for the item.
    unit: Optional[str] = None
    #: The price for the item.
    price: Optional[Price] = None
    #: The quantity for the item.
    quantity: Optional[int] = None
    #: The minimum quantity allowed.
    #:
    #: This will only be set when quantity is settable.
    min_quantity: Optional[int] = None
    #: The maximum quantity allowed.
    #:
    #: This will only be set when the quantity is settable and there is a
    #: discrete (non-infinity) maximum.
    max_quantity: Optional[int] = None
    #: The quantity at which the plan will renew.
    #:
    #: This will only be set when different from quantity and the
    #: subscription is set to renew.
    renew_quantity: Optional[int] = None
    #: The minimum renew quantity allowed.
    #:
    #: This will only be set when renew quantity is settable.
    min_renew_quantity: Optional[int] = None
    #: The maximum renew quantity allowed.
    #:
    #: This will only be set when the new quantity is settable and there is a
    #: discrete (non-infinity) maximum.
    max_renew_quantity: Optional[int] = None
    #: The billing period for the item.
    period: Optional[commonv1.Period] = None
    #: The subtotal amount at checkout.
    subtotal_amount: Optional[str] = None
    #: The item-level discount amount at checkout.
    discount_amount: Optional[str] = None
    #: The normal recurring amount.
    #:
    #: This does not include any time-limited discounts.
    renew_amount: Optional[str] = None
    #: Whether this is a preview-only item.
    #:
    #: Preview-only items are generally prorations or other pending
    #: charges or credits.
    preview: Optional[bool] = None
    #: The item identifier for which you can group this item.
    #:
    #: This allows you to group credits and other preview items
    #: with the related plan, seat, or add-on item.
    group_item_id: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.input_type is not None:
            data["inputType"] = self.input_type

        if self.type is not None:
            data["type"] = self.type

        if self.unit is not None:
            data["unit"] = self.unit

        if self.price is not None:
            data["price"] = Price.__json_encode__(self.price)

        if self.quantity is not None:
            data["quantity"] = self.quantity

        if self.min_quantity is not None:
            data["minQuantity"] = self.min_quantity

        if self.max_quantity is not None:
            data["maxQuantity"] = self.max_quantity

        if self.renew_quantity is not None:
            data["renewQuantity"] = self.renew_quantity

        if self.min_renew_quantity is not None:
            data["minRenewQuantity"] = self.min_renew_quantity

        if self.max_renew_quantity is not None:
            data["maxRenewQuantity"] = self.max_renew_quantity

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

        if self.group_item_id is not None:
            data["groupItemId"] = self.group_item_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutItem":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("inputType") is not None:
            kwargs["input_type"] = data["inputType"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("unit") is not None:
            kwargs["unit"] = data["unit"]

        if data.get("price") is not None:
            kwargs["price"] = Price.__json_decode__(data["price"])

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        if data.get("minQuantity") is not None:
            kwargs["min_quantity"] = data["minQuantity"]

        if data.get("maxQuantity") is not None:
            kwargs["max_quantity"] = data["maxQuantity"]

        if data.get("renewQuantity") is not None:
            kwargs["renew_quantity"] = data["renewQuantity"]

        if data.get("minRenewQuantity") is not None:
            kwargs["min_renew_quantity"] = data["minRenewQuantity"]

        if data.get("maxRenewQuantity") is not None:
            kwargs["max_renew_quantity"] = data["maxRenewQuantity"]

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

        if data.get("groupItemId") is not None:
            kwargs["group_item_id"] = data["groupItemId"]

        return CheckoutItem(**kwargs)
