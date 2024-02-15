# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from userhub_sdk import apiv1

from ._trigger import Trigger


@dataclasses.dataclass
class TriggerResult:
    """
    Result wrapper for a trigger.
    """

    #: The trigger.
    trigger: Optional[Trigger] = None
    #: The trigger error.
    error: Optional[apiv1.Status] = None

    def __json_encode__(self):
        data = {}

        if self.trigger is not None:
            data["trigger"] = Trigger.__json_encode__(self.trigger)

        if self.error is not None:
            data["error"] = apiv1.Status.__json_encode__(self.error)

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("trigger") is not None:
            kwargs["trigger"] = Trigger.__json_decode__(data["trigger"])

        if data.get("error") is not None:
            kwargs["error"] = apiv1.Status.__json_decode__(data["error"])

        return TriggerResult(**kwargs)
