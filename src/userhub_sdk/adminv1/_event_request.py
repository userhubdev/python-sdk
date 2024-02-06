# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class EventRequest:
    """
    The request associated with event.
    """

    #: The IP address of the client/user.
    #:
    #: It's very likely this is the IP address of the
    #: API client and not the end-user.
    ip_address: Optional[str] = None
    #: The trace ID associated with the request.
    trace_id: Optional[str] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("ipAddress") is not None:
            kwargs["ip_address"] = data["ipAddress"]

        if data.get("traceId") is not None:
            kwargs["trace_id"] = data["traceId"]

        return EventRequest(**kwargs)
