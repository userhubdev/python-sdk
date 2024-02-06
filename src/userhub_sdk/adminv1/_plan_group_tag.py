# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class PlanGroupTag:
    """
    A tag which references a specific plan group revision.
    """

    #: The client defined tag (e.g. `2023`).
    tag: str = ""
    #: The system-assigned identifier of the plan group revision.
    revision_id: str = ""

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("tag") is not None:
            kwargs["tag"] = data["tag"]

        if data.get("revisionId") is not None:
            kwargs["revision_id"] = data["revisionId"]

        return PlanGroupTag(**kwargs)
