# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class UpdateSubscriptionItemsRequestItem:
    """
    The subscription items.
    """

    #: The product identifier.
    #:
    #: If this is empty and the user ID is set, the default
    #: seat will be used.
    product_id: Optional[str] = None
    #: The member user ID of the organization member. This can
    #: only be specified for seat items.
    user_id: Optional[str] = None
    #: The quantity for the item.
    #:
    #: If this is `0` the item will be removed.
    quantity: Optional[int] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("productId") is not None:
            kwargs["product_id"] = data["productId"]

        if data.get("userId") is not None:
            kwargs["user_id"] = data["userId"]

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        return UpdateSubscriptionItemsRequestItem(**kwargs)
