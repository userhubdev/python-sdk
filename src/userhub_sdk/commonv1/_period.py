# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class Period:
    """
    A period of time.
    """

    #: The start time.
    start_time: Optional[datetime.datetime] = None
    #: The end time.
    end_time: Optional[datetime.datetime] = None

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

        return Period(**kwargs)
