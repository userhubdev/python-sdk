# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict

from userhub_sdk._internal import constants, util

from ._connection import Connection


@dataclasses.dataclass
class Trigger:
    """
    A trigger is a way to run connection functionality when specific events
    occur.
    """

    #: The connection.
    connection: Connection = dataclasses.field(default_factory=Connection)
    #: The event type.
    event_type: str = ""
    #: The creation time of the trigger.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the trigger.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.connection is not None:
            data["connection"] = Connection.__json_encode__(self.connection)

        if self.event_type is not None:
            data["eventType"] = self.event_type

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Trigger":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("connection") is not None:
            kwargs["connection"] = Connection.__json_decode__(data["connection"])

        if data.get("eventType") is not None:
            kwargs["event_type"] = data["eventType"]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Trigger(**kwargs)
