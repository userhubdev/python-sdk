# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class EventActor:
    """
    The actor associated with event.
    """

    #: The system-assigned identifier of the actor.
    id: Optional[str] = None
    #: The human-readable display name of the actor.
    #:
    #: NOTE: this is the current display name and not
    #: the one as of the time of the event.
    display_name: Optional[str] = None
    #: The email address of the actor.
    #:
    #: NOTE: this is the current email and not
    #: the one as of the time of the event.
    email: Optional[str] = None
    #: Whether the actor is a tenant admin.
    admin: Optional[bool] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("email") is not None:
            kwargs["email"] = data["email"]

        if data.get("admin") is not None:
            kwargs["admin"] = data["admin"]

        return EventActor(**kwargs)
