# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class GetCustomUserRequest:
    """
    Request message for getting a custom user.
    """

    #: The external identifier for the user.
    id: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "GetCustomUserRequest":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        return GetCustomUserRequest(**kwargs)
