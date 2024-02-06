# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class ConnectionProvider:
    """
    The functionality the connection provides (e.g. `BILLING`).
    """

    #: The provider type.
    type: str = ""
    #: Whether the connection is the default for the provider type.
    default: Optional[bool] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("default") is not None:
            kwargs["default"] = data["default"]

        return ConnectionProvider(**kwargs)
