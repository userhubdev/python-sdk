# Code generated. DO NOT EDIT.

import dataclasses


@dataclasses.dataclass
class EventApiKey:
    """
    The API key associated with event.
    """

    #: The system-assigned identifier of the API key.
    id: str = ""

    def __json_encode__(self):
        data = {}

        if self.id is not None:
            data["id"] = self.id

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        return EventApiKey(**kwargs)
