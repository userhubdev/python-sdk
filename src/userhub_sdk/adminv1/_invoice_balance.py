# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class InvoiceBalance:
    """
    The account balance as of the time the invoice
    was finalized.
    """

    #: The starting balance of the account.
    start_amount: Optional[str] = None
    #: The ending balance of the account.
    end_amount: Optional[str] = None
    #: The amount applied to the invoice from the balance.
    #:
    #: A negative amount means a debit from the account balance.
    #: A positive amount means a credit to the account balance.
    applied_amount: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.start_amount is not None:
            data["startAmount"] = self.start_amount

        if self.end_amount is not None:
            data["endAmount"] = self.end_amount

        if self.applied_amount is not None:
            data["appliedAmount"] = self.applied_amount

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "InvoiceBalance":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("startAmount") is not None:
            kwargs["start_amount"] = data["startAmount"]

        if data.get("endAmount") is not None:
            kwargs["end_amount"] = data["endAmount"]

        if data.get("appliedAmount") is not None:
            kwargs["applied_amount"] = data["appliedAmount"]

        return InvoiceBalance(**kwargs)
