# Code generated. DO NOT EDIT.

import datetime
from typing import Any, Dict, Optional, Union

from userhub_sdk import adminv1, apiv1, commonv1
from userhub_sdk._internal import util
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport
from userhub_sdk.types import UNDEFINED, Undefined


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
        show_deleted: Optional[bool] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListOrganizationsResponse:
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
            - `createTime`
            - `deleteTime`
        :param show_deleted:
            Whether to show deleted organizations.
        :param view:
            The organization view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.organizations.list", "GET", "/admin/v1/organizations")
        req.set_idempotent(True)

        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)
        if show_deleted:
            req.set_query("showDeleted", show_deleted)
        if view:
            req.set_query("view", view)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.ListOrganizationsResponse.__json_decode__)

    def create(
        self,
        *,
        unique_id: Optional[str] = None,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        email_verified: Optional[bool] = None,
        phone_number: Optional[str] = None,
        phone_number_verified: Optional[bool] = None,
        image_url: Optional[str] = None,
        currency_code: Optional[str] = None,
        language_code: Optional[str] = None,
        region_code: Optional[str] = None,
        time_zone: Optional[str] = None,
        address: Optional[commonv1.Address] = None,
        signup_time: Optional[datetime.datetime] = None,
        disabled: Optional[bool] = None,
    ) -> adminv1.Organization:
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
        :param email_verified:
            Whether the organization's email address has been verified.
        :param phone_number:
            The E164 phone number for the organization (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the organization's phone number has been verified.
        :param image_url:
            The photo/avatar URL of the organization.

            The maximum length is 2000 characters.
        :param currency_code:
            The default ISO-4217 currency code for the organization (e.g. `USD`).
        :param language_code:
            The IETF BCP-47 language code for the organization (e.g. `en`).
        :param region_code:
            The country/region code for the organization (e.g. `US`).
        :param time_zone:
            The IANA time zone for the organization (e.g. `America/New_York`).
        :param address:
            The billing address for the organization.
        :param signup_time:
            The sign-up time for the organization.
        :param disabled:
            Whether the organization is disabled.
        """
        req = Request("admin.organizations.create", "POST", "/admin/v1/organizations")
        body: Dict[str, Any] = {}

        if unique_id:
            body["uniqueId"] = unique_id
        if display_name:
            body["displayName"] = display_name
        if email:
            body["email"] = email
        if email_verified:
            body["emailVerified"] = email_verified
        if phone_number:
            body["phoneNumber"] = phone_number
        if phone_number_verified:
            body["phoneNumberVerified"] = phone_number_verified
        if image_url:
            body["imageUrl"] = image_url
        if currency_code:
            body["currencyCode"] = currency_code
        if language_code:
            body["languageCode"] = language_code
        if region_code:
            body["regionCode"] = region_code
        if time_zone:
            body["timeZone"] = time_zone
        if address:
            body["address"] = address
        if signup_time:
            body["signupTime"] = signup_time
        if disabled:
            body["disabled"] = disabled

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    def get(
        self,
        organization_id: str,
    ) -> adminv1.Organization:
        """
        Retrieves specified organization.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "admin.organizations.get",
            "GET",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    def update(
        self,
        organization_id: str,
        *,
        unique_id: Union[Optional[str], Undefined] = UNDEFINED,
        display_name: Union[Optional[str], Undefined] = UNDEFINED,
        email: Union[Optional[str], Undefined] = UNDEFINED,
        email_verified: Union[Optional[bool], Undefined] = UNDEFINED,
        phone_number: Union[Optional[str], Undefined] = UNDEFINED,
        phone_number_verified: Union[Optional[bool], Undefined] = UNDEFINED,
        image_url: Union[Optional[str], Undefined] = UNDEFINED,
        currency_code: Union[Optional[str], Undefined] = UNDEFINED,
        language_code: Union[Optional[str], Undefined] = UNDEFINED,
        region_code: Union[Optional[str], Undefined] = UNDEFINED,
        time_zone: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        signup_time: Union[Optional[datetime.datetime], Undefined] = UNDEFINED,
        disabled: Union[Optional[bool], Undefined] = UNDEFINED,
        allow_missing: Optional[bool] = None,
    ) -> adminv1.Organization:
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
        :param email_verified:
            Whether the organization's email address has been verified.
        :param phone_number:
            The E164 phone number for the organization (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the organization's phone number has been verified.
        :param image_url:
            The photo/avatar URL of the organization.

            The maximum length is 2000 characters.
        :param currency_code:
            The default ISO-4217 currency code for the organization (e.g. `USD`).
        :param language_code:
            The IETF BCP-47 language code for the organization (e.g. `en`).
        :param region_code:
            The country/region code for the organization (e.g. `US`).
        :param time_zone:
            The IANA time zone for the organization (e.g. `America/New_York`).
        :param address:
            The billing address for the organization.
        :param signup_time:
            The sign-up time for the organization.
        :param disabled:
            Whether the organization is disabled.
        :param allow_missing:
            If set to true, and the organization is not found, a new organization will be created.

            You must use the unique identifier for the identifier when this is true.
        """
        req = Request(
            "admin.organizations.update",
            "PATCH",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if allow_missing:
            req.set_query("allowMissing", allow_missing)
        if unique_id is not UNDEFINED:
            body["uniqueId"] = unique_id
        if display_name is not UNDEFINED:
            body["displayName"] = display_name
        if email is not UNDEFINED:
            body["email"] = email
        if email_verified is not UNDEFINED:
            body["emailVerified"] = email_verified
        if phone_number is not UNDEFINED:
            body["phoneNumber"] = phone_number
        if phone_number_verified is not UNDEFINED:
            body["phoneNumberVerified"] = phone_number_verified
        if image_url is not UNDEFINED:
            body["imageUrl"] = image_url
        if currency_code is not UNDEFINED:
            body["currencyCode"] = currency_code
        if language_code is not UNDEFINED:
            body["languageCode"] = language_code
        if region_code is not UNDEFINED:
            body["regionCode"] = region_code
        if time_zone is not UNDEFINED:
            body["timeZone"] = time_zone
        if address is not UNDEFINED:
            body["address"] = address
        if signup_time is not UNDEFINED:
            body["signupTime"] = signup_time
        if disabled is not UNDEFINED:
            body["disabled"] = disabled

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    def delete(
        self,
        organization_id: str,
    ) -> adminv1.Organization:
        """
        Marks specified organization for deletion.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "admin.organizations.delete",
            "DELETE",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    def undelete(
        self,
        organization_id: str,
    ) -> adminv1.Organization:
        """
        Un-marks specified organization for deletion.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "admin.organizations.undelete",
            "POST",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}:undelete",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    def connect(
        self,
        organization_id: str,
        *,
        connection_id: str,
        external_id: Optional[str] = None,
    ) -> adminv1.Organization:
        """
        Connect specified organization to external account.

        :param organization_id:
            The organization identifier.
        :param connection_id:
            The identifier of the connection.
        :param external_id:
            The external identifier of the organization to connect.

            On create if this is empty a new external organization will
            be created if the connection supports it.
        """
        req = Request(
            "admin.organizations.connect",
            "POST",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}:connect",
        )
        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
        if external_id:
            body["externalId"] = external_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    def disconnect(
        self,
        organization_id: str,
        *,
        connection_id: str,
        delete_external_account: Optional[bool] = None,
    ) -> adminv1.Organization:
        """
        Disconnect specified organization from external account.

        This will delete all the data associated with the connected account, including
        payment methods, invoices, and subscriptions.

        If the delete external account option is enabled it will also attempt to delete
        the external account (e.g. Stripe Customer object).

        WARNING: This can irreversibly destroy data and should be
        used with extreme caution.

        :param organization_id:
            The organization identifier.
        :param connection_id:
            The identifier of the connection.
        :param delete_external_account:
            Whether to attempt to delete the external account and all
            it's associated data (e.g. Stripe Customer object).
        """
        req = Request(
            "admin.organizations.disconnect",
            "POST",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}:disconnect",
        )
        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
        if delete_external_account:
            body["deleteExternalAccount"] = delete_external_account

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    def list_members(
        self,
        organization_id: str,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> adminv1.ListMembersResponse:
        """
        Lists organization members.

        :param organization_id:
            The identifier of the organization.
        :param page_size:
            The maximum number of members to return. The API may return fewer than
            this value.

            If unspecified, at most 20 members will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list members call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list members must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `createTime`
            - `updateTime`
        """
        req = Request(
            "admin.organizations.listMembers",
            "GET",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members",
        )
        req.set_idempotent(True)

        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.ListMembersResponse.__json_decode__)

    def add_member(
        self,
        organization_id: str,
        *,
        user_id: Optional[str] = None,
        role_id: Optional[str] = None,
    ) -> adminv1.Member:
        """
        Creates a new organization member.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.
        :param role_id:
            The identifier of the role.

            This is currently limited to `member`, `admin`, and `owner`.
        """
        req = Request(
            "admin.organizations.addMember",
            "POST",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members",
        )
        body: Dict[str, Any] = {}

        if user_id:
            body["userId"] = user_id
        if role_id:
            body["roleId"] = role_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Member.__json_decode__)

    def get_member(
        self,
        organization_id: str,
        user_id: str,
    ) -> adminv1.Member:
        """
        Retrieves specified organization member.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.organizations.getMember",
            "GET",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members/{util.quote_path(user_id)}",
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Member.__json_decode__)

    def update_member(
        self,
        organization_id: str,
        user_id: str,
        *,
        role_id: Union[str, Undefined] = UNDEFINED,
        allow_missing: Optional[bool] = None,
    ) -> adminv1.Member:
        """
        Updates specified organization member.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.
        :param role_id:
            The identifier of the role.

            This is currently limited to `member`, `admin`, and `owner`.
        :param allow_missing:
            If set to true, and the member is not found, a new member will be created.
        """
        req = Request(
            "admin.organizations.updateMember",
            "PATCH",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members/{util.quote_path(user_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if allow_missing:
            req.set_query("allowMissing", allow_missing)
        if role_id is not UNDEFINED:
            body["roleId"] = role_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Member.__json_decode__)

    def remove_member(
        self,
        organization_id: str,
        user_id: str,
    ) -> apiv1.EmptyResponse:
        """
        Deletes specified organization member.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.organizations.removeMember",
            "DELETE",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members/{util.quote_path(user_id)}",
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
        show_deleted: Optional[bool] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListOrganizationsResponse:
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
            - `createTime`
            - `deleteTime`
        :param show_deleted:
            Whether to show deleted organizations.
        :param view:
            The organization view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.organizations.list", "GET", "/admin/v1/organizations")
        req.set_idempotent(True)

        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)
        if show_deleted:
            req.set_query("showDeleted", show_deleted)
        if view:
            req.set_query("view", view)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.ListOrganizationsResponse.__json_decode__)

    async def create(
        self,
        *,
        unique_id: Optional[str] = None,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        email_verified: Optional[bool] = None,
        phone_number: Optional[str] = None,
        phone_number_verified: Optional[bool] = None,
        image_url: Optional[str] = None,
        currency_code: Optional[str] = None,
        language_code: Optional[str] = None,
        region_code: Optional[str] = None,
        time_zone: Optional[str] = None,
        address: Optional[commonv1.Address] = None,
        signup_time: Optional[datetime.datetime] = None,
        disabled: Optional[bool] = None,
    ) -> adminv1.Organization:
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
        :param email_verified:
            Whether the organization's email address has been verified.
        :param phone_number:
            The E164 phone number for the organization (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the organization's phone number has been verified.
        :param image_url:
            The photo/avatar URL of the organization.

            The maximum length is 2000 characters.
        :param currency_code:
            The default ISO-4217 currency code for the organization (e.g. `USD`).
        :param language_code:
            The IETF BCP-47 language code for the organization (e.g. `en`).
        :param region_code:
            The country/region code for the organization (e.g. `US`).
        :param time_zone:
            The IANA time zone for the organization (e.g. `America/New_York`).
        :param address:
            The billing address for the organization.
        :param signup_time:
            The sign-up time for the organization.
        :param disabled:
            Whether the organization is disabled.
        """
        req = Request("admin.organizations.create", "POST", "/admin/v1/organizations")
        body: Dict[str, Any] = {}

        if unique_id:
            body["uniqueId"] = unique_id
        if display_name:
            body["displayName"] = display_name
        if email:
            body["email"] = email
        if email_verified:
            body["emailVerified"] = email_verified
        if phone_number:
            body["phoneNumber"] = phone_number
        if phone_number_verified:
            body["phoneNumberVerified"] = phone_number_verified
        if image_url:
            body["imageUrl"] = image_url
        if currency_code:
            body["currencyCode"] = currency_code
        if language_code:
            body["languageCode"] = language_code
        if region_code:
            body["regionCode"] = region_code
        if time_zone:
            body["timeZone"] = time_zone
        if address:
            body["address"] = address
        if signup_time:
            body["signupTime"] = signup_time
        if disabled:
            body["disabled"] = disabled

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    async def get(
        self,
        organization_id: str,
    ) -> adminv1.Organization:
        """
        Retrieves specified organization.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "admin.organizations.get",
            "GET",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    async def update(
        self,
        organization_id: str,
        *,
        unique_id: Union[Optional[str], Undefined] = UNDEFINED,
        display_name: Union[Optional[str], Undefined] = UNDEFINED,
        email: Union[Optional[str], Undefined] = UNDEFINED,
        email_verified: Union[Optional[bool], Undefined] = UNDEFINED,
        phone_number: Union[Optional[str], Undefined] = UNDEFINED,
        phone_number_verified: Union[Optional[bool], Undefined] = UNDEFINED,
        image_url: Union[Optional[str], Undefined] = UNDEFINED,
        currency_code: Union[Optional[str], Undefined] = UNDEFINED,
        language_code: Union[Optional[str], Undefined] = UNDEFINED,
        region_code: Union[Optional[str], Undefined] = UNDEFINED,
        time_zone: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        signup_time: Union[Optional[datetime.datetime], Undefined] = UNDEFINED,
        disabled: Union[Optional[bool], Undefined] = UNDEFINED,
        allow_missing: Optional[bool] = None,
    ) -> adminv1.Organization:
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
        :param email_verified:
            Whether the organization's email address has been verified.
        :param phone_number:
            The E164 phone number for the organization (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the organization's phone number has been verified.
        :param image_url:
            The photo/avatar URL of the organization.

            The maximum length is 2000 characters.
        :param currency_code:
            The default ISO-4217 currency code for the organization (e.g. `USD`).
        :param language_code:
            The IETF BCP-47 language code for the organization (e.g. `en`).
        :param region_code:
            The country/region code for the organization (e.g. `US`).
        :param time_zone:
            The IANA time zone for the organization (e.g. `America/New_York`).
        :param address:
            The billing address for the organization.
        :param signup_time:
            The sign-up time for the organization.
        :param disabled:
            Whether the organization is disabled.
        :param allow_missing:
            If set to true, and the organization is not found, a new organization will be created.

            You must use the unique identifier for the identifier when this is true.
        """
        req = Request(
            "admin.organizations.update",
            "PATCH",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if allow_missing:
            req.set_query("allowMissing", allow_missing)
        if unique_id is not UNDEFINED:
            body["uniqueId"] = unique_id
        if display_name is not UNDEFINED:
            body["displayName"] = display_name
        if email is not UNDEFINED:
            body["email"] = email
        if email_verified is not UNDEFINED:
            body["emailVerified"] = email_verified
        if phone_number is not UNDEFINED:
            body["phoneNumber"] = phone_number
        if phone_number_verified is not UNDEFINED:
            body["phoneNumberVerified"] = phone_number_verified
        if image_url is not UNDEFINED:
            body["imageUrl"] = image_url
        if currency_code is not UNDEFINED:
            body["currencyCode"] = currency_code
        if language_code is not UNDEFINED:
            body["languageCode"] = language_code
        if region_code is not UNDEFINED:
            body["regionCode"] = region_code
        if time_zone is not UNDEFINED:
            body["timeZone"] = time_zone
        if address is not UNDEFINED:
            body["address"] = address
        if signup_time is not UNDEFINED:
            body["signupTime"] = signup_time
        if disabled is not UNDEFINED:
            body["disabled"] = disabled

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    async def delete(
        self,
        organization_id: str,
    ) -> adminv1.Organization:
        """
        Marks specified organization for deletion.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "admin.organizations.delete",
            "DELETE",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}",
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    async def undelete(
        self,
        organization_id: str,
    ) -> adminv1.Organization:
        """
        Un-marks specified organization for deletion.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "admin.organizations.undelete",
            "POST",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}:undelete",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    async def connect(
        self,
        organization_id: str,
        *,
        connection_id: str,
        external_id: Optional[str] = None,
    ) -> adminv1.Organization:
        """
        Connect specified organization to external account.

        :param organization_id:
            The organization identifier.
        :param connection_id:
            The identifier of the connection.
        :param external_id:
            The external identifier of the organization to connect.

            On create if this is empty a new external organization will
            be created if the connection supports it.
        """
        req = Request(
            "admin.organizations.connect",
            "POST",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}:connect",
        )
        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
        if external_id:
            body["externalId"] = external_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    async def disconnect(
        self,
        organization_id: str,
        *,
        connection_id: str,
        delete_external_account: Optional[bool] = None,
    ) -> adminv1.Organization:
        """
        Disconnect specified organization from external account.

        This will delete all the data associated with the connected account, including
        payment methods, invoices, and subscriptions.

        If the delete external account option is enabled it will also attempt to delete
        the external account (e.g. Stripe Customer object).

        WARNING: This can irreversibly destroy data and should be
        used with extreme caution.

        :param organization_id:
            The organization identifier.
        :param connection_id:
            The identifier of the connection.
        :param delete_external_account:
            Whether to attempt to delete the external account and all
            it's associated data (e.g. Stripe Customer object).
        """
        req = Request(
            "admin.organizations.disconnect",
            "POST",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}:disconnect",
        )
        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
        if delete_external_account:
            body["deleteExternalAccount"] = delete_external_account

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Organization.__json_decode__)

    async def list_members(
        self,
        organization_id: str,
        *,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> adminv1.ListMembersResponse:
        """
        Lists organization members.

        :param organization_id:
            The identifier of the organization.
        :param page_size:
            The maximum number of members to return. The API may return fewer than
            this value.

            If unspecified, at most 20 members will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list members call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list members must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `createTime`
            - `updateTime`
        """
        req = Request(
            "admin.organizations.listMembers",
            "GET",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members",
        )
        req.set_idempotent(True)

        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.ListMembersResponse.__json_decode__)

    async def add_member(
        self,
        organization_id: str,
        *,
        user_id: Optional[str] = None,
        role_id: Optional[str] = None,
    ) -> adminv1.Member:
        """
        Creates a new organization member.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.
        :param role_id:
            The identifier of the role.

            This is currently limited to `member`, `admin`, and `owner`.
        """
        req = Request(
            "admin.organizations.addMember",
            "POST",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members",
        )
        body: Dict[str, Any] = {}

        if user_id:
            body["userId"] = user_id
        if role_id:
            body["roleId"] = role_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Member.__json_decode__)

    async def get_member(
        self,
        organization_id: str,
        user_id: str,
    ) -> adminv1.Member:
        """
        Retrieves specified organization member.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.organizations.getMember",
            "GET",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members/{util.quote_path(user_id)}",
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Member.__json_decode__)

    async def update_member(
        self,
        organization_id: str,
        user_id: str,
        *,
        role_id: Union[str, Undefined] = UNDEFINED,
        allow_missing: Optional[bool] = None,
    ) -> adminv1.Member:
        """
        Updates specified organization member.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.
        :param role_id:
            The identifier of the role.

            This is currently limited to `member`, `admin`, and `owner`.
        :param allow_missing:
            If set to true, and the member is not found, a new member will be created.
        """
        req = Request(
            "admin.organizations.updateMember",
            "PATCH",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members/{util.quote_path(user_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if allow_missing:
            req.set_query("allowMissing", allow_missing)
        if role_id is not UNDEFINED:
            body["roleId"] = role_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Member.__json_decode__)

    async def remove_member(
        self,
        organization_id: str,
        user_id: str,
    ) -> apiv1.EmptyResponse:
        """
        Deletes specified organization member.

        :param organization_id:
            The identifier of the organization.
        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.organizations.removeMember",
            "DELETE",
            f"/admin/v1/organizations/{util.quote_path(organization_id)}/members/{util.quote_path(user_id)}",
        )
        res = await self._transport.execute(req)

        return res.decode_body(apiv1.EmptyResponse.__json_decode__)
