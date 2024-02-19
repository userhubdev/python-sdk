# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import util


@dataclasses.dataclass
class SigningSecret:
    """
    The signing secret for the webhook.
    """

    #: The signing secret value.
    secret: str = ""
    #: The time the signing secret is set to expire.
    expire_time: Optional[datetime.datetime] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.secret is not None:
            data["secret"] = self.secret

        if self.expire_time is not None:
            data["expireTime"] = util.encode_datetime(self.expire_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "SigningSecret":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("secret") is not None:
            kwargs["secret"] = data["secret"]

        if data.get("expireTime") is not None:
            kwargs["expire_time"] = util.decode_datetime(data["expireTime"])

        return SigningSecret(**kwargs)
