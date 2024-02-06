# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class Challenge:
    """
    A challenge issued by webhooks to validate the
    endpoint is working correctly.
    """

    #: The challenge string.
    challenge: Optional[str] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("challenge") is not None:
            kwargs["challenge"] = data["challenge"]

        return Challenge(**kwargs)
