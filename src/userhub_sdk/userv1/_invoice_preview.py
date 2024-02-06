# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import List
from typing import Optional

from .._internal import util
from ._invoice_account import InvoiceAccount
from ._invoice_balance import InvoiceBalance
from ._invoice_preview_item import InvoicePreviewItem


@dataclasses.dataclass
class InvoicePreview:
    """
    A preview of an invoice.
    """

    #: The currency code for the invoice (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The contact information associated with the invoice.
    account: Optional[InvoiceAccount] = None
    #: The time the upcoming invoice will be finalized.
    #:
    #: This is an estimate and might not exactly match the finalized
    #: invoice.
    #:
    #: This will be null if the preview would be applied
    #: immediately.
    effective_time: Optional[datetime.datetime] = None
    #: The subtotal amount for the invoice.
    #:
    #: This includes item-level discounts.
    subtotal_amount: Optional[str] = None
    #: The invoice-level discount amount.
    #:
    #: This does not include item level discounts.
    discount_amount: Optional[str] = None
    #: The starting and ending account balance as
    #: of the time the invoice was finalized.
    balance: Optional[InvoiceBalance] = None
    #: The tax amount for the invoice.
    #:
    #: This is for rendering purposes only and is
    #: not the reported tax amount.
    tax_amount: Optional[str] = None
    #: The total amount for the invoice.
    total_amount: Optional[str] = None
    #: The total amount minus any credits automatically
    #: associated with the invoice.
    due_amount: Optional[str] = None
    #: A token which can be passed to a create or update
    #: operation to ensure the change matches the preview.
    #:
    #: This token generally expires within 10 minutes of
    #: being generated.
    change_token: Optional[str] = None
    #: The line items for the invoice.
    items: Optional[List[InvoicePreviewItem]] = dataclasses.field(default_factory=list)

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("account") is not None:
            kwargs["account"] = InvoiceAccount.__json_decode__(data["account"])

        if data.get("effectiveTime") is not None:
            kwargs["effective_time"] = util.decode_datetime(data["effectiveTime"])

        if data.get("subtotalAmount") is not None:
            kwargs["subtotal_amount"] = data["subtotalAmount"]

        if data.get("discountAmount") is not None:
            kwargs["discount_amount"] = data["discountAmount"]

        if data.get("balance") is not None:
            kwargs["balance"] = InvoiceBalance.__json_decode__(data["balance"])

        if data.get("taxAmount") is not None:
            kwargs["tax_amount"] = data["taxAmount"]

        if data.get("totalAmount") is not None:
            kwargs["total_amount"] = data["totalAmount"]

        if data.get("dueAmount") is not None:
            kwargs["due_amount"] = data["dueAmount"]

        if data.get("changeToken") is not None:
            kwargs["change_token"] = data["changeToken"]

        if data.get("items") is not None:
            kwargs["items"] = [
                InvoicePreviewItem.__json_decode__(v) for v in data["items"]
            ]

        return InvoicePreview(**kwargs)
