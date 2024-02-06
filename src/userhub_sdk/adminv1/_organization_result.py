# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .. import apiv1
from .._internal import util
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

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("organization") is not None:
            kwargs["organization"] = Organization.__json_decode__(data["organization"])

        if data.get("error") is not None:
            kwargs["error"] = apiv1.Status.__json_decode__(data["error"])

        return OrganizationResult(**kwargs)
