# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import constants, util

from ._plan_group import PlanGroup


@dataclasses.dataclass
class PlanGroupChangePath:
    """
    This defines the upgrade/downgrade paths for a plan group.
    """

    #: The target plan group for this change path.
    target: Optional[PlanGroup] = None
    #: Whether the change is considered an upgrade or
    #: a downgrade.
    direction: str = ""
    #: The visibility of the change path.
    visibility: str = ""
    #: The creation time of the plan group change path.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the plan group change path.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.target is not None:
            data["target"] = PlanGroup.__json_encode__(self.target)

        if self.direction is not None:
            data["direction"] = self.direction

        if self.visibility is not None:
            data["visibility"] = self.visibility

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanGroupChangePath":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("target") is not None:
            kwargs["target"] = PlanGroup.__json_decode__(data["target"])

        if data.get("direction") is not None:
            kwargs["direction"] = data["direction"]

        if data.get("visibility") is not None:
            kwargs["visibility"] = data["visibility"]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return PlanGroupChangePath(**kwargs)
