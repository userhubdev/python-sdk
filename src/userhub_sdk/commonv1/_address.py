# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class Address:
    """
    A postal address (billing, mailing, etc...).
    """

    #: The address lines.
    lines: List[str] = dataclasses.field(default_factory=list)
    #: The city, district, suburb, town, or village.
    city: Optional[str] = None
    #: The state, country, province, or region.
    state: Optional[str] = None
    #: The ZIP or postal code.
    postal_code: Optional[str] = None
    #: The 2-letter country code.
    country: Optional[str] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("lines") is not None:
            kwargs["lines"] = data["lines"]

        if data.get("city") is not None:
            kwargs["city"] = data["city"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("postalCode") is not None:
            kwargs["postal_code"] = data["postalCode"]

        if data.get("country") is not None:
            kwargs["country"] = data["country"]

        return Address(**kwargs)
