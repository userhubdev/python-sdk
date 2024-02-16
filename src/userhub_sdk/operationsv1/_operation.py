# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk import commonv1
from userhub_sdk._internal import constants, util

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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.done is not None:
            data["done"] = self.done

        if self.error is not None:
            data["error"] = OperationError.__json_encode__(self.error)

        if self.response is not None:
            data["response"] = commonv1.Any.__json_encode__(self.response)

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        if self.delete_time is not None:
            data["deleteTime"] = util.encode_datetime(self.delete_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Operation":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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
