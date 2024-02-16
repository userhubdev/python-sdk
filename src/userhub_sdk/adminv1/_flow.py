# Code generated. DO NOT EDIT.

import dataclasses
import datetime
from typing import Any, Dict, Optional

from userhub_sdk._internal import constants, util

from ._join_organization_flow import JoinOrganizationFlow
from ._organization import Organization
from ._signup_flow import SignupFlow
from ._user import User


@dataclasses.dataclass
class Flow:
    """
    An invitation, task, or user request (e.g. join organization).
    """

    #: The system-assigned identifier of the flow.
    id: str = ""
    #: The current state of the flow.
    state: str = ""
    #: The code that best describes the reason for the state.
    state_reason: Optional[str] = None
    #: The flow type.
    type: str = ""
    #: The target organization for the flow.
    organization: Optional[Organization] = None
    #: The target user for the flow.
    user: Optional[User] = None
    #: The user who created the flow.
    #:
    #: This will not be set if the invitation was created by an admin.
    creator: Optional[User] = None
    #: The start time of the flow.
    start_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The time the flow will expire.
    expire_time: Optional[datetime.datetime] = None
    #: The expire duration of the flow.
    ttl: Optional[str] = None
    #: The flow secret.
    #:
    #: This is only populated on create.
    secret: Optional[str] = None
    #: The creation time of the flow.
    create_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The last update time of the flow.
    update_time: datetime.datetime = constants.EMPTY_DATETIME
    #: The join organization flow type specific data.
    join_organization: Optional[JoinOrganizationFlow] = None
    #: The signup flow type specific data
    signup: Optional[SignupFlow] = None

    def __json_encode__(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {}

        if self.id is not None:
            data["id"] = self.id

        if self.state is not None:
            data["state"] = self.state

        if self.state_reason is not None:
            data["stateReason"] = self.state_reason

        if self.type is not None:
            data["type"] = self.type

        if self.organization is not None:
            data["organization"] = Organization.__json_encode__(self.organization)

        if self.user is not None:
            data["user"] = User.__json_encode__(self.user)

        if self.creator is not None:
            data["creator"] = User.__json_encode__(self.creator)

        if self.start_time is not None:
            data["startTime"] = util.encode_datetime(self.start_time)

        if self.expire_time is not None:
            data["expireTime"] = util.encode_datetime(self.expire_time)

        if self.ttl is not None:
            data["ttl"] = self.ttl

        if self.secret is not None:
            data["secret"] = self.secret

        if self.create_time is not None:
            data["createTime"] = util.encode_datetime(self.create_time)

        if self.update_time is not None:
            data["updateTime"] = util.encode_datetime(self.update_time)

        if self.join_organization is not None:
            data["joinOrganization"] = JoinOrganizationFlow.__json_encode__(
                self.join_organization
            )

        if self.signup is not None:
            data["signup"] = SignupFlow.__json_encode__(self.signup)

        return data

    @staticmethod
    def __json_decode__(data: Dict[str, Any]) -> "Flow":
        if data is None:
            data = {}

        kwargs: Dict[str, Any] = {}

        if data.get("id") is not None:
            kwargs["id"] = data["id"]

        if data.get("state") is not None:
            kwargs["state"] = data["state"]

        if data.get("stateReason") is not None:
            kwargs["state_reason"] = data["stateReason"]

        if data.get("type") is not None:
            kwargs["type"] = data["type"]

        if data.get("organization") is not None:
            kwargs["organization"] = Organization.__json_decode__(data["organization"])

        if data.get("user") is not None:
            kwargs["user"] = User.__json_decode__(data["user"])

        if data.get("creator") is not None:
            kwargs["creator"] = User.__json_decode__(data["creator"])

        if data.get("startTime") is not None:
            kwargs["start_time"] = util.decode_datetime(data["startTime"])

        if data.get("expireTime") is not None:
            kwargs["expire_time"] = util.decode_datetime(data["expireTime"])

        if data.get("ttl") is not None:
            kwargs["ttl"] = data["ttl"]

        if data.get("secret") is not None:
            kwargs["secret"] = data["secret"]

        if data.get("createTime") is not None:
            kwargs["create_time"] = util.decode_datetime(data["createTime"])

        if data.get("updateTime") is not None:
            kwargs["update_time"] = util.decode_datetime(data["updateTime"])

        if data.get("joinOrganization") is not None:
            kwargs["join_organization"] = JoinOrganizationFlow.__json_decode__(
                data["joinOrganization"]
            )

        if data.get("signup") is not None:
            kwargs["signup"] = SignupFlow.__json_decode__(data["signup"])

        return Flow(**kwargs)
