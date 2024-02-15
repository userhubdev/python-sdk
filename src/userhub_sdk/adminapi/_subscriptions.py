# Code generated. DO NOT EDIT.

from typing import Optional

from userhub_sdk import adminv1
from userhub_sdk._internal import util
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport


class Subscriptions:
    """
    The subscription methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def list(
        self,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListSubscriptionsResponse:
        """
        Lists subscriptions.

        :param organization_id:
            Filter results by organization identifier.

            This is required if user identifier is not specified.
        :param user_id:
            Filter results by user identifier.

            This is required if organization identifier is not specified.
        :param page_size:
            The maximum number of subscriptions to return. The API may return fewer than
            this value.

            If unspecified, at most 20 subscriptions will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list subscriptions call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list subscriptions must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `createTime`
        :param view:
            The Subscription view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.subscriptions.list", "GET", "/admin/v1/subscriptions")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)
        if view:
            req.set_query("view", view)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.ListSubscriptionsResponse.__json_decode__)

    def get(
        self,
        subscription_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.Subscription:
        """
        Retrieves specified subscription.

        :param subscription_id:
            The identifier of the subscription.
        :param organization_id:
            Restrict by organization identifier.
        :param user_id:
            Restrict by user identifier.
        """
        req = Request(
            "admin.subscriptions.get",
            "GET",
            f"/admin/v1/subscriptions/{util.quote_path(subscription_id)}",
        )
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Subscription.__json_decode__)


class AsyncSubscriptions:
    """
    The subscription methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list(
        self,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListSubscriptionsResponse:
        """
        Lists subscriptions.

        :param organization_id:
            Filter results by organization identifier.

            This is required if user identifier is not specified.
        :param user_id:
            Filter results by user identifier.

            This is required if organization identifier is not specified.
        :param page_size:
            The maximum number of subscriptions to return. The API may return fewer than
            this value.

            If unspecified, at most 20 subscriptions will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list subscriptions call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list subscriptions must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `createTime`
        :param view:
            The Subscription view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.subscriptions.list", "GET", "/admin/v1/subscriptions")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)
        if view:
            req.set_query("view", view)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.ListSubscriptionsResponse.__json_decode__)

    async def get(
        self,
        subscription_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.Subscription:
        """
        Retrieves specified subscription.

        :param subscription_id:
            The identifier of the subscription.
        :param organization_id:
            Restrict by organization identifier.
        :param user_id:
            Restrict by user identifier.
        """
        req = Request(
            "admin.subscriptions.get",
            "GET",
            f"/admin/v1/subscriptions/{util.quote_path(subscription_id)}",
        )
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Subscription.__json_decode__)
