# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class OperationInfo:
    """
    Operations metadata.
    """

    #: The message name of the primary return type for this operation.
    response_type: Optional[str] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("responseType") is not None:
            kwargs["response_type"] = data["responseType"]

        return OperationInfo(**kwargs)
