# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List

from ._organization_result import OrganizationResult


@dataclasses.dataclass
class BatchGetOrganizationsResponse:
    """
    Response message for BatchGetOrganizations.
    """

    #: The organizations.
    organizations: List[OrganizationResult] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.organizations is not None:
            data["organizations"] = [
                OrganizationResult.__json_encode__(v) for v in self.organizations
            ]

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "BatchGetOrganizationsResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("organizations") is not None:
            kwargs["organizations"] = [
                OrganizationResult.__json_decode__(v) for v in data["organizations"]
            ]

        return BatchGetOrganizationsResponse(**kwargs)
