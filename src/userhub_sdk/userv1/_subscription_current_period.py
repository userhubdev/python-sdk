# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import util


@dataclasses.dataclass
class SubscriptionCurrentPeriod:
    """
    Information about the current billing period.
    """

    #: The time the current billing period started.
    start_time: Optional[datetime.datetime] = None
    #: The time the current billing period ends.
    end_time: Optional[datetime.datetime] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.start_time is not None:
            data["startTime"] = util.encode_datetime(self.start_time)

        if self.end_time is not None:
            data["endTime"] = util.encode_datetime(self.end_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "SubscriptionCurrentPeriod":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("startTime") is not None:
            kwargs["start_time"] = util.decode_datetime(data["startTime"])

        if data.get("endTime") is not None:
            kwargs["end_time"] = util.decode_datetime(data["endTime"])

        return SubscriptionCurrentPeriod(**kwargs)
