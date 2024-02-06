# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


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

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("startAmount") is not None:
            kwargs["start_amount"] = data["startAmount"]

        if data.get("endAmount") is not None:
            kwargs["end_amount"] = data["endAmount"]

        if data.get("appliedAmount") is not None:
            kwargs["applied_amount"] = data["appliedAmount"]

        return InvoiceBalance(**kwargs)
