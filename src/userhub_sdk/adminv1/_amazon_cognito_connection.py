# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional

from ._oidc_config import OidcConfig


@dataclasses.dataclass
class AmazonCognitoConnection:
    """
    The Amazon Cognito connection data.
    """

    #: The Amazon Cognito user pool ID.
    user_pool_id: str = ""
    #: The Amazon region.
    region: str = ""
    #: The Amazon access key ID.
    access_key_id: str = ""
    #: The Amazon access key secret.
    access_key_secret: str = ""
    #: OpenID Connect (OIDC) configuration.
    #:
    #: If configured, this can be used instead of implementing a
    #: Portal callback.
    oidc: Optional[OidcConfig] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.user_pool_id is not None:
            data["userPoolId"] = self.user_pool_id

        if self.region is not None:
            data["region"] = self.region

        if self.access_key_id is not None:
            data["accessKeyId"] = self.access_key_id

        if self.access_key_secret is not None:
            data["accessKeySecret"] = self.access_key_secret

        if self.oidc is not None:
            data["oidc"] = OidcConfig.__json_encode__(self.oidc)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "AmazonCognitoConnection":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("userPoolId") is not None:
            kwargs["user_pool_id"] = data["userPoolId"]

        if data.get("region") is not None:
            kwargs["region"] = data["region"]

        if data.get("accessKeyId") is not None:
            kwargs["access_key_id"] = data["accessKeyId"]

        if data.get("accessKeySecret") is not None:
            kwargs["access_key_secret"] = data["accessKeySecret"]

        if data.get("oidc") is not None:
            kwargs["oidc"] = OidcConfig.__json_decode__(data["oidc"])

        return AmazonCognitoConnection(**kwargs)
