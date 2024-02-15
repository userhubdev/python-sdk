# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional


@dataclasses.dataclass
class PlanGroupTrial:
    """
    The trial settings.
    """

    #: The number of days in the trial.
    days: Optional[int] = None

    def __json_encode__(self):
        data = {}

        if self.days is not None:
            data["days"] = self.days

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("days") is not None:
            kwargs["days"] = data["days"]

        return PlanGroupTrial(**kwargs)
