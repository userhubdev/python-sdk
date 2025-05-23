# Code generated. DO NOT EDIT.

from typing import Any, Dict, Optional, Union

from userhub_sdk import userv1
from userhub_sdk._internal import util
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport
from userhub_sdk.types import UNDEFINED, Undefined


class Flows:
    """
    The flow methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def list(
        self,
        *,
        organization_id: Optional[str] = None,
        type: Optional[str] = None,
        active: Optional[bool] = None,
        creator: Optional[bool] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> userv1.ListFlowsResponse:
        """
        List flows.

        :param organization_id:
            The identifier of the organization.

            When not set the user's flows are returned.

            Otherwise if the user is an admin of the provided organization then
            the flows associated with that organization are returned.
        :param type:
            Filter the results by the specified flow type.
        :param active:
            Whether to filter out flows not in the `START_PENDING` or `STARTED`
            state.
        :param creator:
            Whether to only return flows created by the authenticated user.
        :param page_size:
            The maximum number of flows to return. The API may return fewer than
            this value.

            If unspecified, at most 20 flows will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list flows call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list flows must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by.
        """
        req = Request("user.flows.list", "GET", "/user/v1/flows")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if type:
            req.set_query("type", type)
        if active:
            req.set_query("active", active)
        if creator:
            req.set_query("creator", creator)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = self._transport.execute(req)

        return res.decode_body(userv1.ListFlowsResponse.__json_decode__)

    def create_join_organization(
        self,
        *,
        organization_id: str,
        user_id: Optional[str] = None,
        email: Optional[str] = None,
        display_name: Optional[str] = None,
        role_id: Optional[str] = None,
    ) -> userv1.Flow:
        """
        Create a new join organization flow.

        This invites a person to join an organization.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.

            This is required if email is not specified.
        :param email:
            The email address of the person to invite.

            This is required if user is not specified or the user
            does not have an email address.
        :param display_name:
            The display name of the person to invite.
        :param role_id:
            The identifier of the role.
        """
        req = Request(
            "user.flows.createJoinOrganization",
            "POST",
            "/user/v1/flows:createJoinOrganization",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id
        if email:
            body["email"] = email
        if display_name:
            body["displayName"] = display_name
        if role_id:
            body["roleId"] = role_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    def update_join_organization(
        self,
        flow_id: str,
        *,
        role_id: Union[Optional[str], Undefined] = UNDEFINED,
    ) -> userv1.Flow:
        """
        Update a join organization flow.

        :param flow_id:
            The identifier of the flow.
        :param role_id:
            The identifier of the role.
        """
        req = Request(
            "user.flows.updateJoinOrganization",
            "PATCH",
            f"/user/v1/flows/{util.quote_path(flow_id)}:updateJoinOrganization",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if role_id is not UNDEFINED:
            body["roleId"] = role_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    def create_signup(
        self,
        *,
        email: str,
        display_name: Optional[str] = None,
        create_organization: Optional[bool] = None,
    ) -> userv1.Flow:
        """
        Create a new signup flow.

        This invites a person to join the app.

        :param email:
            The email address of the person to invite.
        :param display_name:
            The display name of the person to invite.
        :param create_organization:
            Whether to create an organization as part of the signup flow.
        """
        req = Request("user.flows.createSignup", "POST", "/user/v1/flows:createSignup")
        body: Dict[str, Any] = {}

        if email:
            body["email"] = email
        if display_name:
            body["displayName"] = display_name
        if create_organization:
            body["createOrganization"] = create_organization

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    def get(
        self,
        flow_id: str,
    ) -> userv1.Flow:
        """
        Get a flow.

        :param flow_id:
            The identifier of the flow or the flow secret.
        """
        req = Request(
            "user.flows.get", "GET", f"/user/v1/flows/{util.quote_path(flow_id)}"
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    def consume(
        self,
        flow_id: str,
    ) -> userv1.Flow:
        """
        Consume a flow.

        This accepts the flow (e.g. for a join organization flow it will
        accept the invitation and add the member to the organization).

        :param flow_id:
            The identifier of the flow or the flow secret.
        """
        req = Request(
            "user.flows.consume",
            "POST",
            f"/user/v1/flows/{util.quote_path(flow_id)}:consume",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    def cancel(
        self,
        flow_id: str,
    ) -> userv1.Flow:
        """
        Cancel a flow.

        This cancels the flow and hides it from the user.

        :param flow_id:
            The identifier of the flow or the flow secret.
        """
        req = Request(
            "user.flows.cancel",
            "POST",
            f"/user/v1/flows/{util.quote_path(flow_id)}:cancel",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)


class AsyncFlows:
    """
    The flow methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list(
        self,
        *,
        organization_id: Optional[str] = None,
        type: Optional[str] = None,
        active: Optional[bool] = None,
        creator: Optional[bool] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> userv1.ListFlowsResponse:
        """
        List flows.

        :param organization_id:
            The identifier of the organization.

            When not set the user's flows are returned.

            Otherwise if the user is an admin of the provided organization then
            the flows associated with that organization are returned.
        :param type:
            Filter the results by the specified flow type.
        :param active:
            Whether to filter out flows not in the `START_PENDING` or `STARTED`
            state.
        :param creator:
            Whether to only return flows created by the authenticated user.
        :param page_size:
            The maximum number of flows to return. The API may return fewer than
            this value.

            If unspecified, at most 20 flows will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list flows call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list flows must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by.
        """
        req = Request("user.flows.list", "GET", "/user/v1/flows")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if type:
            req.set_query("type", type)
        if active:
            req.set_query("active", active)
        if creator:
            req.set_query("creator", creator)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.ListFlowsResponse.__json_decode__)

    async def create_join_organization(
        self,
        *,
        organization_id: str,
        user_id: Optional[str] = None,
        email: Optional[str] = None,
        display_name: Optional[str] = None,
        role_id: Optional[str] = None,
    ) -> userv1.Flow:
        """
        Create a new join organization flow.

        This invites a person to join an organization.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.

            This is required if email is not specified.
        :param email:
            The email address of the person to invite.

            This is required if user is not specified or the user
            does not have an email address.
        :param display_name:
            The display name of the person to invite.
        :param role_id:
            The identifier of the role.
        """
        req = Request(
            "user.flows.createJoinOrganization",
            "POST",
            "/user/v1/flows:createJoinOrganization",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id
        if email:
            body["email"] = email
        if display_name:
            body["displayName"] = display_name
        if role_id:
            body["roleId"] = role_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    async def update_join_organization(
        self,
        flow_id: str,
        *,
        role_id: Union[Optional[str], Undefined] = UNDEFINED,
    ) -> userv1.Flow:
        """
        Update a join organization flow.

        :param flow_id:
            The identifier of the flow.
        :param role_id:
            The identifier of the role.
        """
        req = Request(
            "user.flows.updateJoinOrganization",
            "PATCH",
            f"/user/v1/flows/{util.quote_path(flow_id)}:updateJoinOrganization",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if role_id is not UNDEFINED:
            body["roleId"] = role_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    async def create_signup(
        self,
        *,
        email: str,
        display_name: Optional[str] = None,
        create_organization: Optional[bool] = None,
    ) -> userv1.Flow:
        """
        Create a new signup flow.

        This invites a person to join the app.

        :param email:
            The email address of the person to invite.
        :param display_name:
            The display name of the person to invite.
        :param create_organization:
            Whether to create an organization as part of the signup flow.
        """
        req = Request("user.flows.createSignup", "POST", "/user/v1/flows:createSignup")
        body: Dict[str, Any] = {}

        if email:
            body["email"] = email
        if display_name:
            body["displayName"] = display_name
        if create_organization:
            body["createOrganization"] = create_organization

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    async def get(
        self,
        flow_id: str,
    ) -> userv1.Flow:
        """
        Get a flow.

        :param flow_id:
            The identifier of the flow or the flow secret.
        """
        req = Request(
            "user.flows.get", "GET", f"/user/v1/flows/{util.quote_path(flow_id)}"
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    async def consume(
        self,
        flow_id: str,
    ) -> userv1.Flow:
        """
        Consume a flow.

        This accepts the flow (e.g. for a join organization flow it will
        accept the invitation and add the member to the organization).

        :param flow_id:
            The identifier of the flow or the flow secret.
        """
        req = Request(
            "user.flows.consume",
            "POST",
            f"/user/v1/flows/{util.quote_path(flow_id)}:consume",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)

    async def cancel(
        self,
        flow_id: str,
    ) -> userv1.Flow:
        """
        Cancel a flow.

        This cancels the flow and hides it from the user.

        :param flow_id:
            The identifier of the flow or the flow secret.
        """
        req = Request(
            "user.flows.cancel",
            "POST",
            f"/user/v1/flows/{util.quote_path(flow_id)}:cancel",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Flow.__json_decode__)
