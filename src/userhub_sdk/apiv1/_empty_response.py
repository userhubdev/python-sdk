# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class EmptyResponse:
    """
    Empty response.
    """

    def __json_encode__(self):
        data = {}

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        return EmptyResponse(**kwargs)
