# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class UpdateSubscriptionItemsRequestItem:
    """
    The subscription items.
    """

    #: The product identifier.
    #:
    #: If this is empty and the user ID is set, the default
    #: seat will be used.
    product_id: str = ""
    #: The member user ID of the organization member. This can
    #: only be specified for seat items.
    user_id: Optional[str] = None
    #: The quantity for the item.
    #:
    #: If this is `0` the item will be removed.
    quantity: Optional[int] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.product_id is not None:
            data["productId"] = self.product_id

        if self.user_id is not None:
            data["userId"] = self.user_id

        if self.quantity is not None:
            data["quantity"] = self.quantity

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "UpdateSubscriptionItemsRequestItem":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("productId") is not None:
            kwargs["product_id"] = data["productId"]

        if data.get("userId") is not None:
            kwargs["user_id"] = data["userId"]

        if data.get("quantity") is not None:
            kwargs["quantity"] = data["quantity"]

        return UpdateSubscriptionItemsRequestItem(**kwargs)
