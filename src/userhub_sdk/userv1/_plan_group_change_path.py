# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class PlanGroupChangePath:
    """
    The change path.
    """

    #: Whether the change is considered an upgrade or
    #: a downgrade.
    direction: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.direction is not None:
            data["direction"] = self.direction

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("direction") is not None:
            kwargs["direction"] = data["direction"]

        return PlanGroupChangePath(**kwargs)
