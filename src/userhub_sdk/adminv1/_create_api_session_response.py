# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict

from userhub_sdk._internal import constants, util


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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.access_token is not None:
            data["accessToken"] = self.access_token

        if self.expire_time is not None:
            data["expireTime"] = util.encode_datetime(self.expire_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CreateApiSessionResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("accessToken") is not None:
            kwargs["access_token"] = data["accessToken"]

        if data.get("expireTime") is not None:
            kwargs["expire_time"] = util.decode_datetime(data["expireTime"])

        return CreateApiSessionResponse(**kwargs)
