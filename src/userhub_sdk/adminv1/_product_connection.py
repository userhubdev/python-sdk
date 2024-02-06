# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import constants
from .._internal import util
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

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

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
