# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any, Dict, List

from ._user_result import UserResult


@dataclasses.dataclass
class BatchGetUsersResponse:
    """
    Response message for BatchGetUsers.
    """

    #: The user results.
    users: List[UserResult] = dataclasses.field(default_factory=list)

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.users is not None:
            data["users"] = [UserResult.__json_encode__(v) for v in self.users]

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "BatchGetUsersResponse":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("users") is not None:
            kwargs["users"] = [UserResult.__json_decode__(v) for v in data["users"]]

        return BatchGetUsersResponse(**kwargs)
