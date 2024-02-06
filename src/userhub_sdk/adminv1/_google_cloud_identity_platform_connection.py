# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class GoogleCloudIdentityPlatformConnection:
    """
    The Google Cloud Identity Platform/Firebase specific connection data.
    """

    #: The service account key in JSON format.
    credentials: str = ""
    #: The Google Cloud Identity Platform/Firebase project ID.
    #:
    #: This will default to the project ID in the service account key if
    #: not specified.
    project_id: Optional[str] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("credentials") is not None:
            kwargs["credentials"] = data["credentials"]

        if data.get("projectId") is not None:
            kwargs["project_id"] = data["projectId"]

        return GoogleCloudIdentityPlatformConnection(**kwargs)
