# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import commonv1


@dataclasses.dataclass
class BillingAccountInput:
    """
    BillingAccountInput input parameters.
    """

    #: The human-readable display name of the billing account.
    #:
    #: The maximum length is 200 characters.
    #:
    #: This might be further restricted by the billing provider.
    display_name: Optional[str] = None
    #: The email address of the billing account.
    #:
    #: The maximum length is 320 characters.
    #:
    #: This might be further restricted by the billing provider.
    email: Optional[str] = None
    #: The E164 phone number of the billing account (e.g. `+12125550123`).
    phone_number: Optional[str] = None
    #: The address for the billing account.
    address: Optional[commonv1.Address] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        if self.phone_number is not None:
            data["phoneNumber"] = self.phone_number

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "BillingAccountInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("phoneNumber") is not None:
            kwargs["phone_number"] = data["phoneNumber"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        return BillingAccountInput(**kwargs)
