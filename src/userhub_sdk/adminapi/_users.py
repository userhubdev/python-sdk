# Code generated. DO NOT EDIT.

import datetime
from typing import Any, Dict, Optional, Union

from userhub_sdk import adminv1, commonv1
from userhub_sdk._internal import util
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport
from userhub_sdk.types import UNDEFINED, Undefined


class Users:
    """
    The user methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def list(
        self,
        *,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        show_deleted: Optional[bool] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListUsersResponse:
        """
        List users.

        :param display_name:
            Filter the results by display name.

            To enable prefix filtering append `*` to the end of the value
            and ensure you provide at least 3 characters excluding the
            wildcard.

            This filter is case-insensitivity.
        :param email:
            Filter the results by email address.

            To enable prefix filtering append `*` to the end of the value
            and ensure you provide at least 3 characters excluding the
            wildcard.

            This filter is case-insensitivity.
        :param page_size:
            The maximum number of users to return. The API may return fewer than
            this value.

            If unspecified, at most 20 users will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list users call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list users must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by.
        :param show_deleted:
            Whether to show deleted users.
        :param view:
            The User view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.users.list", "GET", "/admin/v1/users")
        req.set_idempotent(True)

        if display_name:
            req.set_query("displayName", display_name)
        if email:
            req.set_query("email", email)
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

        return res.decode_body(adminv1.ListUsersResponse.__json_decode__)

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
    ) -> adminv1.User:
        """
        Create a user.

        :param unique_id:
            The client defined unique identifier of the user account.

            It is restricted to letters, numbers, underscores, and hyphens,
            with the first character a letter or a number, and a 255
            character maximum.

            ID's starting with `usr_` are reserved.
        :param display_name:
            The human-readable display name of the user.

            The maximum length is 200 characters.
        :param email:
            The email address of the user.

            The maximum length is 320 characters.
        :param email_verified:
            Whether the user's email address has been verified.
        :param phone_number:
            The E164 phone number for the user (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the user's phone number has been verified.
        :param image_url:
            The photo/avatar URL of the user.

            The maximum length is 2000 characters.
        :param currency_code:
            The default ISO-4217 currency code for the user (e.g. `USD`).
        :param language_code:
            The IETF BCP-47 language code for the user (e.g. `en`).
        :param region_code:
            The country/region code for the user (e.g. `US`).
        :param time_zone:
            The IANA time zone for the user (e.g. `America/New_York`).
        :param address:
            The default address for the user.
        :param signup_time:
            The sign-up time for the user.
        :param disabled:
            Whether the user is disabled.
        """
        req = Request("admin.users.create", "POST", "/admin/v1/users")
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

        return res.decode_body(adminv1.User.__json_decode__)

    def get(
        self,
        user_id: str,
    ) -> adminv1.User:
        """
        Get a user.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.get", "GET", f"/admin/v1/users/{util.quote_path(user_id)}"
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    def update(
        self,
        user_id: str,
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
    ) -> adminv1.User:
        """
        Update a user.

        :param user_id:
            The identifier of the user.
        :param unique_id:
            The client defined unique identifier of the user account.

            It is restricted to letters, numbers, underscores, and hyphens,
            with the first character a letter or a number, and a 255
            character maximum.

            ID's starting with `usr_` are reserved.
        :param display_name:
            The human-readable display name of the user.

            The maximum length is 200 characters.
        :param email:
            The email address of the user.

            The maximum length is 320 characters.
        :param email_verified:
            Whether the user's email address has been verified.
        :param phone_number:
            The E164 phone number for the user (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the user's phone number has been verified.
        :param image_url:
            The photo/avatar URL of the user.

            The maximum length is 2000 characters.
        :param currency_code:
            The default ISO-4217 currency code for the user (e.g. `USD`).
        :param language_code:
            The IETF BCP-47 language code for the user (e.g. `en`).
        :param region_code:
            The country/region code for the user (e.g. `US`).
        :param time_zone:
            The IANA time zone for the user (e.g. `America/New_York`).
        :param address:
            The default address for the user.
        :param signup_time:
            The sign-up time for the user.
        :param disabled:
            Whether the user is disabled.
        :param allow_missing:
            If set to true, and the user is not found, a new user will be created.

            You must use the unique identifier for the identifier when this is true.
        """
        req = Request(
            "admin.users.update", "PATCH", f"/admin/v1/users/{util.quote_path(user_id)}"
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

        return res.decode_body(adminv1.User.__json_decode__)

    def delete(
        self,
        user_id: str,
    ) -> adminv1.User:
        """
        Delete a user.

        This marks the user for deletion and can be restored during
        a grace period.

        To immediately delete a user, you must also call purge user.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.delete",
            "DELETE",
            f"/admin/v1/users/{util.quote_path(user_id)}",
        )
        res = self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    def undelete(
        self,
        user_id: str,
    ) -> adminv1.User:
        """
        Restore a user.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.undelete",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:undelete",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    def purge(
        self,
        user_id: str,
    ) -> adminv1.PurgeUserResponse:
        """
        Purge a deleted user.

        The user must be marked for deletion before it can be purged.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.purge",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:purge",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.PurgeUserResponse.__json_decode__)

    def connect(
        self,
        user_id: str,
        *,
        connection_id: str,
        external_id: Optional[str] = None,
    ) -> adminv1.User:
        """
        Connect a user to an external account.

        :param user_id:
            The user identifier.
        :param connection_id:
            The identifier of the connection.
        :param external_id:
            The external identifier of the user to connect.

            On create if this is empty a new external user will
            be created if the connection supports it.
        """
        req = Request(
            "admin.users.connect",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:connect",
        )
        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
        if external_id:
            body["externalId"] = external_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    def update_connection(
        self,
        user_id: str,
        *,
        connection_id: str,
        display_name: Union[Optional[str], Undefined] = UNDEFINED,
        email: Union[Optional[str], Undefined] = UNDEFINED,
        email_verified: Union[Optional[bool], Undefined] = UNDEFINED,
        phone_number: Union[Optional[str], Undefined] = UNDEFINED,
        phone_number_verified: Union[Optional[bool], Undefined] = UNDEFINED,
        currency_code: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        disabled: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> adminv1.User:
        """
        Update a user's external account.

        :param user_id:
            The identifier of the user.
        :param connection_id:
            The system-assigned identifier for the connection of the external account.
        :param display_name:
            The human-readable display name of the external account.

            The maximum length is 200 characters.

            This might be further restricted by the external provider.
        :param email:
            The email address of the external account.

            The maximum length is 320 characters.

            This might be further restricted by the external provider.
        :param email_verified:
            Whether the external account's email address has been verified.
        :param phone_number:
            The E164 phone number for the external account (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the external account's phone number has been verified.
        :param currency_code:
            The default ISO-4217 currency code for the external account (e.g. `USD`).
        :param address:
            The billing address for the external account.
        :param disabled:
            Whether the external account is disabled.
        """
        req = Request(
            "admin.users.updateConnection",
            "PATCH",
            f"/admin/v1/users/{util.quote_path(user_id)}:updateConnection",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
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
        if currency_code is not UNDEFINED:
            body["currencyCode"] = currency_code
        if address is not UNDEFINED:
            body["address"] = address
        if disabled is not UNDEFINED:
            body["disabled"] = disabled

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    def disconnect(
        self,
        user_id: str,
        *,
        connection_id: str,
        delete_external_account: Optional[bool] = None,
    ) -> adminv1.User:
        """
        Disconnect a user from an external account.

        This will delete all the data associated with the connected account, including
        payment methods, invoices, and subscriptions.

        If the delete external account option is enabled it will also attempt to delete
        the external account (e.g. Stripe Customer object).

        WARNING: This can irreversibly destroy data and should be
        used with extreme caution.

        :param user_id:
            The user identifier.
        :param connection_id:
            The identifier of the connection.
        :param delete_external_account:
            Whether to attempt to delete the external account and all
            it's associated data (e.g. Stripe Customer object).
        """
        req = Request(
            "admin.users.disconnect",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:disconnect",
        )
        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
        if delete_external_account:
            body["deleteExternalAccount"] = delete_external_account

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    def import_account(
        self,
        user_id: str,
    ) -> adminv1.User:
        """
        Import a user from a user provider.

        If the user already exists, this is a no-op.

        :param user_id:
            The identifier of the user.

            This must be in the format `<externalId>@<connectionId>` where
            `externalId` is the identity provider user identifier and
            and `connectionId` is the User provider connection identifier.
        """
        req = Request(
            "admin.users.importAccount",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:import",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    def report_event(
        self,
        user_id: str,
        *,
        type: Optional[str] = None,
        wait: Optional[bool] = None,
    ) -> adminv1.ReportUserEventResponse:
        """
        Report a user event.

        If the `<externalId>@<connectionId>` user identifier syntax is
        used and the user doesn't exist, they will be imported.

        By default, the event is processed asynchronously.

        :param user_id:
            The identifier of the user.

            This can be in the format `<externalId>@<connectionId>` where
            `externalId` is the identity provider user identifier and
            and `connectionId` is the User provider connection identifier.
        :param type:
            The event type.

            If not specified, this defaults to `CHANGED`.
        :param wait:
            Process the user action synchronously.

            Otherwise the action is processed in the background and errors
            won't be returned.
        """
        req = Request(
            "admin.users.reportEvent",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:event",
        )
        body: Dict[str, Any] = {}

        if type:
            body["type"] = type
        if wait:
            body["wait"] = wait

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.ReportUserEventResponse.__json_decode__)

    def create_api_session(
        self,
        user_id: str,
    ) -> adminv1.CreateApiSessionResponse:
        """
        Create a User API session.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.createApiSession",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:createApiSession",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.CreateApiSessionResponse.__json_decode__)

    def create_portal_session(
        self,
        user_id: str,
        *,
        portal_url: Optional[str] = None,
        return_url: Optional[str] = None,
        success_url: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> adminv1.CreatePortalSessionResponse:
        """
        Create a Portal session.

        :param user_id:
            The user ID.

            In addition to supporting the UserHub user ID,
            you can also pass in the User provider external identifier in the
            format `<externalId>@<connectionId>` and if the user doesn't
            exist in UserHub they will automatically be imported.
        :param portal_url:
            The Portal URL, this is the target URL on the portal site.

            If not defined the root URL for the portal will be used.

            This does not need to be the full URL, you have the option
            of passing in a path instead (e.g. `/`).

            You also have the option of including the `{accountId}`
            string in the path/URL which will be replaced with either the
            UserHub user ID (if `organizationId` is not specified)
            or the UserHub organization ID (if specified).

            Examples:
            * `/{accountId}` - the billing dashboard
            * `/{accountId}/cancel` - cancel current plan
            * `/{accountId}/members` - manage organization members
            * `/{accountId}/invite` - invite a user to an organization
        :param return_url:
            The URL the user should be sent to when they want to return to
            the app (e.g. cancel checkout).

            If not defined the app URL will be used.
        :param success_url:
            The URL the user should be sent after they successfully complete
            an action (e.g. checkout).

            If not defined the return URL will be used.
        :param organization_id:
            The organization ID.

            When specified the `{accountId}` in the `portalUrl` will be
            replaced with the organization ID, otherwise the user ID
            will be used.
        """
        req = Request(
            "admin.users.createPortalSession",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:createPortalSession",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if portal_url:
            body["portalUrl"] = portal_url
        if return_url:
            body["returnUrl"] = return_url
        if success_url:
            body["successUrl"] = success_url
        if organization_id:
            body["organizationId"] = organization_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.CreatePortalSessionResponse.__json_decode__)


class AsyncUsers:
    """
    The user methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list(
        self,
        *,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        show_deleted: Optional[bool] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListUsersResponse:
        """
        List users.

        :param display_name:
            Filter the results by display name.

            To enable prefix filtering append `*` to the end of the value
            and ensure you provide at least 3 characters excluding the
            wildcard.

            This filter is case-insensitivity.
        :param email:
            Filter the results by email address.

            To enable prefix filtering append `*` to the end of the value
            and ensure you provide at least 3 characters excluding the
            wildcard.

            This filter is case-insensitivity.
        :param page_size:
            The maximum number of users to return. The API may return fewer than
            this value.

            If unspecified, at most 20 users will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list users call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list users must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by.
        :param show_deleted:
            Whether to show deleted users.
        :param view:
            The User view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.users.list", "GET", "/admin/v1/users")
        req.set_idempotent(True)

        if display_name:
            req.set_query("displayName", display_name)
        if email:
            req.set_query("email", email)
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

        return res.decode_body(adminv1.ListUsersResponse.__json_decode__)

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
    ) -> adminv1.User:
        """
        Create a user.

        :param unique_id:
            The client defined unique identifier of the user account.

            It is restricted to letters, numbers, underscores, and hyphens,
            with the first character a letter or a number, and a 255
            character maximum.

            ID's starting with `usr_` are reserved.
        :param display_name:
            The human-readable display name of the user.

            The maximum length is 200 characters.
        :param email:
            The email address of the user.

            The maximum length is 320 characters.
        :param email_verified:
            Whether the user's email address has been verified.
        :param phone_number:
            The E164 phone number for the user (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the user's phone number has been verified.
        :param image_url:
            The photo/avatar URL of the user.

            The maximum length is 2000 characters.
        :param currency_code:
            The default ISO-4217 currency code for the user (e.g. `USD`).
        :param language_code:
            The IETF BCP-47 language code for the user (e.g. `en`).
        :param region_code:
            The country/region code for the user (e.g. `US`).
        :param time_zone:
            The IANA time zone for the user (e.g. `America/New_York`).
        :param address:
            The default address for the user.
        :param signup_time:
            The sign-up time for the user.
        :param disabled:
            Whether the user is disabled.
        """
        req = Request("admin.users.create", "POST", "/admin/v1/users")
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

        return res.decode_body(adminv1.User.__json_decode__)

    async def get(
        self,
        user_id: str,
    ) -> adminv1.User:
        """
        Get a user.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.get", "GET", f"/admin/v1/users/{util.quote_path(user_id)}"
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    async def update(
        self,
        user_id: str,
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
    ) -> adminv1.User:
        """
        Update a user.

        :param user_id:
            The identifier of the user.
        :param unique_id:
            The client defined unique identifier of the user account.

            It is restricted to letters, numbers, underscores, and hyphens,
            with the first character a letter or a number, and a 255
            character maximum.

            ID's starting with `usr_` are reserved.
        :param display_name:
            The human-readable display name of the user.

            The maximum length is 200 characters.
        :param email:
            The email address of the user.

            The maximum length is 320 characters.
        :param email_verified:
            Whether the user's email address has been verified.
        :param phone_number:
            The E164 phone number for the user (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the user's phone number has been verified.
        :param image_url:
            The photo/avatar URL of the user.

            The maximum length is 2000 characters.
        :param currency_code:
            The default ISO-4217 currency code for the user (e.g. `USD`).
        :param language_code:
            The IETF BCP-47 language code for the user (e.g. `en`).
        :param region_code:
            The country/region code for the user (e.g. `US`).
        :param time_zone:
            The IANA time zone for the user (e.g. `America/New_York`).
        :param address:
            The default address for the user.
        :param signup_time:
            The sign-up time for the user.
        :param disabled:
            Whether the user is disabled.
        :param allow_missing:
            If set to true, and the user is not found, a new user will be created.

            You must use the unique identifier for the identifier when this is true.
        """
        req = Request(
            "admin.users.update", "PATCH", f"/admin/v1/users/{util.quote_path(user_id)}"
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

        return res.decode_body(adminv1.User.__json_decode__)

    async def delete(
        self,
        user_id: str,
    ) -> adminv1.User:
        """
        Delete a user.

        This marks the user for deletion and can be restored during
        a grace period.

        To immediately delete a user, you must also call purge user.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.delete",
            "DELETE",
            f"/admin/v1/users/{util.quote_path(user_id)}",
        )
        res = await self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    async def undelete(
        self,
        user_id: str,
    ) -> adminv1.User:
        """
        Restore a user.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.undelete",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:undelete",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    async def purge(
        self,
        user_id: str,
    ) -> adminv1.PurgeUserResponse:
        """
        Purge a deleted user.

        The user must be marked for deletion before it can be purged.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.purge",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:purge",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.PurgeUserResponse.__json_decode__)

    async def connect(
        self,
        user_id: str,
        *,
        connection_id: str,
        external_id: Optional[str] = None,
    ) -> adminv1.User:
        """
        Connect a user to an external account.

        :param user_id:
            The user identifier.
        :param connection_id:
            The identifier of the connection.
        :param external_id:
            The external identifier of the user to connect.

            On create if this is empty a new external user will
            be created if the connection supports it.
        """
        req = Request(
            "admin.users.connect",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:connect",
        )
        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
        if external_id:
            body["externalId"] = external_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    async def update_connection(
        self,
        user_id: str,
        *,
        connection_id: str,
        display_name: Union[Optional[str], Undefined] = UNDEFINED,
        email: Union[Optional[str], Undefined] = UNDEFINED,
        email_verified: Union[Optional[bool], Undefined] = UNDEFINED,
        phone_number: Union[Optional[str], Undefined] = UNDEFINED,
        phone_number_verified: Union[Optional[bool], Undefined] = UNDEFINED,
        currency_code: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        disabled: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> adminv1.User:
        """
        Update a user's external account.

        :param user_id:
            The identifier of the user.
        :param connection_id:
            The system-assigned identifier for the connection of the external account.
        :param display_name:
            The human-readable display name of the external account.

            The maximum length is 200 characters.

            This might be further restricted by the external provider.
        :param email:
            The email address of the external account.

            The maximum length is 320 characters.

            This might be further restricted by the external provider.
        :param email_verified:
            Whether the external account's email address has been verified.
        :param phone_number:
            The E164 phone number for the external account (e.g. `+12125550123`).
        :param phone_number_verified:
            Whether the external account's phone number has been verified.
        :param currency_code:
            The default ISO-4217 currency code for the external account (e.g. `USD`).
        :param address:
            The billing address for the external account.
        :param disabled:
            Whether the external account is disabled.
        """
        req = Request(
            "admin.users.updateConnection",
            "PATCH",
            f"/admin/v1/users/{util.quote_path(user_id)}:updateConnection",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
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
        if currency_code is not UNDEFINED:
            body["currencyCode"] = currency_code
        if address is not UNDEFINED:
            body["address"] = address
        if disabled is not UNDEFINED:
            body["disabled"] = disabled

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    async def disconnect(
        self,
        user_id: str,
        *,
        connection_id: str,
        delete_external_account: Optional[bool] = None,
    ) -> adminv1.User:
        """
        Disconnect a user from an external account.

        This will delete all the data associated with the connected account, including
        payment methods, invoices, and subscriptions.

        If the delete external account option is enabled it will also attempt to delete
        the external account (e.g. Stripe Customer object).

        WARNING: This can irreversibly destroy data and should be
        used with extreme caution.

        :param user_id:
            The user identifier.
        :param connection_id:
            The identifier of the connection.
        :param delete_external_account:
            Whether to attempt to delete the external account and all
            it's associated data (e.g. Stripe Customer object).
        """
        req = Request(
            "admin.users.disconnect",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:disconnect",
        )
        body: Dict[str, Any] = {}

        if connection_id:
            body["connectionId"] = connection_id
        if delete_external_account:
            body["deleteExternalAccount"] = delete_external_account

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    async def import_account(
        self,
        user_id: str,
    ) -> adminv1.User:
        """
        Import a user from a user provider.

        If the user already exists, this is a no-op.

        :param user_id:
            The identifier of the user.

            This must be in the format `<externalId>@<connectionId>` where
            `externalId` is the identity provider user identifier and
            and `connectionId` is the User provider connection identifier.
        """
        req = Request(
            "admin.users.importAccount",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:import",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.User.__json_decode__)

    async def report_event(
        self,
        user_id: str,
        *,
        type: Optional[str] = None,
        wait: Optional[bool] = None,
    ) -> adminv1.ReportUserEventResponse:
        """
        Report a user event.

        If the `<externalId>@<connectionId>` user identifier syntax is
        used and the user doesn't exist, they will be imported.

        By default, the event is processed asynchronously.

        :param user_id:
            The identifier of the user.

            This can be in the format `<externalId>@<connectionId>` where
            `externalId` is the identity provider user identifier and
            and `connectionId` is the User provider connection identifier.
        :param type:
            The event type.

            If not specified, this defaults to `CHANGED`.
        :param wait:
            Process the user action synchronously.

            Otherwise the action is processed in the background and errors
            won't be returned.
        """
        req = Request(
            "admin.users.reportEvent",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:event",
        )
        body: Dict[str, Any] = {}

        if type:
            body["type"] = type
        if wait:
            body["wait"] = wait

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.ReportUserEventResponse.__json_decode__)

    async def create_api_session(
        self,
        user_id: str,
    ) -> adminv1.CreateApiSessionResponse:
        """
        Create a User API session.

        :param user_id:
            The identifier of the user.
        """
        req = Request(
            "admin.users.createApiSession",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:createApiSession",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.CreateApiSessionResponse.__json_decode__)

    async def create_portal_session(
        self,
        user_id: str,
        *,
        portal_url: Optional[str] = None,
        return_url: Optional[str] = None,
        success_url: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> adminv1.CreatePortalSessionResponse:
        """
        Create a Portal session.

        :param user_id:
            The user ID.

            In addition to supporting the UserHub user ID,
            you can also pass in the User provider external identifier in the
            format `<externalId>@<connectionId>` and if the user doesn't
            exist in UserHub they will automatically be imported.
        :param portal_url:
            The Portal URL, this is the target URL on the portal site.

            If not defined the root URL for the portal will be used.

            This does not need to be the full URL, you have the option
            of passing in a path instead (e.g. `/`).

            You also have the option of including the `{accountId}`
            string in the path/URL which will be replaced with either the
            UserHub user ID (if `organizationId` is not specified)
            or the UserHub organization ID (if specified).

            Examples:
            * `/{accountId}` - the billing dashboard
            * `/{accountId}/cancel` - cancel current plan
            * `/{accountId}/members` - manage organization members
            * `/{accountId}/invite` - invite a user to an organization
        :param return_url:
            The URL the user should be sent to when they want to return to
            the app (e.g. cancel checkout).

            If not defined the app URL will be used.
        :param success_url:
            The URL the user should be sent after they successfully complete
            an action (e.g. checkout).

            If not defined the return URL will be used.
        :param organization_id:
            The organization ID.

            When specified the `{accountId}` in the `portalUrl` will be
            replaced with the organization ID, otherwise the user ID
            will be used.
        """
        req = Request(
            "admin.users.createPortalSession",
            "POST",
            f"/admin/v1/users/{util.quote_path(user_id)}:createPortalSession",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if portal_url:
            body["portalUrl"] = portal_url
        if return_url:
            body["returnUrl"] = return_url
        if success_url:
            body["successUrl"] = success_url
        if organization_id:
            body["organizationId"] = organization_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.CreatePortalSessionResponse.__json_decode__)
