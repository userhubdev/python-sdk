# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List, Optional

from ._role import Role


@dataclasses.dataclass
class ListRolesResponse:
    """
    Response message for ListRoles.
    """

    #: The list of roles.
    roles: List[Role] = dataclasses.field(default_factory=list)
    #: A token, which can be sent as `pageToken` to retrieve the next page.
    #: If this field is omitted, there are no subsequent pages.
    next_page_token: str = ""
    #: A token, which can be sent as `pageToken` to retrieve the previous page.
    #: If this field is absent, there are no preceding pages. If this field is
    #: an empty string then the previous page is the first result.
    previous_page_token: Optional[str] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.roles is not None:
            data["roles"] = [Role.__json_encode__(v) for v in self.roles]

        if self.next_page_token is not None:
            data["nextPageToken"] = self.next_page_token

        if self.previous_page_token is not None:
            data["previousPageToken"] = self.previous_page_token

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "ListRolesResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("roles") is not None:
            kwargs["roles"] = [Role.__json_decode__(v) for v in data["roles"]]

        if data.get("nextPageToken") is not None:
            kwargs["next_page_token"] = data["nextPageToken"]

        if data.get("previousPageToken") is not None:
            kwargs["previous_page_token"] = data["previousPageToken"]

        return ListRolesResponse(**kwargs)
