# Code generated. DO NOT EDIT.

import dataclasses
from typing import Optional


@dataclasses.dataclass
class CreatePortalSessionResponse:
    """
    Response message for CreatePortalSession.
    """

    #: The URL you should redirect the user to after calling create portal
    #: session.
    redirect_url: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.redirect_url is not None:
            data["redirectUrl"] = self.redirect_url

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("redirectUrl") is not None:
            kwargs["redirect_url"] = data["redirectUrl"]

        return CreatePortalSessionResponse(**kwargs)
