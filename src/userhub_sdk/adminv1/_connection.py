# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import constants, util

from ._auth0_connection import Auth0Connection
from ._builtin_email_connection import BuiltinEmailConnection
from ._connection_delegate import ConnectionDelegate
from ._connection_provider import ConnectionProvider
from ._google_cloud_identity_platform_connection import (
    GoogleCloudIdentityPlatformConnection,
)
from ._postmark_connection import PostmarkConnection
from ._stripe_connection import StripeConnection
from ._webhook_connection import WebhookConnection


@dataclasses.dataclass
class Connection:
    """
    An integration that connects your tenant to an external system.
    """

    #: The system-assigned identifier of the connection.
    id: str = ""
    #: The client defined unique identifier of the connection.
    #:
    #: It is restricted to letters, numbers, underscores, and hyphens,
    #: with the first character a letter or a number, and a 255
    #: character maximum.
    #:
    #: ID's starting with `conn_` are reserved.
    unique_id: Optional[str] = None
    #: The human-readable display name of the connection.
    #:
    #: The maximum length is 200 characters.
    display_name: str = ""
    #: The current status of the connection.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The connection type.
    type: str = ""
    #: The delegated connection.
    delegate: Optional[ConnectionDelegate] = None
    #: The connection providers.
    providers: List[ConnectionProvider] = dataclasses.field(default_factory=list)
    #: The creation time of the connection.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the connection.
    update_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The Auth0 connection data.
    auth0: Optional[Auth0Connection] = None
    #: The builtin email configuration data.
    builtin_email: Optional[BuiltinEmailConnection] = None
    #: The Google Cloud Identity Platform (Firebase Auth) connection.
    google_cloud_identity_platform: Optional[
        GoogleCloudIdentityPlatformConnection
    ] = None
    #: The Postmark configuration data.
    postmark: Optional[PostmarkConnection] = None
    #: The Stripe billing configuration data.
    stripe: Optional[StripeConnection] = None
    #: The webhooks configuration data.
    webhook: Optional[WebhookConnection] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

        if self.type is not None:
            data["type"] = self.type

        if self.delegate is not None:
            data["delegate"] = ConnectionDelegate.__json_encode__(self.delegate)

        if self.providers is not None:
            data["providers"] = [
                ConnectionProvider.__json_encode__(v) for v in self.providers
            ]

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        if self.auth0 is not None:
            data["auth0"] = Auth0Connection.__json_encode__(self.auth0)

        if self.builtin_email is not None:
            data["builtinEmail"] = BuiltinEmailConnection.__json_encode__(
                self.builtin_email
            )

        if self.google_cloud_identity_platform is not None:
            data[
                "googleCloudIdentityPlatform"
            ] = GoogleCloudIdentityPlatformConnection.__json_encode__(
                self.google_cloud_identity_platform
            )

        if self.postmark is not None:
            data["postmark"] = PostmarkConnection.__json_encode__(self.postmark)

        if self.stripe is not None:
            data["stripe"] = StripeConnection.__json_encode__(self.stripe)

        if self.webhook is not None:
            data["webhook"] = WebhookConnection.__json_encode__(self.webhook)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Connection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("delegate") is not None:
            kwargs["delegate"] = ConnectionDelegate.__json_decode__(data["delegate"])

        if data.get("providers") is not None:
            kwargs["providers"] = [
                ConnectionProvider.__json_decode__(v) for v in data["providers"]
            ]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        if data.get("auth0") is not None:
            kwargs["auth0"] = Auth0Connection.__json_decode__(data["auth0"])

        if data.get("builtinEmail") is not None:
            kwargs["builtin_email"] = BuiltinEmailConnection.__json_decode__(
                data["builtinEmail"]
            )

        if data.get("googleCloudIdentityPlatform") is not None:
            kwargs[
                "google_cloud_identity_platform"
            ] = GoogleCloudIdentityPlatformConnection.__json_decode__(
                data["googleCloudIdentityPlatform"]
            )

        if data.get("postmark") is not None:
            kwargs["postmark"] = PostmarkConnection.__json_decode__(data["postmark"])

        if data.get("stripe") is not None:
            kwargs["stripe"] = StripeConnection.__json_decode__(data["stripe"])

        if data.get("webhook") is not None:
            kwargs["webhook"] = WebhookConnection.__json_decode__(data["webhook"])

        return Connection(**kwargs)
