# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.ip_address is not None:
            data["ipAddress"] = self.ip_address

        if self.trace_id is not None:
            data["traceId"] = self.trace_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "EventRequest":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("ipAddress") is not None:
            kwargs["ip_address"] = data["ipAddress"]

        if data.get("traceId") is not None:
            kwargs["trace_id"] = data["traceId"]

        return EventRequest(**kwargs)
