# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class SubscriptionTrial:
    """
    The trial information for the subscription.
    """

    #: The time the trial started.
    start_time: Optional[datetime.datetime] = None
    #: The time the trial ended/ends.
    end_time: Optional[datetime.datetime] = None
    #: The number of days in the trial.
    #:
    #: This number is rounded to the nearest whole number
    #: of days.
    days: Optional[int] = None
    #: The number of days remaining in the trial.
    #:
    #: This number is rounded down, so will generally be
    #: less than days. It will be zero on the last day
    #: of the trial and null when the trial expires.
    remaining_days: Optional[int] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("startTime") is not None:
            kwargs["start_time"] = util.decode_datetime(data["startTime"])

        if data.get("endTime") is not None:
            kwargs["end_time"] = util.decode_datetime(data["endTime"])

        if data.get("days") is not None:
            kwargs["days"] = data["days"]

        if data.get("remainingDays") is not None:
            kwargs["remaining_days"] = data["remainingDays"]

        return SubscriptionTrial(**kwargs)
