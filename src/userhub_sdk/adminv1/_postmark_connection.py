# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .. import commonv1
from .._internal import util


@dataclasses.dataclass
class PostmarkConnection:
    """
    The Postmark specific connection data.
    """

    #: The Postmark server token (e.g. `942faf79-bf10-4dc1-830a-dc7943f43f35`).
    server_token: str = ""
    #: The Postmark server ID.
    #:
    #: This is automatically populated when the server token is updated.
    server_id: Optional[str] = None
    #: The from email address.
    #:
    #: The Postmark account must be allowed to send from this email
    #: address.
    from_: Optional[commonv1.Email] = None
    #: The reply to email address.
    reply_to: Optional[commonv1.Email] = None
    #: The allowed email list.
    allowed_emails: List[str] = dataclasses.field(default_factory=list)

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("serverToken") is not None:
            kwargs["server_token"] = data["serverToken"]

        if data.get("serverId") is not None:
            kwargs["server_id"] = data["serverId"]

        if data.get("from") is not None:
            kwargs["from_"] = commonv1.Email.__json_decode__(data["from"])

        if data.get("replyTo") is not None:
            kwargs["reply_to"] = commonv1.Email.__json_decode__(data["replyTo"])

        if data.get("allowedEmails") is not None:
            kwargs["allowed_emails"] = data["allowedEmails"]

        return PostmarkConnection(**kwargs)
