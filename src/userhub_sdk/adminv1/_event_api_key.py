# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class EventApiKey:
    """
    The API key associated with event.
    """

    #: The system-assigned identifier of the API key.
    id: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "EventApiKey":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        return EventApiKey(**kwargs)
