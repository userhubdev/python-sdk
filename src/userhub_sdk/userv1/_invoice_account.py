# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import commonv1
from .._internal import util


@dataclasses.dataclass
class InvoiceAccount:
    """
    THe contact information for the invoice.
    """

    #: The company or individual's full name.
    full_name: Optional[str] = None
    #: The billing email address.
    email: Optional[str] = None
    #: The billing phone number.
    phone_number: Optional[str] = None
    #: The billing address.
    address: Optional[commonv1.Address] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("fullName") is not None:
            kwargs["full_name"] = data["fullName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("phoneNumber") is not None:
            kwargs["phone_number"] = data["phoneNumber"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        return InvoiceAccount(**kwargs)
