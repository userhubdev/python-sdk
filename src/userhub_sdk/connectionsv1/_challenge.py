# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class Challenge:
    """
    A challenge issued by webhooks to validate the
    endpoint is working correctly.
    """

    #: The challenge string.
    challenge: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.challenge is not None:
            data["challenge"] = self.challenge

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Challenge":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("challenge") is not None:
            kwargs["challenge"] = data["challenge"]

        return Challenge(**kwargs)
