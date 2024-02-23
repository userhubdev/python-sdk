# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk import commonv1
from userhub_sdk._internal import util


@dataclasses.dataclass
class OrganizationInput:
    """
    Organization input parameters.
    """

    #: The system-assigned identifier of the organization.
    id: str = ""
    #: The client defined unique identifier of the organization account.
    #:
    #: It is restricted to letters, numbers, underscores, and hyphens,
    #: with the first character a letter or a number, and a 255
    #: character maximum.
    #:
    #: ID's starting with `org_` are reserved.
    unique_id: Optional[str] = None
    #: The human-readable display name of the organization.
    #:
    #: The maximum length is 200 characters.
    display_name: Optional[str] = None
    #: The email address of the organization.
    #:
    #: The maximum length is 320 characters.
    email: Optional[str] = None
    #: Whether the organization's email address has been verified.
    email_verified: Optional[bool] = None
    #: The E164 phone number for the organization (e.g. `+12125550123`).
    phone_number: Optional[str] = None
    #: Whether the organization's phone number has been verified.
    phone_number_verified: Optional[bool] = None
    #: The photo/avatar URL of the organization.
    #:
    #: The maximum length is 2000 characters.
    image_url: Optional[str] = None
    #: The default ISO-4217 currency code for the organization (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The IETF BCP-47 language code for the organization (e.g. `en`).
    language_code: Optional[str] = None
    #: The country/region code for the organization (e.g. `US`).
    region_code: Optional[str] = None
    #: The IANA time zone for the organization (e.g. `America/New_York`).
    time_zone: Optional[str] = None
    #: The billing address for the organization.
    address: Optional[commonv1.Address] = None
    #: The sign-up time for the organization.
    signup_time: Optional[datetime.datetime] = None
    #: Whether the organization is disabled.
    disabled: Optional[bool] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

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

        if self.image_url is not None:
            data["imageUrl"] = self.image_url

        if self.currency_code is not None:
            data["currencyCode"] = self.currency_code

        if self.language_code is not None:
            data["languageCode"] = self.language_code

        if self.region_code is not None:
            data["regionCode"] = self.region_code

        if self.time_zone is not None:
            data["timeZone"] = self.time_zone

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        if self.signup_time is not None:
            data["signupTime"] = util.encode_datetime(self.signup_time)

        if self.disabled is not None:
            data["disabled"] = self.disabled

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "OrganizationInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

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

        if data.get("imageUrl") is not None:
            kwargs["image_url"] = data["imageUrl"]

        if data.get("currencyCode") is not None:
            kwargs["currency_code"] = data["currencyCode"]

        if data.get("languageCode") is not None:
            kwargs["language_code"] = data["languageCode"]

        if data.get("regionCode") is not None:
            kwargs["region_code"] = data["regionCode"]

        if data.get("timeZone") is not None:
            kwargs["time_zone"] = data["timeZone"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        if data.get("signupTime") is not None:
            kwargs["signup_time"] = util.decode_datetime(data["signupTime"])

        if data.get("disabled") is not None:
            kwargs["disabled"] = data["disabled"]

        return OrganizationInput(**kwargs)
