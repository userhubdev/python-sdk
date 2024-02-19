# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import commonv1

from ._price import Price
from ._product import Product


@dataclasses.dataclass
class InvoicePreviewItem:
    """
    The line items for the preview.
    """

    #: The details of the associated product.
    product: Optional[Product] = None
    #: The details of the associated price.
    price: Optional[Price] = None
    #: The quantity of the item product/price.
    quantity: Optional[int] = None
    #: The total amount for the line item excluding
    #: taxes and discounts.
    subtotal_amount: Optional[str] = None
    #: The item-level discount amount.
    discount_amount: Optional[str] = None
    #: The user facing description for the line item.
    description: Optional[str] = None
    #: Whether the item was a proration.
    proration: Optional[bool] = None
    #: The billing period for the item.
    period: Optional[commonv1.Period] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.product is not None:
            data["product"] = Product.__json_encode__(self.product)

        if self.price is not None:
            data["price"] = Price.__json_encode__(self.price)

        if self.quantity is not None:
            data["quantity"] = self.quantity

        if self.subtotal_amount is not None:
            data["subtotalAmount"] = self.subtotal_amount

        if self.discount_amount is not None:
            data["discountAmount"] = self.discount_amount

        if self.description is not None:
            data["description"] = self.description

        if self.proration is not None:
            data["proration"] = self.proration

        if self.period is not None:
            data["period"] = commonv1.Period.__json_encode__(self.period)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "InvoicePreviewItem":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        if data.get("price") is not None:
            kwargs["price"] = Price.__json_decode__(data["price"])

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        if data.get("subtotalAmount") is not None:
            kwargs["subtotal_amount"] = data["subtotalAmount"]

        if data.get("discountAmount") is not None:
            kwargs["discount_amount"] = data["discountAmount"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("proration") is not None:
            kwargs["proration"] = data["proration"]

        if data.get("period") is not None:
            kwargs["period"] = commonv1.Period.__json_decode__(data["period"])

        return InvoicePreviewItem(**kwargs)
