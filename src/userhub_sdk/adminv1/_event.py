# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Optional

from .._internal import constants
from .._internal import util
from ._event_actor import EventActor
from ._event_api_key import EventApiKey
from ._event_connection import EventConnection
from ._event_entity import EventEntity
from ._event_organization import EventOrganization
from ._event_request import EventRequest
from ._event_user import EventUser


@dataclasses.dataclass
class Event:
    """
    Event describes a service a tenant provides. Multiple
    events can be multiple and sold using a plan.
    """

    #: The system-assigned identifier of the event.
    id: str = ""
    #: The type of the event.
    type: str = ""
    #: The time of the event.
    time: datetime.datetime = constants.EMPTY_DATETIME
    #: The entity associated with the event.
    entity: Optional[EventEntity] = None
    #: The connection associated with the event.
    connection: Optional[EventConnection] = None
    #: The organization associated with the event.
    organization: Optional[EventOrganization] = None
    #: The user associated with the event.
    user: Optional[EventUser] = None
    #: The API key associated with the event.
    api_key: Optional[EventApiKey] = None
    #: The actor associated with the event.
    actor: Optional[EventActor] = None
    #: The request associated with the event.
    request: Optional[EventRequest] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("time") is not None:
            kwargs["time"] = util.decode_datetime(data["time"])

        if data.get("entity") is not None:
            kwargs["entity"] = EventEntity.__json_decode__(data["entity"])

        if data.get("connection") is not None:
            kwargs["connection"] = EventConnection.__json_decode__(data["connection"])

        if data.get("organization") is not None:
            kwargs["organization"] = EventOrganization.__json_decode__(
                data["organization"]
            )

        if data.get("user") is not None:
            kwargs["user"] = EventUser.__json_decode__(data["user"])

        if data.get("apiKey") is not None:
            kwargs["api_key"] = EventApiKey.__json_decode__(data["apiKey"])

        if data.get("actor") is not None:
            kwargs["actor"] = EventActor.__json_decode__(data["actor"])

        if data.get("request") is not None:
            kwargs["request"] = EventRequest.__json_decode__(data["request"])

        return Event(**kwargs)
