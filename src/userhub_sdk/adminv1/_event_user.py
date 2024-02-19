# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class EventUser:
    """
    The user associated with event.
    """

    #: The system-assigned identifier of the user.
    id: str = ""
    #: The human-readable display name of the user.
    #:
    #: NOTE: this is the current display name and not
    #: the one as of the time of the event.
    display_name: Optional[str] = None
    #: The email address of the user.
    #:
    #: NOTE: this is the current email and not
    #: the one as of the time of the event.
    email: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.email is not None:
            data["email"] = self.email

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "EventUser":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        return EventUser(**kwargs)
