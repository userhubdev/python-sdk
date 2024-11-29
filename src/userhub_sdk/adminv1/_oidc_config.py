# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class OidcConfig:
    """
    OpenID Connect (OIDC) configuration.
    """

    #: The issuer URL.
    issuer_url: str = ""
    #: The client ID.
    client_id: str = ""
    #: The client secret.
    client_secret: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.issuer_url is not None:
            data["issuerUrl"] = self.issuer_url

        if self.client_id is not None:
            data["clientId"] = self.client_id

        if self.client_secret is not None:
            data["clientSecret"] = self.client_secret

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "OidcConfig":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("issuerUrl") is not None:
            kwargs["issuer_url"] = data["issuerUrl"]

        if data.get("clientId") is not None:
            kwargs["client_id"] = data["clientId"]

        if data.get("clientSecret") is not None:
            kwargs["client_secret"] = data["clientSecret"]

        return OidcConfig(**kwargs)
