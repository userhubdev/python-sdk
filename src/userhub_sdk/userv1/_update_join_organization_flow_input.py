# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class UpdateJoinOrganizationFlowInput:
    """
    Input message for UpdateJoinOrganizationFlow.
    """

    #: The identifier of the role.
    role_id: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.role_id is not None:
            data["roleId"] = self.role_id

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "UpdateJoinOrganizationFlowInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("roleId") is not None:
            kwargs["role_id"] = data["roleId"]

        return UpdateJoinOrganizationFlowInput(**kwargs)
