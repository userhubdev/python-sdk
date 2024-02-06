# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util
from ._product import Product


@dataclasses.dataclass
class PlanGroupRevisionItem:
    """
    The products which the plan group includes.
    """

    #: The product associated with the item.
    product: Optional[Product] = None
    #: The plan item type.
    type: str = ""

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("product") is not None:
            kwargs["product"] = Product.__json_decode__(data["product"])

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        return PlanGroupRevisionItem(**kwargs)
