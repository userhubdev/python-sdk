# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional

from .._internal import util


@dataclasses.dataclass
class Auth0Connection:
    """
    The Auth0 connection data.
    """

    #: The Auth0 domain.
    domain: str = ""
    #: The Auth0 client ID.
    client_id: str = ""
    #: The Auth0 client secret.
    client_secret: str = ""

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("domain") is not None:
            kwargs["domain"] = data["domain"]

        if data.get("clientId") is not None:
            kwargs["client_id"] = data["clientId"]

        if data.get("clientSecret") is not None:
            kwargs["client_secret"] = data["clientSecret"]

        return Auth0Connection(**kwargs)
