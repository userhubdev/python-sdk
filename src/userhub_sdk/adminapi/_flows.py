# Code generated. DO NOT EDIT.

import datetime
from typing import Any, Dict, Optional

from userhub_sdk import adminv1
from userhub_sdk._internal import util
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport


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
        user_id: Optional[str] = None,
        type: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListFlowsResponse:
        """
        Lists flows.

        :param organization_id:
            Filter results by organization identifier.
        :param user_id:
            Filter results by user identifier.
        :param type:
            Filter the results by the specified flow type.
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
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `type`
            - `createTime`
        :param view:
            The Flow view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.flows.list", "GET", "/admin/v1/flows")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)
        if type:
            req.set_query("type", type)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)
        if view:
            req.set_query("view", view)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.ListFlowsResponse.__json_decode__)

    def create_join_organization(
        self,
        *,
        organization_id: str,
        user_id: Optional[str] = None,
        email: Optional[str] = None,
        display_name: Optional[str] = None,
        creator_user_id: Optional[str] = None,
        expire_time: Optional[datetime.datetime] = None,
        ttl: Optional[str] = None,
    ) -> adminv1.Flow:
        """
        Create a join organization flow.

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
        :param creator_user_id:
            The identifier of the user sending the invite.
        :param expire_time:
            The time the flow will expire.

            This field is not allowed if `ttl` is specified.
        :param ttl:
            The amount of time a flow will be available (e.g. `86400s`).

            This must be a string with the number of seconds followed by a
            trailing `s`.

            This field is not allowed if `expireTime` is specified.
        """
        req = Request(
            "admin.flows.createJoinOrganization",
            "POST",
            "/admin/v1/flows:createJoinOrganization",
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
        if creator_user_id:
            body["creatorUserId"] = creator_user_id
        if expire_time:
            body["expireTime"] = expire_time
        if ttl:
            body["ttl"] = ttl

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Flow.__json_decode__)

    def create_signup(
        self,
        *,
        email: str,
        display_name: Optional[str] = None,
        create_organization: Optional[bool] = None,
        creator_user_id: Optional[str] = None,
        expire_time: Optional[datetime.datetime] = None,
        ttl: Optional[str] = None,
    ) -> adminv1.Flow:
        """
        Create a signup flow.

        This invites a person to join the app.

        :param email:
            The email address of the person to invite.
        :param display_name:
            The display name of the person to invite.
        :param create_organization:
            Whether to create an organization as part of the signup flow.
        :param creator_user_id:
            The identifier of the user sending the invite.
        :param expire_time:
            The time the flow will expire.

            This field is not allowed if `ttl` is specified.
        :param ttl:
            The amount of time a flow will be available (e.g. `86400s`).

            This must be a string with the number of seconds followed by a
            trailing `s`.

            This field is not allowed if `expireTime` is specified.
        """
        req = Request(
            "admin.flows.createSignup", "POST", "/admin/v1/flows:createSignup"
        )
        body: Dict[str, Any] = {}

        if email:
            body["email"] = email
        if display_name:
            body["displayName"] = display_name
        if create_organization:
            body["createOrganization"] = create_organization
        if creator_user_id:
            body["creatorUserId"] = creator_user_id
        if expire_time:
            body["expireTime"] = expire_time
        if ttl:
            body["ttl"] = ttl

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Flow.__json_decode__)

    def get(
        self,
        flow_id: str,
    ) -> adminv1.Flow:
        """
        Retrieves specified flow.

        :param flow_id:
            The identifier of the flow.
        """
        req = Request(
            "admin.flows.get", "GET", f"/admin/v1/flows/{util.quote_path(flow_id)}"
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Flow.__json_decode__)

    def cancel(
        self,
        flow_id: str,
    ) -> adminv1.Flow:
        """
        Cancels specified flow.

        :param flow_id:
            The identifier of the flow.
        """
        req = Request(
            "admin.flows.cancel",
            "POST",
            f"/admin/v1/flows/{util.quote_path(flow_id)}:cancel",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Flow.__json_decode__)


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
        user_id: Optional[str] = None,
        type: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListFlowsResponse:
        """
        Lists flows.

        :param organization_id:
            Filter results by organization identifier.
        :param user_id:
            Filter results by user identifier.
        :param type:
            Filter the results by the specified flow type.
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
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `type`
            - `createTime`
        :param view:
            The Flow view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.flows.list", "GET", "/admin/v1/flows")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)
        if type:
            req.set_query("type", type)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)
        if view:
            req.set_query("view", view)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.ListFlowsResponse.__json_decode__)

    async def create_join_organization(
        self,
        *,
        organization_id: str,
        user_id: Optional[str] = None,
        email: Optional[str] = None,
        display_name: Optional[str] = None,
        creator_user_id: Optional[str] = None,
        expire_time: Optional[datetime.datetime] = None,
        ttl: Optional[str] = None,
    ) -> adminv1.Flow:
        """
        Create a join organization flow.

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
        :param creator_user_id:
            The identifier of the user sending the invite.
        :param expire_time:
            The time the flow will expire.

            This field is not allowed if `ttl` is specified.
        :param ttl:
            The amount of time a flow will be available (e.g. `86400s`).

            This must be a string with the number of seconds followed by a
            trailing `s`.

            This field is not allowed if `expireTime` is specified.
        """
        req = Request(
            "admin.flows.createJoinOrganization",
            "POST",
            "/admin/v1/flows:createJoinOrganization",
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
        if creator_user_id:
            body["creatorUserId"] = creator_user_id
        if expire_time:
            body["expireTime"] = expire_time
        if ttl:
            body["ttl"] = ttl

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Flow.__json_decode__)

    async def create_signup(
        self,
        *,
        email: str,
        display_name: Optional[str] = None,
        create_organization: Optional[bool] = None,
        creator_user_id: Optional[str] = None,
        expire_time: Optional[datetime.datetime] = None,
        ttl: Optional[str] = None,
    ) -> adminv1.Flow:
        """
        Create a signup flow.

        This invites a person to join the app.

        :param email:
            The email address of the person to invite.
        :param display_name:
            The display name of the person to invite.
        :param create_organization:
            Whether to create an organization as part of the signup flow.
        :param creator_user_id:
            The identifier of the user sending the invite.
        :param expire_time:
            The time the flow will expire.

            This field is not allowed if `ttl` is specified.
        :param ttl:
            The amount of time a flow will be available (e.g. `86400s`).

            This must be a string with the number of seconds followed by a
            trailing `s`.

            This field is not allowed if `expireTime` is specified.
        """
        req = Request(
            "admin.flows.createSignup", "POST", "/admin/v1/flows:createSignup"
        )
        body: Dict[str, Any] = {}

        if email:
            body["email"] = email
        if display_name:
            body["displayName"] = display_name
        if create_organization:
            body["createOrganization"] = create_organization
        if creator_user_id:
            body["creatorUserId"] = creator_user_id
        if expire_time:
            body["expireTime"] = expire_time
        if ttl:
            body["ttl"] = ttl

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Flow.__json_decode__)

    async def get(
        self,
        flow_id: str,
    ) -> adminv1.Flow:
        """
        Retrieves specified flow.

        :param flow_id:
            The identifier of the flow.
        """
        req = Request(
            "admin.flows.get", "GET", f"/admin/v1/flows/{util.quote_path(flow_id)}"
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Flow.__json_decode__)

    async def cancel(
        self,
        flow_id: str,
    ) -> adminv1.Flow:
        """
        Cancels specified flow.

        :param flow_id:
            The identifier of the flow.
        """
        req = Request(
            "admin.flows.cancel",
            "POST",
            f"/admin/v1/flows/{util.quote_path(flow_id)}:cancel",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Flow.__json_decode__)
