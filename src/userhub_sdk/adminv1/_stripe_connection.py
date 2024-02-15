# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class StripeConnection:
    """
    The stripe billing specific connection data.
    """

    #: The Stripe account ID (e.g. `acct_1LcUvxQYGbxD2SPK`)
    account_id: str = ""
    #: The live vs test status for the Stripe account.
    live: bool = False

    def __json_encode__(self):
        data = {}

        if self.account_id is not None:
            data["accountId"] = self.account_id

        if self.live is not None:
            data["live"] = self.live

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("accountId") is not None:
            kwargs["account_id"] = data["accountId"]

        if data.get("live") is not None:
            kwargs["live"] = data["live"]

        return StripeConnection(**kwargs)
