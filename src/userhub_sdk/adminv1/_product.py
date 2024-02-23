# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

from userhub_sdk._internal import constants, util

from ._product_connection import ProductConnection


@dataclasses.dataclass
class Product:
    """
    Product describes a service a tenant provides.
    """

    #: The system-assigned identifier of the product.
    id: str = ""
    #: The client defined unique identifier of the product.
    #:
    #: It is restricted to letters, numbers, underscores, and hyphens,
    #: with the first character a letter or a number, and a 255
    #: character maximum.
    #:
    #: ID's starting with `pd_` are reserved.
    unique_id: Optional[str] = None
    #: The customer facing human-readable display name of the product.
    #:
    #: The maximum length is 200 characters.
    display_name: str = ""
    #: The public description of the product.
    #:
    #: The maximum length is 1000 characters.
    description: Optional[str] = None
    #: Whether the price has been committed.
    #:
    #: This is automatically set the first time the product is used
    #: in a plan.
    committed: bool = False
    #: The archived status of the product.
    #:
    #: It determines if the product can be activated by self-serve plans.
    archived: bool = False
    #: The connected products.
    product_connections: Optional[List[ProductConnection]] = dataclasses.field(
        default_factory=list
    )
    #: The creation time of the product.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the product.
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

        if self.committed is not None:
            data["committed"] = self.committed

        if self.archived is not None:
            data["archived"] = self.archived

        if self.product_connections is not None:
            data["productConnections"] = [
                ProductConnection.__json_encode__(v) for v in self.product_connections
            ]

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Product":
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

        if data.get("committed") is not None:
            kwargs["committed"] = data["committed"]

        if data.get("archived") is not None:
            kwargs["archived"] = data["archived"]

        if data.get("productConnections") is not None:
            kwargs["product_connections"] = [
                ProductConnection.__json_decode__(v) for v in data["productConnections"]
            ]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        return Product(**kwargs)
