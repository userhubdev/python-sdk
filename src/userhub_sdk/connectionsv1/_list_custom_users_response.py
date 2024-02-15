# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util
from ._custom_user import CustomUser


@dataclasses.dataclass
class ListCustomUsersResponse:
    """
    Response message for listing custom users.
    """

    #: The list of users.
    users: Optional[List[CustomUser]] = dataclasses.field(default_factory=list)
    #: A token the webhook can set to indicate it has more results.
    #:
    #: This can be a page number, offset number, timestamp, or any value
    #: the webhook handler wants to use for pagination.
    #:
    #: It must be encoded as a string.
    next_page_token: Optional[str] = None

    def __json_encode__(self):
        data = {}

        if self.users is not None:
            data["users"] = [CustomUser.__json_encode__(v) for v in self.users]

        if self.next_page_token is not None:
            data["nextPageToken"] = self.next_page_token

        return data

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("users") is not None:
            kwargs["users"] = [CustomUser.__json_decode__(v) for v in data["users"]]

        if data.get("nextPageToken") is not None:
            kwargs["next_page_token"] = data["nextPageToken"]

        return ListCustomUsersResponse(**kwargs)
