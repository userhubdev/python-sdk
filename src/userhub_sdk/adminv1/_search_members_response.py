# Code generated. DO NOT EDIT.

import dataclasses
from typing import List
from typing import Optional

from .._internal import util
from ._member import Member


@dataclasses.dataclass
class SearchMembersResponse:
    """
    Response message for SearchMembers.
    """

    #: The search of members.
    members: Optional[List[Member]] = dataclasses.field(default_factory=list)
    #: A token, which can be sent as `pageToken` to retrieve the next page.
    #: If this field is omitted, there are no subsequent pages.
    next_page_token: Optional[str] = None
    #: A token, which can be sent as `pageToken` to retrieve the previous page.
    #: If this field is absent, there are no preceding pages. If this field is
    #: an empty string then the previous page is the first result.
    previous_page_token: Optional[str] = None
    #: The estimated total count of matched members irrespective of pagination.
    #:
    #: This field is ignored if `show_total_size` is not true or `pageToken`
    #: is not empty.
    total_size: Optional[int] = None

    def __json_encode__(self):
        return dict(user.__dict__)

    @staticmethod
    def __json_decode__(data):
        if data is None:
            return None

        kwargs = {}

        if data.get("members") is not None:
            kwargs["members"] = [Member.__json_decode__(v) for v in data["members"]]

        if data.get("nextPageToken") is not None:
            kwargs["next_page_token"] = data["nextPageToken"]

        if data.get("previousPageToken") is not None:
            kwargs["previous_page_token"] = data["previousPageToken"]

        if data.get("totalSize") is not None:
            kwargs["total_size"] = data["totalSize"]

        return SearchMembersResponse(**kwargs)
