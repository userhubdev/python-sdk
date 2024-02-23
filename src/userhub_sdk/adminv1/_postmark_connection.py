# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional

from userhub_sdk import commonv1


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
    server_id: str = ""
    #: The from email address.
    #:
    #: The Postmark account must be allowed to send from this email
    #: address.
    from_: Optional[commonv1.Email] = None
    #: The reply to email address.
    reply_to: Optional[commonv1.Email] = None
    #: The allowed email list.
    allowed_emails: List[str] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.server_token is not None:
            data["serverToken"] = self.server_token

        if self.server_id is not None:
            data["serverId"] = self.server_id

        if self.from_ is not None:
            data["from"] = commonv1.Email.__json_encode__(self.from_)

        if self.reply_to is not None:
            data["replyTo"] = commonv1.Email.__json_encode__(self.reply_to)

        if self.allowed_emails is not None:
            data["allowedEmails"] = self.allowed_emails

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PostmarkConnection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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
