# Code generated. DO NOT EDIT.

from typing import Optional

from userhub_sdk import userv1
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport


class Roles:
    """
    The role methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def list(
        self,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> userv1.ListRolesResponse:
        """
        List roles.

        :param page_size:
            The maximum number of roles to return. The API may return fewer than
            this value.

            If unspecified, at most 20 roles will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list roles call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list roles must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by.
        """
        req = Request("user.roles.list", "GET", "/user/v1/roles")
        req.set_idempotent(True)

        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = self._transport.execute(req)

        return res.decode_body(userv1.ListRolesResponse.__json_decode__)


class AsyncRoles:
    """
    The role methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list(
        self,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> userv1.ListRolesResponse:
        """
        List roles.

        :param page_size:
            The maximum number of roles to return. The API may return fewer than
            this value.

            If unspecified, at most 20 roles will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list roles call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list roles must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by.
        """
        req = Request("user.roles.list", "GET", "/user/v1/roles")
        req.set_idempotent(True)

        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.ListRolesResponse.__json_decode__)
