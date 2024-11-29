# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import commonv1


@dataclasses.dataclass
class AccountConnectionInput:
    """
    AccountConnection input parameters.
    """

    #: The system-assigned identifier for the connection of the external account.
    connection_id: str = ""
    #: The human-readable display name of the external account.
    #:
    #: The maximum length is 200 characters.
    #:
    #: This might be further restricted by the external provider.
    display_name: Optional[str] = None
    #: The email address of the external account.
    #:
    #: The maximum length is 320 characters.
    #:
    #: This might be further restricted by the external provider.
    email: Optional[str] = None
    #: Whether the external account's email address has been verified.
    email_verified: Optional[bool] = None
    #: The E164 phone number for the external account (e.g. `+12125550123`).
    phone_number: Optional[str] = None
    #: Whether the external account's phone number has been verified.
    phone_number_verified: Optional[bool] = None
    #: The default ISO-4217 currency code for the external account (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The billing address for the external account.
    address: Optional[commonv1.Address] = None
    #: Whether the external account is disabled.
    disabled: Optional[bool] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.connection_id is not None:
            data["connectionId"] = self.connection_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        if self.email_verified is not None:
            data["emailVerified"] = self.email_verified

        if self.phone_number is not None:
            data["phoneNumber"] = self.phone_number

        if self.phone_number_verified is not None:
            data["phoneNumberVerified"] = self.phone_number_verified

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        if self.disabled is not None:
            data["disabled"] = self.disabled

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "AccountConnectionInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("connectionId") is not None:
            kwargs["connection_id"] = data["connectionId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("emailVerified") is not None:
            kwargs["email_verified"] = data["emailVerified"]

        if data.get("phoneNumber") is not None:
            kwargs["phone_number"] = data["phoneNumber"]

        if data.get("phoneNumberVerified") is not None:
            kwargs["phone_number_verified"] = data["phoneNumberVerified"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        if data.get("disabled") is not None:
            kwargs["disabled"] = data["disabled"]

        return AccountConnectionInput(**kwargs)
