# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class CheckoutDiscount:
    """
    The discount.
    """

    #: The checkout discount identifier.
    id: str = ""
    #: The discount code.
    code: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.code is not None:
            data["code"] = self.code

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CheckoutDiscount":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("code") is not None:
            kwargs["code"] = data["code"]

        return CheckoutDiscount(**kwargs)
