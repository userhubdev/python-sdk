# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class EventConnection:
    """
    The connection associated with the event.
    """

    #: The system-assigned identifier of the connection.
    id: str = ""
    #: The human-readable display name of the connection.
    #:
    #: NOTE: this is the current display name and not
    #: the one as of the time of the event.
    display_name: Optional[str] = None
    #: The connection type.
    type: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.type is not None:
            data["type"] = self.type

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "EventConnection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        return EventConnection(**kwargs)
