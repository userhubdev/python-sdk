# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class ConnectionProvider:
    """
    The functionality the connection provides (e.g. `BILLING`).
    """

    #: The provider type.
    type: str = ""
    #: Whether the connection is the default for the provider type.
    default: Optional[bool] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.type is not None:
            data["type"] = self.type

        if self.default is not None:
            data["default"] = self.default

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "ConnectionProvider":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("default") is not None:
            kwargs["default"] = data["default"]

        return ConnectionProvider(**kwargs)
