# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict


@dataclasses.dataclass
class CreatePortalSessionResponse:
    """
    Response message for CreatePortalSession.
    """

    #: The URL you should redirect the user to after calling create portal
    #: session.
    redirect_url: str = ""

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.redirect_url is not None:
            data["redirectUrl"] = self.redirect_url

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "CreatePortalSessionResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("redirectUrl") is not None:
            kwargs["redirect_url"] = data["redirectUrl"]

        return CreatePortalSessionResponse(**kwargs)
