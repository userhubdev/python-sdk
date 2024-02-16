# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import apiv1

from ._organization import Organization


@dataclasses.dataclass
class OrganizationResult:
    """
    Result wrapper for an organization.
    """

    #: The organization.
    organization: Optional[Organization] = None
    #: The organization error.
    error: Optional[apiv1.Status] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.organization is not None:
            data["organization"] = Organization.__json_encode__(self.organization)

        if self.error is not None:
            data["error"] = apiv1.Status.__json_encode__(self.error)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "OrganizationResult":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("organization") is not None:
            kwargs["organization"] = Organization.__json_decode__(data["organization"])

        if data.get("error") is not None:
            kwargs["error"] = apiv1.Status.__json_decode__(data["error"])

        return OrganizationResult(**kwargs)
