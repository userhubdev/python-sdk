# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional

from ._user import User


@dataclasses.dataclass
class SearchUsersResponse:
    """
    Response message for SearchUsers.
    """

    #: The search of users.
    users: List[User] = dataclasses.field(default_factory=list)
    #: A token, which can be sent as `pageToken` to retrieve the next page.
    #: If this field is omitted, there are no subsequent pages.
    next_page_token: str = ""
    #: A token, which can be sent as `pageToken` to retrieve the previous page.
    #: If this field is absent, there are no preceding pages. If this field is
    #: an empty string then the previous page is the first result.
    previous_page_token: Optional[str] = None
    #: The estimated total count of matched users irrespective of pagination.
    #:
    #: This field is ignored if `show_total_size` is not true or `pageToken`
    #: is not empty.
    total_size: Optional[int] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.users is not None:
            data["users"] = [User.__json_encode__(v) for v in self.users]

        if self.next_page_token is not None:
            data["nextPageToken"] = self.next_page_token

        if self.previous_page_token is not None:
            data["previousPageToken"] = self.previous_page_token

        if self.total_size is not None:
            data["totalSize"] = self.total_size

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "SearchUsersResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("users") is not None:
            kwargs["users"] = [User.__json_decode__(v) for v in data["users"]]

        if data.get("nextPageToken") is not None:
            kwargs["next_page_token"] = data["nextPageToken"]

        if data.get("previousPageToken") is not None:
            kwargs["previous_page_token"] = data["previousPageToken"]

        if data.get("totalSize") is not None:
            kwargs["total_size"] = data["totalSize"]

        return SearchUsersResponse(**kwargs)
