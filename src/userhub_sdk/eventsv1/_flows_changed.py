# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import adminv1
from .._internal import util


@dataclasses.dataclass
class FlowsChanged:
    """
    The flows changed event.
    """

    #: The flow.
    flow: Optional[adminv1.Flow] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("flow") is not None:
            kwargs["flow"] = adminv1.Flow.__json_decode__(data["flow"])

        return FlowsChanged(**kwargs)
