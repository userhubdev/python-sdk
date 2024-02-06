# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class PlanGroupTrial:
    """
    The trial settings.
    """

    #: The default number of days in the trial.
    days: Optional[int] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("days") is not None:
            kwargs["days"] = data["days"]

        return PlanGroupTrial(**kwargs)
