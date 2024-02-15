# Code generated. DO NOT EDIT.

import dataclasses
from typing import Dict
from typing import List
from typing import Optional

from .._internal import util
from ._signing_secret import SigningSecret


@dataclasses.dataclass
class WebhookConnection:
    """
    The webhook specific connection data.
    """

    #: The URL of the events webhook.
    url: str = ""
    #: The headers sent with requests to the connection URL.
    headers: Dict[str, str] = dataclasses.field(default_factory=dict)
    #: The webhook secrets
    signing_secrets: Optional[List[SigningSecret]] = dataclasses.field(
        default_factory=list
    )

    def __json_encode__(self):
        data = {}

        if self.url is not None:
            data["url"] = self.url

        if self.headers is not None:
            data["headers"] = self.headers

        if self.signing_secrets is not None:
            data["signingSecrets"] = [
                SigningSecret.__json_encode__(v) for v in self.signing_secrets
            ]

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("url") is not None:
            kwargs["url"] = data["url"]

        if data.get("headers") is not None:
            kwargs["headers"] = data["headers"]

        if data.get("signingSecrets") is not None:
            kwargs["signing_secrets"] = [
                SigningSecret.__json_decode__(v) for v in data["signingSecrets"]
            ]

        return WebhookConnection(**kwargs)
