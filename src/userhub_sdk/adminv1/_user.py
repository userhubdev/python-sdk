# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk import commonv1
from userhub_sdk._internal import constants, util

from ._account_connection import AccountConnection
from ._account_subscription import AccountSubscription
from ._membership import Membership


@dataclasses.dataclass
class User:
    """
    Individual account.
    """

    #: The system-assigned identifier of the user.
    id: str = ""
    #: The current state of the user.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The client defined unique identifier of the user account.
    unique_id: Optional[str] = None
    #: The human-readable display name of the user.
    display_name: Optional[str] = None
    #: The email address of the user.
    email: Optional[str] = None
    #: Whether the user's email address has been verified.
    email_verified: Optional[bool] = None
    #: The E164 phone number for the user (e.g. `+12125550123`).
    phone_number: Optional[str] = None
    #: Whether the user's phone number has been verified.
    phone_number_verified: Optional[bool] = None
    #: The photo/avatar URL of the user.
    image_url: Optional[str] = None
    #: The default ISO-4217 currency code for the user (e.g. `USD`).
    currency_code: Optional[str] = None
    #: The IETF BCP-47 language code for the user (e.g. `en`).
    language_code: Optional[str] = None
    #: The country/region code for the user (e.g. `US`).
    region_code: Optional[str] = None
    #: The IANA time zone for the user (e.g. `America/New_York`).
    time_zone: Optional[str] = None
    #: The billing address for the user.
    address: Optional[commonv1.Address] = None
    #: The connected accounts.
    account_connections: Optional[List[AccountConnection]] = dataclasses.field(
        default_factory=list
    )
    #: The user's default active individual subscription.
    #:
    #: See memberships for organization subscription and
    #: seat information.
    subscription: Optional[AccountSubscription] = None
    #: The user's organization memberships.
    memberships: Optional[List[Membership]] = dataclasses.field(default_factory=list)
    #: The sign-up time for the user.
    signup_time: Optional[datetime.datetime] = None
    #: Whether the user is disabled.
    disabled: Optional[bool] = None
    #: The creation time of the user.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the user.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

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

        if self.account_connections is not None:
            data["accountConnections"] = [
                AccountConnection.__json_encode__(v) for v in self.account_connections
            ]

        if self.subscription is not None:
            data["subscription"] = AccountSubscription.__json_encode__(
                self.subscription
            )

        if self.memberships is not None:
            data["memberships"] = [
                Membership.__json_encode__(v) for v in self.memberships
            ]

        if self.signup_time is not None:
            data["signupTime"] = util.encode_datetime(self.signup_time)

        if self.disabled is not None:
            data["disabled"] = self.disabled

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "User":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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

        if data.get("memberships") is not None:
            kwargs["memberships"] = [
                Membership.__json_decode__(v) for v in data["memberships"]
            ]

        if data.get("signupTime") is not None:
            kwargs["signup_time"] = util.decode_datetime(data["signupTime"])

        if data.get("disabled") is not None:
            kwargs["disabled"] = data["disabled"]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return User(**kwargs)
