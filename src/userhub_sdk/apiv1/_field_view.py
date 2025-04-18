# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class FieldView:
    """
    The field view options..
    """

    #: Whether the field is included in the view.
    #:
    #: THis overrides the message default.
    include: str = ""
    #: Whether the field is excluded from the view.
    #:
    #: THis overrides the message default.
    exclude: str = ""
    #: The referenced type's view.
    type: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.include is not None:
            data["include"] = self.include

        if self.exclude is not None:
            data["exclude"] = self.exclude

        if self.type is not None:
            data["type"] = self.type

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "FieldView":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("include") is not None:
            kwargs["include"] = data["include"]

        if data.get("exclude") is not None:
            kwargs["exclude"] = data["exclude"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        return FieldView(**kwargs)
