# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import constants, util

from ._plan_group_revision import PlanGroupRevision
from ._plan_group_trial import PlanGroupTrial


@dataclasses.dataclass
class PlanGroup:
    """
    Plan group is a container for plan revisions and billing
    intervals.

    A plan group would generally describe a tier of plans offered
    (e.g. Pro) which might contain two options, a monthly and
    yearly plan.
    """

    #: The system-assigned identifier of the plan group.
    id: str = ""
    #: The client defined unique identifier of the plan group (e.g. `pro`).
    #:
    #: It is restricted to letters, numbers, underscores, and hyphens,
    #: with the first character a letter or a number, and a 255
    #: character maximum.
    #:
    #: ID's starting with `pg_r are reserved.
    unique_id: Optional[str] = None
    #: The customer facing human-readable display name of the plan group.
    #:
    #: The maximum length is 200 characters.
    display_name: str = ""
    #: The admin facing description of the plan group.
    #:
    #: The maximum length is 1000 characters.
    description: Optional[str] = None
    #: The type of account the plan can be activated for.
    account_type: str = ""
    #: The trial settings.
    trial: Optional[PlanGroupTrial] = None
    #: The visibility of the plan group.
    visibility: str = ""
    #: The archived status of the plan group.
    archived: bool = False
    #: The current revision for the plan group.
    revision: Optional[PlanGroupRevision] = None
    #: The creation time of the plan group.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the plan group.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.unique_id is not None:
            data["uniqueId"] = self.unique_id

        if self.display_name is not None:
            data["displayName"] = self.display_name

        if self.description is not None:
            data["description"] = self.description

        if self.account_type is not None:
            data["accountType"] = self.account_type

        if self.trial is not None:
            data["trial"] = PlanGroupTrial.__json_encode__(self.trial)

        if self.visibility is not None:
            data["visibility"] = self.visibility

        if self.archived is not None:
            data["archived"] = self.archived

        if self.revision is not None:
            data["revision"] = PlanGroupRevision.__json_encode__(self.revision)

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanGroup":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("accountType") is not None:
            kwargs["account_type"] = data["accountType"]

        if data.get("trial") is not None:
            kwargs["trial"] = PlanGroupTrial.__json_decode__(data["trial"])

        if data.get("visibility") is not None:
            kwargs["visibility"] = data["visibility"]

        if data.get("archived") is not None:
            kwargs["archived"] = data["archived"]

        if data.get("revision") is not None:
            kwargs["revision"] = PlanGroupRevision.__json_decode__(data["revision"])

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return PlanGroup(**kwargs)
