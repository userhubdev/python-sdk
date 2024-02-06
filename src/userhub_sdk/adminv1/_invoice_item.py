# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import commonv1
from .._internal import util
from ._price import Price
from ._product import Product


@dataclasses.dataclass
class InvoiceItem:
    """
    The line items for the invoice.
    """

    #: The identifier of the item.
    id: str = ""
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
    #: The external identifier of the invoice item.
    external_id: Optional[str] = None
    #: Whether the item was a proration.
    proration: Optional[bool] = None
    #: The billing period for the item.
    period: Optional[commonv1.Period] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

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

        if data.get("externalId") is not None:
            kwargs["external_id"] = data["externalId"]

        if data.get("proration") is not None:
            kwargs["proration"] = data["proration"]

        if data.get("period") is not None:
            kwargs["period"] = commonv1.Period.__json_decode__(data["period"])

        return InvoiceItem(**kwargs)
