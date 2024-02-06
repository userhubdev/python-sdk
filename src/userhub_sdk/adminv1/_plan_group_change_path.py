# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import constants
from .._internal import util
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
    direction: Optional[str] = None
    #: The visibility of the change path.
    visibility: Optional[str] = None
    #: The creation time of the plan group change path.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the plan group change path.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

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
