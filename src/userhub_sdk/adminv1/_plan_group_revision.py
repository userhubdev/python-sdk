# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import constants, util

from ._plan_group_revision_item import PlanGroupRevisionItem
from ._plan_group_revision_plan import PlanGroupRevisionPlan


@dataclasses.dataclass
class PlanGroupRevision:
    """
    Plan group revisions track the configuration options for a plan group.
    """

    #: The system-assigned identifier of the plan group revision.
    id: str = ""
    #: The default status of the revision.
    #:
    #: When this is true, the revision will be used as the default when not
    #: explicitly specified.
    default: bool = False
    #: The supported currency codes (e.g. `USD`).
    currency_codes: List[str] = dataclasses.field(default_factory=list)
    #: The plans associated with plan group revision.
    plans: Optional[List[PlanGroupRevisionPlan]] = dataclasses.field(
        default_factory=list
    )
    #: The items associated with plan group revision.
    items: Optional[List[PlanGroupRevisionItem]] = dataclasses.field(
        default_factory=list
    )
    #: Whether the revision has been committed.
    #:
    #: After the revision has been committed, it is available for use, but
    #: can no longer be edited.
    committed: bool = False
    #: The tags associated with the revision.
    #:
    #: Tags are restricted to letters, numbers, underscores, and hyphens,
    #: with the first character a letter or a number, and a 255
    #: character maximum.
    #:
    #: A revision is limited to 10 tags.
    tags: List[str] = dataclasses.field(default_factory=list)
    #: The revised plan group revision identifier.
    #:
    #: This allows you to track the revision lineage.
    source_revision_id: Optional[str] = None
    #: The creation time of the plan group revision.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the plan group revision.
    update_time: datetime.datetime = constants.EMPTY_DATETIME

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.default is not None:
            data["default"] = self.default

        if self.currency_codes is not None:
            data["currencyCodes"] = self.currency_codes

        if self.plans is not None:
            data["plans"] = [
                PlanGroupRevisionPlan.__json_encode__(v) for v in self.plans
            ]

        if self.items is not None:
            data["items"] = [
                PlanGroupRevisionItem.__json_encode__(v) for v in self.items
            ]

        if self.committed is not None:
            data["committed"] = self.committed

        if self.tags is not None:
            data["tags"] = self.tags

        if self.source_revision_id is not None:
            data["sourceRevisionId"] = self.source_revision_id

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PlanGroupRevision":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("default") is not None:
            kwargs["default"] = data["default"]

        if data.get("currencyCodes") is not None:
            kwargs["currency_codes"] = data["currencyCodes"]

        if data.get("plans") is not None:
            kwargs["plans"] = [
                PlanGroupRevisionPlan.__json_decode__(v) for v in data["plans"]
            ]

        if data.get("items") is not None:
            kwargs["items"] = [
                PlanGroupRevisionItem.__json_decode__(v) for v in data["items"]
            ]

        if data.get("committed") is not None:
            kwargs["committed"] = data["committed"]

        if data.get("tags") is not None:
            kwargs["tags"] = data["tags"]

        if data.get("sourceRevisionId") is not None:
            kwargs["source_revision_id"] = data["sourceRevisionId"]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return PlanGroupRevision(**kwargs)
