# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import commonv1


@dataclasses.dataclass
class InvoiceAccount:
    """
    THe contact information of the bill to account.
    """

    #: The company or individual's full name.
    full_name: Optional[str] = None
    #: The billing email address.
    email: Optional[str] = None
    #: The billing phone number.
    phone_number: Optional[str] = None
    #: The billing address.
    address: Optional[commonv1.Address] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.full_name is not None:
            data["fullName"] = self.full_name

        if self.email is not None:
            data["email"] = self.email

        if self.phone_number is not None:
            data["phoneNumber"] = self.phone_number

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "InvoiceAccount":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("fullName") is not None:
            kwargs["full_name"] = data["fullName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("phoneNumber") is not None:
            kwargs["phone_number"] = data["phoneNumber"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        return InvoiceAccount(**kwargs)
