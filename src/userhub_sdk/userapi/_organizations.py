# Code generated. DO NOT EDIT.

import dataclasses
from typing import Any
from typing import Dict
from typing import Optional
from urllib.parse import quote

from .. import apiv1
from .. import userv1
from .._internal import constants
from .._internal import util
from .._internal.request import Request
from .._internal.transport import AsyncTransport
from .._internal.transport import Transport


class Organizations:
    """
    The organization methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def list(
        self,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> userv1.ListOrganizationsResponse:
        """
        Lists organizations.

        :param page_size:
            The maximum number of organizations to return. The API may return fewer than
            this value.

            If unspecified, at most 20 organizations will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list organizations call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list organizations must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `displayName`
            - `email`
        """
        req = Request("user.organizations.list", "GET", "/user/v1/organizations")
        req.set_idempotent(True)

        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = self._transport.execute(req)

        return res.decode_body(userv1.ListOrganizationsResponse.__json_decode__)

    def create(
        self,
        *,
        unique_id: Optional[str] = None,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        flow_id: Optional[str] = None,
    ) -> userv1.Organization:
        """
        Creates a new organization.

        :param unique_id:
            The client defined unique identifier of the organization account.

            It is restricted to letters, numbers, underscores, and hyphens,
            with the first character a letter or a number, and a 255
            character maximum.

            ID's starting with `org_` are reserved.
        :param display_name:
            The human-readable display name of the organization.

            The maximum length is 200 characters.
        :param email:
            The email address of the organization.

            The maximum length is 320 characters.
        :param flow_id:
            The flow identifier associated with the creation of the organization.

            The flow type must be `SIGNUP` and associated with the user creating the organization.
        """
        req = Request("user.organizations.create", "POST", "/user/v1/organizations")
        body: Dict[str, Any] = {}

        if unique_id:
            body["uniqueId"] = unique_id
        if display_name:
            body["displayName"] = display_name
        if email:
            body["email"] = email
        if flow_id:
            body["flowId"] = flow_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Organization.__json_decode__)

    def get(
        self,
        organization_id: str,
    ) -> userv1.Organization:
        """
        Retrieves specified organization.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "user.organizations.get",
            "GET",
            f"/user/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Organization.__json_decode__)

    def update(
        self,
        organization_id: str,
        *,
        unique_id: Optional[str] = None,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        flow_id: Optional[str] = None,
    ) -> userv1.Organization:
        """
        Updates specified organization.

        :param organization_id:
            The identifier of the organization.
        :param unique_id:
            The client defined unique identifier of the organization account.

            It is restricted to letters, numbers, underscores, and hyphens,
            with the first character a letter or a number, and a 255
            character maximum.

            ID's starting with `org_` are reserved.
        :param display_name:
            The human-readable display name of the organization.

            The maximum length is 200 characters.
        :param email:
            The email address of the organization.

            The maximum length is 320 characters.
        :param flow_id:
            The flow identifier associated with the creation of the organization.

            The flow type must be `SIGNUP` and associated with the user creating the organization.
        """
        req = Request(
            "user.organizations.update",
            "PATCH",
            f"/user/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if unique_id is not dataclasses.MISSING:
            body["uniqueId"] = unique_id
        if display_name is not dataclasses.MISSING:
            body["displayName"] = display_name
        if email is not dataclasses.MISSING:
            body["email"] = email
        if flow_id is not dataclasses.MISSING:
            body["flowId"] = flow_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Organization.__json_decode__)

    def delete(
        self,
        organization_id: str,
    ) -> userv1.Organization:
        """
        Delete specified organization.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "user.organizations.delete",
            "DELETE",
            f"/user/v1/organizations/{util.quote_path(organization_id)}",
        )
        res = self._transport.execute(req)

        return res.decode_body(userv1.Organization.__json_decode__)

    def leave(
        self,
        organization_id: str,
    ) -> apiv1.EmptyResponse:
        """
        Leave organization.

        This allows a user to remove themselves from an organization
        without have permission to manage the organization.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "user.organizations.leave",
            "DELETE",
            f"/user/v1/organizations/{util.quote_path(organization_id)}:leave",
        )
        res = self._transport.execute(req)

        return res.decode_body(apiv1.EmptyResponse.__json_decode__)


class AsyncOrganizations:
    """
    The organization methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list(
        self,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> userv1.ListOrganizationsResponse:
        """
        Lists organizations.

        :param page_size:
            The maximum number of organizations to return. The API may return fewer than
            this value.

            If unspecified, at most 20 organizations will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list organizations call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list organizations must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `displayName`
            - `email`
        """
        req = Request("user.organizations.list", "GET", "/user/v1/organizations")
        req.set_idempotent(True)

        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.ListOrganizationsResponse.__json_decode__)

    async def create(
        self,
        *,
        unique_id: Optional[str] = None,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        flow_id: Optional[str] = None,
    ) -> userv1.Organization:
        """
        Creates a new organization.

        :param unique_id:
            The client defined unique identifier of the organization account.

            It is restricted to letters, numbers, underscores, and hyphens,
            with the first character a letter or a number, and a 255
            character maximum.

            ID's starting with `org_` are reserved.
        :param display_name:
            The human-readable display name of the organization.

            The maximum length is 200 characters.
        :param email:
            The email address of the organization.

            The maximum length is 320 characters.
        :param flow_id:
            The flow identifier associated with the creation of the organization.

            The flow type must be `SIGNUP` and associated with the user creating the organization.
        """
        req = Request("user.organizations.create", "POST", "/user/v1/organizations")
        body: Dict[str, Any] = {}

        if unique_id:
            body["uniqueId"] = unique_id
        if display_name:
            body["displayName"] = display_name
        if email:
            body["email"] = email
        if flow_id:
            body["flowId"] = flow_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Organization.__json_decode__)

    async def get(
        self,
        organization_id: str,
    ) -> userv1.Organization:
        """
        Retrieves specified organization.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "user.organizations.get",
            "GET",
            f"/user/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Organization.__json_decode__)

    async def update(
        self,
        organization_id: str,
        *,
        unique_id: Optional[str] = None,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        flow_id: Optional[str] = None,
    ) -> userv1.Organization:
        """
        Updates specified organization.

        :param organization_id:
            The identifier of the organization.
        :param unique_id:
            The client defined unique identifier of the organization account.

            It is restricted to letters, numbers, underscores, and hyphens,
            with the first character a letter or a number, and a 255
            character maximum.

            ID's starting with `org_` are reserved.
        :param display_name:
            The human-readable display name of the organization.

            The maximum length is 200 characters.
        :param email:
            The email address of the organization.

            The maximum length is 320 characters.
        :param flow_id:
            The flow identifier associated with the creation of the organization.

            The flow type must be `SIGNUP` and associated with the user creating the organization.
        """
        req = Request(
            "user.organizations.update",
            "PATCH",
            f"/user/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if unique_id is not dataclasses.MISSING:
            body["uniqueId"] = unique_id
        if display_name is not dataclasses.MISSING:
            body["displayName"] = display_name
        if email is not dataclasses.MISSING:
            body["email"] = email
        if flow_id is not dataclasses.MISSING:
            body["flowId"] = flow_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Organization.__json_decode__)

    async def delete(
        self,
        organization_id: str,
    ) -> userv1.Organization:
        """
        Delete specified organization.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "user.organizations.delete",
            "DELETE",
            f"/user/v1/organizations/{util.quote_path(organization_id)}",
        )
        res = await self._transport.execute(req)

        return res.decode_body(userv1.Organization.__json_decode__)

    async def leave(
        self,
        organization_id: str,
    ) -> apiv1.EmptyResponse:
        """
        Leave organization.

        This allows a user to remove themselves from an organization
        without have permission to manage the organization.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "user.organizations.leave",
            "DELETE",
            f"/user/v1/organizations/{util.quote_path(organization_id)}:leave",
        )
        res = await self._transport.execute(req)

        return res.decode_body(apiv1.EmptyResponse.__json_decode__)
