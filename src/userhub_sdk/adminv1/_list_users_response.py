# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util
from ._user import User


@dataclasses.dataclass
class ListUsersResponse:
    """
    Response message for ListUsers.
    """

    #: The list of users.
    users: Optional[List[User]] = dataclasses.field(default_factory=list)
    #: A token, which can be sent as `pageToken` to retrieve the next page.
    #: If this field is omitted, there are no subsequent pages.
    next_page_token: Optional[str] = None
    #: A token, which can be sent as `pageToken` to retrieve the previous page.
    #: If this field is absent, there are no preceding pages. If this field is
    #: an empty string then the previous page is the first result.
    previous_page_token: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.users is not None:
            data["users"] = [User.__json_encode__(v) for v in self.users]

        if self.next_page_token is not None:
            data["nextPageToken"] = self.next_page_token

        if self.previous_page_token is not None:
            data["previousPageToken"] = self.previous_page_token

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("users") is not None:
            kwargs["users"] = [User.__json_decode__(v) for v in data["users"]]

        if data.get("nextPageToken") is not None:
            kwargs["next_page_token"] = data["nextPageToken"]

        if data.get("previousPageToken") is not None:
            kwargs["previous_page_token"] = data["previousPageToken"]

        return ListUsersResponse(**kwargs)
