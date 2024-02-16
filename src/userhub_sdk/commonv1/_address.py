# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional


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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.lines is not None:
            data["lines"] = self.lines

        if self.city is not None:
            data["city"] = self.city

        if self.state is not None:
            data["state"] = self.state

        if self.postal_code is not None:
            data["postalCode"] = self.postal_code

        if self.country is not None:
            data["country"] = self.country

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Address":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

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
