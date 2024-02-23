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
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        show_deleted: Optional[bool] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListUsersResponse:
        """
        Lists users.

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
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `displayName`
            - `email`
            - `createTime`
            - `deleteTime`
        :param show_deleted:
            Whether to show deleted users.
        :param view:
            The User view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.users.list", "GET", "/admin/v1/users")
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
        Creates a new user.

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
            The billing address for the user.
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
        Retrieves specified user.

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
        Updates specified user.

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
            The billing address for the user.
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
        Marks specified user for deletion.

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
        Un-marks specified user for deletion.

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

    def connect(
        self,
        user_id: str,
        *,
        connection_id: str,
        external_id: Optional[str] = None,
    ) -> adminv1.User:
        """
        Connect specified user to external account.

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

    def disconnect(
        self,
        user_id: str,
        *,
        connection_id: str,
        delete_external_account: Optional[bool] = None,
    ) -> adminv1.User:
        """
        Disconnect specified user from external account.

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
        Import user from external identity provider if they don't already
        exist.

        If the user already exists in UserHub, this is a no-op.

        :param user_id:
            The identifier of the user.

            This must be in the format `<externalId>@<connectionId>` where
            `externalId` is the identity provider user identifier and
            and `connectionId` is the User Provider connection identifier.
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
    ) -> adminv1.CreatePortalSessionResponse:
        """
        Create Portal session.

        :param user_id:
            The user ID.

            In addition to supporting the UserHub user ID,
            you can also pass in the User Provider external identifier in the
            format `<externalId>@<connectionId>` and if the user doesn't
            exist in UserHub they will automatically be imported.
        :param portal_url:
            The portal URL, this is the target URL on the portal site.

            If not defined the root URL for the portal will be used.
        :param return_url:
            The URL the user should be sent to when they want to return to
            the app (e.g. cancel checkout).

            If not defined the app URL will be used.
        :param success_url:
            The URl the user should be sent after they successfully complete
            an action (e.g. checkout).

            If not defined the return URL will be used.
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
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        show_deleted: Optional[bool] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListUsersResponse:
        """
        Lists users.

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
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `displayName`
            - `email`
            - `createTime`
            - `deleteTime`
        :param show_deleted:
            Whether to show deleted users.
        :param view:
            The User view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.users.list", "GET", "/admin/v1/users")
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
        Creates a new user.

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
            The billing address for the user.
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
        Retrieves specified user.

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
        Updates specified user.

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
            The billing address for the user.
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
        Marks specified user for deletion.

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
        Un-marks specified user for deletion.

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

    async def connect(
        self,
        user_id: str,
        *,
        connection_id: str,
        external_id: Optional[str] = None,
    ) -> adminv1.User:
        """
        Connect specified user to external account.

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

    async def disconnect(
        self,
        user_id: str,
        *,
        connection_id: str,
        delete_external_account: Optional[bool] = None,
    ) -> adminv1.User:
        """
        Disconnect specified user from external account.

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
        Import user from external identity provider if they don't already
        exist.

        If the user already exists in UserHub, this is a no-op.

        :param user_id:
            The identifier of the user.

            This must be in the format `<externalId>@<connectionId>` where
            `externalId` is the identity provider user identifier and
            and `connectionId` is the User Provider connection identifier.
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
    ) -> adminv1.CreatePortalSessionResponse:
        """
        Create Portal session.

        :param user_id:
            The user ID.

            In addition to supporting the UserHub user ID,
            you can also pass in the User Provider external identifier in the
            format `<externalId>@<connectionId>` and if the user doesn't
            exist in UserHub they will automatically be imported.
        :param portal_url:
            The portal URL, this is the target URL on the portal site.

            If not defined the root URL for the portal will be used.
        :param return_url:
            The URL the user should be sent to when they want to return to
            the app (e.g. cancel checkout).

            If not defined the app URL will be used.
        :param success_url:
            The URl the user should be sent after they successfully complete
            an action (e.g. checkout).

            If not defined the return URL will be used.
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

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.CreatePortalSessionResponse.__json_decode__)
