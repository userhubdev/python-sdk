# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class Product:
    """
    The product.
    """

    #: The system-assigned identifier of the product.
    id: str = ""
    #: The client defined unique identifier of the product.
    unique_id: Optional[str] = None
    #: The human-readable display name of the product.
    display_name: str = ""

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("uniqueId") is not None:
            kwargs["unique_id"] = data["uniqueId"]

        if data.get("displayName") is not None:
            kwargs["display_name"] = data["displayName"]

        return Product(**kwargs)
