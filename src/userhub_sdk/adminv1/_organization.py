# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import List
from typing import Optional

from .. import commonv1
from .._internal import constants
from .._internal import util
from ._account_connection import AccountConnection
from ._account_subscription import AccountSubscription


@dataclasses.dataclass
class Organization:
    """
    A group account.
    """

    #: The system-assigned identifier of the organization.
    id: str = ""
    #: The current state of the organization.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The client defined unique identifier of the organization account.
    unique_id: Optional[str] = None
    #: The human-readable display name of the organization.
    display_name: Optional[str] = None
    #: The email address of the organization.
    email: Optional[str] = None
    #: Whether the organization's email address has been verified.
    email_verified: Optional[bool] = None
    #: The E164 phone number for the organization (e.g. `+12125550123`).
    phone_number: Optional[str] = None
    #: Whether the organization's phone number has been verified.
    phone_number_verified: Optional[bool] = None
    #: The photo/avatar URL of the organization.
    image_url: Optional[str] = None
    #: The default ISO-4217 currency code for the organization (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The IETF BCP-47 language code for the organization (e.g. `en`).
    language_code: Optional[str] = None
    #: The country/region code for the organization (e.g. `US`).
    region_code: Optional[str] = None
    #: The IANA time zone for the organization (e.g. `America/New_York`).
    time_zone: Optional[str] = None
    #: The address for the organization.
    address: Optional[commonv1.Address] = None
    #: The connected accounts.
    account_connections: Optional[List[AccountConnection]] = dataclasses.field(
        default_factory=list
    )
    #: The organization's default active subscription.
    subscription: Optional[AccountSubscription] = None
    #: The sign-up time for the organization.
    signup_time: Optional[datetime.datetime] = None
    #: Whether the organization is disabled.
    disabled: Optional[bool] = None
    #: The creation time of the organization.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the organization.
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

        if data.get("accountConnections") is not None:
            kwargs["account_connections"] = [
                AccountConnection.__json_decode__(v) for v in data["accountConnections"]
            ]

        if data.get("subscription") is not None:
            kwargs["subscription"] = AccountSubscription.__json_decode__(
                data["subscription"]
            )

        if data.get("signupTime") is not None:
            kwargs["signup_time"] = util.decode_datetime(data["signupTime"])

        if data.get("disabled") is not None:
            kwargs["disabled"] = data["disabled"]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Organization(**kwargs)
