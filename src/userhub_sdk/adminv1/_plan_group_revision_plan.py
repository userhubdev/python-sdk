# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .. import commonv1
from .._internal import util
from ._connection import Connection
from ._price import Price


@dataclasses.dataclass
class PlanGroupRevisionPlan:
    """
    The actual plan within the plan group. This defines the associated
    connection and billing interval.
    """

    #: The client defined unique identifier for the plan (e.g. `monthly`).
    unique_id: Optional[str] = None
    #: The details of the associated connection.
    connection: Optional[Connection] = None
    #: The billing interval for the plan.
    interval: Optional[commonv1.Interval] = None
    #: The customer facing human-readable display name for the plan.
    display_name: Optional[str] = None
    #: The admin facing description of the plan.
    #:
    #: The maximum length is 1000 characters.
    description: Optional[str] = None
    #: The prices associated with the plan.
    #:
    #: There should be a price for each product/currency
    #: combination.
    prices: Optional[List[Price]] = dataclasses.field(default_factory=list)
    #: The visibility of the plan.
    visibility: Optional[str] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("connection") is not None:
            kwargs["connection"] = Connection.__json_decode__(data["connection"])

        if data.get("interval") is not None:
            kwargs["interval"] = commonv1.Interval.__json_decode__(data["interval"])

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        if data.get("description") is not None:
            kwargs["description"] = data["description"]

        if data.get("prices") is not None:
            kwargs["prices"] = [Price.__json_decode__(v) for v in data["prices"]]

        if data.get("visibility") is not None:
            kwargs["visibility"] = data["visibility"]

        return PlanGroupRevisionPlan(**kwargs)
