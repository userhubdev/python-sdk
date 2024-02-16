# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class DeleteCustomUserRequest:
    """
    Request message for deleting a custom user.
    """

    #: The external identifier for the user.
    id: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "DeleteCustomUserRequest":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        return DeleteCustomUserRequest(**kwargs)
