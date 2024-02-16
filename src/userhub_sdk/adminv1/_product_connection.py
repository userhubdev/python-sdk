# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import constants, util

from ._connection import Connection


@dataclasses.dataclass
class ProductConnection:
    """
    A link between a UserHub product and an external product.
    """

    #: The basic view of the connection.
    connection: Optional[Connection] = None
    #: The external identifier of the connected product.
    external_id: str = ""
    #: The status of the connected product.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The last time the product was pulled from the connection.
    pull_time: Optional[datetime.datetime] = None
    #: The last time the product was pushed to the connection.
    push_time: Optional[datetime.datetime] = None
    #: The creation time of the product connection.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the product connection.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.connection is not None:
            data["connection"] = Connection.__json_encode__(self.connection)

        if self.external_id is not None:
            data["externalId"] = self.external_id

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

        if self.pull_time is not None:
            data["pullTime"] = util.encode_datetime(self.pull_time)

        if self.push_time is not None:
            data["pushTime"] = util.encode_datetime(self.push_time)

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "ProductConnection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("connection") is not None:
            kwargs["connection"] = Connection.__json_decode__(data["connection"])

        if data.get("externalId") is not None:
            kwargs["external_id"] = data["externalId"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

        if data.get("pullTime") is not None:
            kwargs["pull_time"] = util.decode_datetime(data["pullTime"])

        if data.get("pushTime") is not None:
            kwargs["push_time"] = util.decode_datetime(data["pushTime"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return ProductConnection(**kwargs)
