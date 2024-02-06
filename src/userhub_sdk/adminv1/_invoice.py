# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import List
from typing import Optional

from .. import commonv1
from .._internal import constants
from .._internal import util
from ._connection import Connection
from ._invoice_account import InvoiceAccount
from ._invoice_balance import InvoiceBalance
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
    external_id: Optional[str] = None
    #: The invoice number.
    number: Optional[str] = None
    #: The currency code for the invoice (e.g. `USD`).
    currency_code: Optional[str] = None
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
    #: The last time the invoice was pulled from the connection.
    pull_time: Optional[datetime.datetime] = None
    #: The creation time of the invoice.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the invoice.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

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

        if data.get("pullTime") is not None:
            kwargs["pull_time"] = util.decode_datetime(data["pullTime"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Invoice(**kwargs)
