# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class MessageView:
    """
    The message view options.
    """

    #: Whether all fields are included in the view by default.
    include: str = ""
    #: Whether all fields are excluded from the view by default.
    exclude: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.include is not None:
            data["include"] = self.include

        if self.exclude is not None:
            data["exclude"] = self.exclude

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "MessageView":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("include") is not None:
            kwargs["include"] = data["include"]

        if data.get("exclude") is not None:
            kwargs["exclude"] = data["exclude"]

        return MessageView(**kwargs)
