# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional


@dataclasses.dataclass
class OperationInfo:
    """
    Operations metadata.
    """

    #: The message name of the primary return type for this operation.
    response_type: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.response_type is not None:
            data["responseType"] = self.response_type

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("responseType") is not None:
            kwargs["response_type"] = data["responseType"]

        return OperationInfo(**kwargs)
