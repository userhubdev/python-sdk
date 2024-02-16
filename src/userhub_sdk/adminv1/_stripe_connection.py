# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class StripeConnection:
    """
    The stripe billing specific connection data.
    """

    #: The Stripe account ID (e.g. `acct_1LcUvxQYGbxD2SPK`)
    account_id: str = ""
    #: The live vs test status for the Stripe account.
    live: bool = False

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.account_id is not None:
            data["accountId"] = self.account_id

        if self.live is not None:
            data["live"] = self.live

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "StripeConnection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("accountId") is not None:
            kwargs["account_id"] = data["accountId"]

        if data.get("live") is not None:
            kwargs["live"] = data["live"]

        return StripeConnection(**kwargs)
