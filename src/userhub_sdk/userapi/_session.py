# Code generated. DO NOT EDIT.

from typing import Any, Dict, Optional

from userhub_sdk import userv1
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport


class Session:
    """
    The Portal session.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def get(
        self,
    ) -> userv1.Session:
        """
        Get details about the current session.
        """
        req = Request("user.session.get", "GET", "/user/v1/session")
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Session.__json_decode__)

    def exchange_token(
        self,
        *,
        token: str,
    ) -> userv1.ExchangeSessionTokenResponse:
        """
        Exchange an ID token from an IdP for an access token.

        :param token:
            The IdP ID token which is used to authenticated the user.
        """
        req = Request(
            "user.session.exchangeToken", "POST", "/user/v1/session:exchangeToken"
        )
        body: Dict[str, Any] = {}

        if token:
            body["token"] = token

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.ExchangeSessionTokenResponse.__json_decode__)

    def create_portal(
        self,
        *,
        organization_id: Optional[str] = None,
        portal_url: Optional[str] = None,
        return_url: Optional[str] = None,
        success_url: Optional[str] = None,
    ) -> userv1.CreatePortalSessionResponse:
        """
        Create a new Portal session.

        :param organization_id:
            The identifier of the organization.

            When specified the `{accountId}` in the `portalUrl` will be
            replaced with the organization ID, otherwise the user ID
            will be used.
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
            * `/{accountId}/checkout` - start a checkout
            * `/{accountId}/checkout/<some-plan-id>` - start a checkout with a specified plan
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
        """
        req = Request(
            "user.session.createPortal", "POST", "/user/v1/session:createPortal"
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if portal_url:
            body["portalUrl"] = portal_url
        if return_url:
            body["returnUrl"] = return_url
        if success_url:
            body["successUrl"] = success_url

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.CreatePortalSessionResponse.__json_decode__)


class AsyncSession:
    """
    The Portal session.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get(
        self,
    ) -> userv1.Session:
        """
        Get details about the current session.
        """
        req = Request("user.session.get", "GET", "/user/v1/session")
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Session.__json_decode__)

    async def exchange_token(
        self,
        *,
        token: str,
    ) -> userv1.ExchangeSessionTokenResponse:
        """
        Exchange an ID token from an IdP for an access token.

        :param token:
            The IdP ID token which is used to authenticated the user.
        """
        req = Request(
            "user.session.exchangeToken", "POST", "/user/v1/session:exchangeToken"
        )
        body: Dict[str, Any] = {}

        if token:
            body["token"] = token

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.ExchangeSessionTokenResponse.__json_decode__)

    async def create_portal(
        self,
        *,
        organization_id: Optional[str] = None,
        portal_url: Optional[str] = None,
        return_url: Optional[str] = None,
        success_url: Optional[str] = None,
    ) -> userv1.CreatePortalSessionResponse:
        """
        Create a new Portal session.

        :param organization_id:
            The identifier of the organization.

            When specified the `{accountId}` in the `portalUrl` will be
            replaced with the organization ID, otherwise the user ID
            will be used.
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
            * `/{accountId}/checkout` - start a checkout
            * `/{accountId}/checkout/<some-plan-id>` - start a checkout with a specified plan
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
        """
        req = Request(
            "user.session.createPortal", "POST", "/user/v1/session:createPortal"
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if portal_url:
            body["portalUrl"] = portal_url
        if return_url:
            body["returnUrl"] = return_url
        if success_url:
            body["successUrl"] = success_url

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.CreatePortalSessionResponse.__json_decode__)
