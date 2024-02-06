# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import constants
from .._internal import util


@dataclasses.dataclass
class CreateApiSessionResponse:
    """
    Response message for CreateApiSession.
    """

    #: An authorization token which can be used to access the User API.
    #:
    #: This should be included in the `Authorization` header with a
    #: `Bearer` prefix.
    access_token: str = ""
    #: The expiration time for the session.
    expire_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("accessToken") is not None:
            kwargs["access_token"] = data["accessToken"]

        if data.get("expireTime") is not None:
            kwargs["expire_time"] = util.decode_datetime(data["expireTime"])

        return CreateApiSessionResponse(**kwargs)
