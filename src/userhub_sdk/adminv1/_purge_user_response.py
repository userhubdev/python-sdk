# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class PurgeUserResponse:
    """
    Response message for PurgeUser.
    """

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PurgeUserResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        return PurgeUserResponse(**kwargs)
