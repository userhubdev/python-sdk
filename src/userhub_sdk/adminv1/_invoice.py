# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk import commonv1
from userhub_sdk._internal import constants, util

from ._connection import Connection
from ._invoice_account import InvoiceAccount
from ._invoice_balance import InvoiceBalance
from ._invoice_change import InvoiceChange
from ._invoice_item import InvoiceItem
from ._payment_intent import PaymentIntent


@dataclasses.dataclass
class Invoice:
    """
    A bill or statement.
    """

    #: The system-assigned identifier of the invoice.
    id: str = ""
    #: The status of the invoice.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The time associated with the current state (e.g. paid time).
    state_time: Optional[datetime.datetime] = None
    #: The billing connection.
    connection: Optional[Connection] = None
    #: The external identifier of the invoice.
    external_id: str = ""
    #: The invoice number.
    number: Optional[str] = None
    #: The currency code for the invoice (e.g. `USD`).
    currency_code: str = ""
    #: The user facing description for the invoice.
    description: Optional[str] = None
    #: The bill to contact information.
    account: Optional[InvoiceAccount] = None
    #: The time the invoice was finalized.
    effective_time: Optional[datetime.datetime] = None
    #: The billing period for the invoice.
    period: Optional[commonv1.Period] = None
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
    #: The due amount minus the amount already paid.
    remaining_due_amount: Optional[str] = None
    #: The time the invoice must be paid by.
    due_time: Optional[datetime.datetime] = None
    #: The amount already paid towards the invoice.
    paid_amount: Optional[str] = None
    #: The status of the invoice payment.
    payment_state: Optional[str] = None
    #: The payment intent for the invoice.
    payment_intent: Optional[PaymentIntent] = None
    #: The line items for the invoice.
    items: Optional[List[InvoiceItem]] = dataclasses.field(default_factory=list)
    #: The prorated changes that occurred mid-billing cycle.
    changes: Optional[List[InvoiceChange]] = dataclasses.field(default_factory=list)
    #: The last time the invoice was pulled from the connection.
    pull_time: Optional[datetime.datetime] = None
    #: The creation time of the invoice.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the invoice.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

        if self.state_time is not None:
            data["stateTime"] = util.encode_datetime(self.state_time)

        if self.connection is not None:
            data["connection"] = Connection.__json_encode__(self.connection)

        if self.external_id is not None:
            data["externalId"] = self.external_id

        if self.number is not None:
            data["number"] = self.number

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.description is not None:
            data["description"] = self.description

        if self.account is not None:
            data["account"] = InvoiceAccount.__json_encode__(self.account)

        if self.effective_time is not None:
            data["effectiveTime"] = util.encode_datetime(self.effective_time)

        if self.period is not None:
            data["period"] = commonv1.Period.__json_encode__(self.period)

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

        if self.remaining_due_amount is not None:
            data["remainingDueAmount"] = self.remaining_due_amount

        if self.due_time is not None:
            data["dueTime"] = util.encode_datetime(self.due_time)

        if self.paid_amount is not None:
            data["paidAmount"] = self.paid_amount

        if self.payment_state is not None:
            data["paymentState"] = self.payment_state

        if self.payment_intent is not None:
            data["paymentIntent"] = PaymentIntent.__json_encode__(self.payment_intent)

        if self.items is not None:
            data["items"] = [InvoiceItem.__json_encode__(v) for v in self.items]

        if self.changes is not None:
            data["changes"] = [InvoiceChange.__json_encode__(v) for v in self.changes]

        if self.pull_time is not None:
            data["pullTime"] = util.encode_datetime(self.pull_time)

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Invoice":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

        if data.get("stateTime") is not None:
            kwargs["state_time"] = util.decode_datetime(data["stateTime"])

        if data.get("connection") is not None:
            kwargs["connection"] = Connection.__json_decode__(data["connection"])

        if data.get("externalId") is not None:
            kwargs["external_id"] = data["externalId"]

        if data.get("number") is not None:
            kwargs["number"] = data["number"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("account") is not None:
            kwargs["account"] = InvoiceAccount.__json_decode__(data["account"])

        if data.get("effectiveTime") is not None:
            kwargs["effective_time"] = util.decode_datetime(data["effectiveTime"])

        if data.get("period") is not None:
            kwargs["period"] = commonv1.Period.__json_decode__(data["period"])

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

        if data.get("remainingDueAmount") is not None:
            kwargs["remaining_due_amount"] = data["remainingDueAmount"]

        if data.get("dueTime") is not None:
            kwargs["due_time"] = util.decode_datetime(data["dueTime"])

        if data.get("paidAmount") is not None:
            kwargs["paid_amount"] = data["paidAmount"]

        if data.get("paymentState") is not None:
            kwargs["payment_state"] = data["paymentState"]

        if data.get("paymentIntent") is not None:
            kwargs["payment_intent"] = PaymentIntent.__json_decode__(
                data["paymentIntent"]
            )

        if data.get("items") is not None:
            kwargs["items"] = [InvoiceItem.__json_decode__(v) for v in data["items"]]

        if data.get("changes") is not None:
            kwargs["changes"] = [
                InvoiceChange.__json_decode__(v) for v in data["changes"]
            ]

        if data.get("pullTime") is not None:
            kwargs["pull_time"] = util.decode_datetime(data["pullTime"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Invoice(**kwargs)
