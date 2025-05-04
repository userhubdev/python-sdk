# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from userhub_sdk import commonv1


@dataclasses.dataclass
class PaymentMethodInput:
    """
    Payment method input parameters.
    """

    #: The full name of the owner of the payment method (e.g. `Jane Doe`).
    full_name: Optional[str] = None
    #: The address for the payment method.
    address: Optional[commonv1.Address] = None
    #: The card expiration year (e.g. `2030`).
    exp_year: Optional[int] = None
    #: The card expiration month (e.g. `12`).
    exp_month: Optional[int] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.full_name is not None:
            data["fullName"] = self.full_name

        if self.address is not None:
            data["address"] = commonv1.Address.__json_encode__(self.address)

        if self.exp_year is not None:
            data["expYear"] = self.exp_year

        if self.exp_month is not None:
            data["expMonth"] = self.exp_month

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "PaymentMethodInput":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("fullName") is not None:
            kwargs["full_name"] = data["fullName"]

        if data.get("address") is not None:
            kwargs["address"] = commonv1.Address.__json_decode__(data["address"])

        if data.get("expYear") is not None:
            kwargs["exp_year"] = data["expYear"]

        if data.get("expMonth") is not None:
            kwargs["exp_month"] = data["expMonth"]

        return PaymentMethodInput(**kwargs)
