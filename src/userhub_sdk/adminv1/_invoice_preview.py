# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import util

from ._invoice_account import InvoiceAccount
from ._invoice_balance import InvoiceBalance
from ._invoice_preview_item import InvoicePreviewItem


@dataclasses.dataclass
class InvoicePreview:
    """
    A preview of an invoice.
    """

    #: The currency code for the preview (e.g. `USD`).
    currency_code: str = ""
    #: The bill to contact information.
    account: Optional[InvoiceAccount] = None
    #: The time the upcoming invoice will be finalized.
    #:
    #: This is an estimate and might not exactly match the finalized
    #: invoice.
    #:
    #: This will be null if the preview would be applied
    #: immediately.
    effective_time: Optional[datetime.datetime] = None
    #: The subtotal amount for the preview.
    #:
    #: This includes item-level discounts.
    subtotal_amount: Optional[str] = None
    #: The preview-level discount amount.
    #:
    #: This does not include item level discounts.
    discount_amount: Optional[str] = None
    #: The starting and ending account balance as
    #: of the time the preview.
    balance: Optional[InvoiceBalance] = None
    #: The tax amount for the preview.
    tax_amount: Optional[str] = None
    #: The total amount for the preview.
    total_amount: Optional[str] = None
    #: The total amount minus any credits automatically
    #: associated with the preview.
    due_amount: Optional[str] = None
    #: A token which can be passed to a create or update
    #: operation to ensure the change matches the preview.
    #:
    #: This token generally expires within 10 minutes of
    #: being generated.
    change_token: Optional[str] = None
    #: The line items for the invoice.
    items: Optional[List[InvoicePreviewItem]] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.account is not None:
            data["account"] = InvoiceAccount.__json_encode__(self.account)

        if self.effective_time is not None:
            data["effectiveTime"] = util.encode_datetime(self.effective_time)

        if self.subtotal_amount is not None:
            data["subtotalAmount"] = self.subtotal_amount

        if self.discount_amount is not None:
            data["discountAmount"] = self.discount_amount

        if self.balance is not None:
            data["balance"] = InvoiceBalance.__json_encode__(self.balance)

        if self.tax_amount is not None:
            data["taxAmount"] = self.tax_amount

        if self.total_amount is not None:
            data["totalAmount"] = self.total_amount

        if self.due_amount is not None:
            data["dueAmount"] = self.due_amount

        if self.change_token is not None:
            data["changeToken"] = self.change_token

        if self.items is not None:
            data["items"] = [InvoicePreviewItem.__json_encode__(v) for v in self.items]

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "InvoicePreview":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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
