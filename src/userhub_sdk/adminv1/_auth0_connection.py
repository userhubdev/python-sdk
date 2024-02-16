# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


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

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.domain is not None:
            data["domain"] = self.domain

        if self.client_id is not None:
            data["clientId"] = self.client_id

        if self.client_secret is not None:
            data["clientSecret"] = self.client_secret

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Auth0Connection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("domain") is not None:
            kwargs["domain"] = data["domain"]

        if data.get("clientId") is not None:
            kwargs["client_id"] = data["clientId"]

        if data.get("clientSecret") is not None:
            kwargs["client_secret"] = data["clientSecret"]

        return Auth0Connection(**kwargs)
