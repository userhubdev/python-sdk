# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class OperationInfo:
    """
    Operations metadata.
    """

    #: The message name of the primary return type for this operation.
    response_type: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.response_type is not None:
            data["responseType"] = self.response_type

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "OperationInfo":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("responseType") is not None:
            kwargs["response_type"] = data["responseType"]

        return OperationInfo(**kwargs)
