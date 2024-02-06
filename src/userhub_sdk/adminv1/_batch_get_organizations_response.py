# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util
from ._organization_result import OrganizationResult


@dataclasses.dataclass
class BatchGetOrganizationsResponse:
    """
    Response message for BatchGetOrganizations.
    """

    #: The organizations.
    organizations: Optional[List[OrganizationResult]] = dataclasses.field(
        default_factory=list
    )

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("organizations") is not None:
            kwargs["organizations"] = [
                OrganizationResult.__json_decode__(v) for v in data["organizations"]
            ]

        return BatchGetOrganizationsResponse(**kwargs)
