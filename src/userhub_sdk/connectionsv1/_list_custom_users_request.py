# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, Optional


@dataclasses.dataclass
class ListCustomUsersRequest:
    """
    Request message for listing custom users.
    """

    #: The maximum number of users to return. The webhook is allowed to
    #: return fewer than this value, but it should never return more.
    page_size: int = 0
    #: A page token, this is from the response of the previous list
    #: request.
    #:
    #: This should be used to determine the next page of results.
    page_token: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.page_size is not None:
            data["pageSize"] = self.page_size

        if self.page_token is not None:
            data["pageToken"] = self.page_token

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "ListCustomUsersRequest":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("pageSize") is not None:
            kwargs["page_size"] = data["pageSize"]

        if data.get("pageToken") is not None:
            kwargs["page_token"] = data["pageToken"]

        return ListCustomUsersRequest(**kwargs)
