# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class PlanGroupTag:
    """
    A tag which references a specific plan group revision.
    """

    #: The client defined tag (e.g. `2023`).
    tag: str = ""
    #: The system-assigned identifier of the plan group revision.
    revision_id: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.tag is not None:
            data["tag"] = self.tag

        if self.revision_id is not None:
            data["revisionId"] = self.revision_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanGroupTag":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("tag") is not None:
            kwargs["tag"] = data["tag"]

        if data.get("revisionId") is not None:
            kwargs["revision_id"] = data["revisionId"]

        return PlanGroupTag(**kwargs)
