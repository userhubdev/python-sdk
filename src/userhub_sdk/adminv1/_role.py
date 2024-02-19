# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import constants, util


@dataclasses.dataclass
class Role:
    """
    A member's role within an organization.
    """

    #: The system-assigned identifier of the role.
    id: str = ""
    #: The client defined unique identifier of the role.
    #:
    #: It is restricted to letters, numbers, underscores, and hyphens,
    #: with the first character a letter or a number, and a 255
    #: character maximum.
    #:
    #: ID's starting with `role_` are reserved.
    unique_id: str = ""
    #: The human-readable display name of the role.
    display_name: str = ""
    #: The role type.
    type: str = ""
    #: The description of the role.
    #:
    #: The maximum length is 1000 characters.
    description: Optional[str] = None
    #: The additional permissions allowed by the role.
    permission_sets: List[str] = dataclasses.field(default_factory=list)
    #: Whether the role is the default for the tenant.
    default: Optional[bool] = None
    #: The archived status of the role.
    archived: Optional[bool] = None
    #: The creation time of the role.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the role.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.type is not None:
            data["type"] = self.type

        if self.description is not None:
            data["description"] = self.description

        if self.permission_sets is not None:
            data["permissionSets"] = self.permission_sets

        if self.default is not None:
            data["default"] = self.default

        if self.archived is not None:
            data["archived"] = self.archived

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Role":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("permissionSets") is not None:
            kwargs["permission_sets"] = data["permissionSets"]

        if data.get("default") is not None:
            kwargs["default"] = data["default"]

        if data.get("archived") is not None:
            kwargs["archived"] = data["archived"]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Role(**kwargs)
