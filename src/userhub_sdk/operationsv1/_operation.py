# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .. import commonv1
from .._internal import constants
from .._internal import util
from ._operation_error import OperationError


@dataclasses.dataclass
class Operation:
    """
    Operation is a long running background task.
    """

    #: The system-assigned identifier of the operation.
    id: str = ""
    #: If the value is `false`, it means the operation is still in progress.
    #: If `true`, the operation is completed, and either `error` or `response` is
    #: available.
    done: bool = False
    #: The error result of the operation in case of failure.
    error: Optional[OperationError] = None
    #: The normal response of the operation in case of success.
    response: Optional[commonv1.Any] = None
    #: The creation time of the operation.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the operation.
    update_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The deletion time of the operation.
    delete_time: Optional[datetime.datetime] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("done") is not None:
            kwargs["done"] = data["done"]

        if data.get("error") is not None:
            kwargs["error"] = OperationError.__json_decode__(data["error"])

        if data.get("response") is not None:
            kwargs["response"] = commonv1.Any.__json_decode__(data["response"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        if data.get("deleteTime") is not None:
            kwargs["delete_time"] = util.decode_datetime(data["deleteTime"])

        return Operation(**kwargs)
