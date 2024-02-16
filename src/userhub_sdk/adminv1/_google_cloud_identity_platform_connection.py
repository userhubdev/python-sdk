# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.credentials is not None:
            data["credentials"] = self.credentials

        if self.project_id is not None:
            data["projectId"] = self.project_id

        return data

    @staticmethod
    def __json_decode__(
        data: Dict[str, Any],
    ) -> "GoogleCloudIdentityPlatformConnection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("credentials") is not None:
            kwargs["credentials"] = data["credentials"]

        if data.get("projectId") is not None:
            kwargs["project_id"] = data["projectId"]

        return GoogleCloudIdentityPlatformConnection(**kwargs)
