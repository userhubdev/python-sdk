# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional

from userhub_sdk import apiv1, commonv1

from ._checkout_discount import CheckoutDiscount
from ._checkout_item import CheckoutItem
from ._checkout_step import CheckoutStep
from ._payment_method import PaymentMethod
from ._plan import Plan


@dataclasses.dataclass
class Checkout:
    """
    The checkout.
    """

    #: The system-assigned identifier of the checkout.
    id: str = ""
    #: The type of checkout.
    type: str = ""
    #: The state of the checkout.
    state: str = ""
    #: The checkout error.
    error: Optional[apiv1.Status] = None
    #: The currently selected currency code.
    currency_code: str = ""
    #: The plans available for checkout.
    plans: Optional[List[Plan]] = dataclasses.field(default_factory=list)
    #: The payment method for the checkout.
    payment_method: Optional[PaymentMethod] = None
    #: The company or individual's full name.
    full_name: Optional[str] = None
    #: The billing address.
    address: Optional[commonv1.Address] = None
    #: The steps required to complete the checkout.
    steps: Optional[List[CheckoutStep]] = dataclasses.field(default_factory=list)
    #: The products included in the checkout.
    items: Optional[List[CheckoutItem]] = dataclasses.field(default_factory=list)
    #: The discounts applied to the checkout.
    discounts: Optional[List[CheckoutDiscount]] = dataclasses.field(
        default_factory=list
    )
    #: The subtotal amount for the checkout.
    #:
    #: This includes item-level discounts.
    subtotal_amount: Optional[str] = None
    #: The top-level discount amount.
    #:
    #: This does not include item level discounts.
    discount_amount: Optional[str] = None
    #: The tax amount for the checkout.
    #:
    #: This is for rendering purposes only and is
    #: not the reported tax amount.
    tax_amount: Optional[str] = None
    #: The total amount for the checkout.
    total_amount: Optional[str] = None
    #: The amount applied to the checkout from the balance.
    #:
    #: A negative amount means a debit from the account balance.
    #: A positive amount means a credit to the account balance.
    balance_applied_amount: Optional[str] = None
    #: The total amount minus any credits automatically
    #: associated with the invoice.
    due_amount: Optional[str] = None
    #: The normal total recurring amount.
    #:
    #: This does not include any time-limited discounts.
    renew_amount: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.type is not None:
            data["type"] = self.type

        if self.state is not None:
            data["state"] = self.state

        if self.error is not None:
            data["error"] = apiv1.Status.__json_encode__(self.error)

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.plans is not None:
            data["plans"] = [Plan.__json_encode__(v) for v in self.plans]

        if self.payment_method is not None:
            data["paymentMethod"] = PaymentMethod.__json_encode__(self.payment_method)

        if self.full_name is not None:
            data["fullName"] = self.full_name

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        if self.steps is not None:
            data["steps"] = [CheckoutStep.__json_encode__(v) for v in self.steps]

        if self.items is not None:
            data["items"] = [CheckoutItem.__json_encode__(v) for v in self.items]

        if self.discounts is not None:
            data["discounts"] = [
                CheckoutDiscount.__json_encode__(v) for v in self.discounts
            ]

        if self.subtotal_amount is not None:
            data["subtotalAmount"] = self.subtotal_amount

        if self.discount_amount is not None:
            data["discountAmount"] = self.discount_amount

        if self.tax_amount is not None:
            data["taxAmount"] = self.tax_amount

        if self.total_amount is not None:
            data["totalAmount"] = self.total_amount

        if self.balance_applied_amount is not None:
            data["balanceAppliedAmount"] = self.balance_applied_amount

        if self.due_amount is not None:
            data["dueAmount"] = self.due_amount

        if self.renew_amount is not None:
            data["renewAmount"] = self.renew_amount

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Checkout":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("error") is not None:
            kwargs["error"] = apiv1.Status.__json_decode__(data["error"])

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("plans") is not None:
            kwargs["plans"] = [Plan.__json_decode__(v) for v in data["plans"]]

        if data.get("paymentMethod") is not None:
            kwargs["payment_method"] = PaymentMethod.__json_decode__(
                data["paymentMethod"]
            )

        if data.get("fullName") is not None:
            kwargs["full_name"] = data["fullName"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        if data.get("steps") is not None:
            kwargs["steps"] = [CheckoutStep.__json_decode__(v) for v in data["steps"]]

        if data.get("items") is not None:
            kwargs["items"] = [CheckoutItem.__json_decode__(v) for v in data["items"]]

        if data.get("discounts") is not None:
            kwargs["discounts"] = [
                CheckoutDiscount.__json_decode__(v) for v in data["discounts"]
            ]

        if data.get("subtotalAmount") is not None:
            kwargs["subtotal_amount"] = data["subtotalAmount"]

        if data.get("discountAmount") is not None:
            kwargs["discount_amount"] = data["discountAmount"]

        if data.get("taxAmount") is not None:
            kwargs["tax_amount"] = data["taxAmount"]

        if data.get("totalAmount") is not None:
            kwargs["total_amount"] = data["totalAmount"]

        if data.get("balanceAppliedAmount") is not None:
            kwargs["balance_applied_amount"] = data["balanceAppliedAmount"]

        if data.get("dueAmount") is not None:
            kwargs["due_amount"] = data["dueAmount"]

        if data.get("renewAmount") is not None:
            kwargs["renew_amount"] = data["renewAmount"]

        return Checkout(**kwargs)
