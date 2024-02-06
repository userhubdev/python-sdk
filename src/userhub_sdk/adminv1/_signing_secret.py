# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class SigningSecret:
    """
    The signing secret for the webhook.
    """

    #: The signing secret value.
    secret: str = ""
    #: The time the signing secret is set to expire.
    expire_time: Optional[datetime.datetime] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("secret") is not None:
            kwargs["secret"] = data["secret"]

        if data.get("expireTime") is not None:
            kwargs["expire_time"] = util.decode_datetime(data["expireTime"])

        return SigningSecret(**kwargs)
