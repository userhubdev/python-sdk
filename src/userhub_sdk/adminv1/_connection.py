# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import List
from typing import Optional

from .._internal import constants
from .._internal import util
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
    providers: Optional[List[ConnectionProvider]] = dataclasses.field(
        default_factory=list
    )
    #: The creation time of the connection.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the connection.
    update_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The Auth0 connection data.
    auth0: Optional[Auth0Connection] = None
    #: The builtin email configuration data.
    builtin_email: Optional[BuiltinEmailConnection] = None
    #: The Google Cloud Identity Platform (Firebase Auth) connection.
    google_cloud_identity_platform: Optional[GoogleCloudIdentityPlatformConnection] = (
        None
    )
    #: The Postmark configuration data.
    postmark: Optional[PostmarkConnection] = None
    #: The Stripe billing configuration data.
    stripe: Optional[StripeConnection] = None
    #: The webhooks configuration data.
    webhook: Optional[WebhookConnection] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

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
            kwargs["google_cloud_identity_platform"] = (
                GoogleCloudIdentityPlatformConnection.__json_decode__(
                    data["googleCloudIdentityPlatform"]
                )
            )

        if data.get("postmark") is not None:
            kwargs["postmark"] = PostmarkConnection.__json_decode__(data["postmark"])

        if data.get("stripe") is not None:
            kwargs["stripe"] = StripeConnection.__json_decode__(data["stripe"])

        if data.get("webhook") is not None:
            kwargs["webhook"] = WebhookConnection.__json_decode__(data["webhook"])

        return Connection(**kwargs)
