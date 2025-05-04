# Code generated. DO NOT EDIT.

from typing import Optional

from userhub_sdk import userv1
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport


class Pricing:
    """
    The pricing methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def get(
        self,
        *,
        account_type: Optional[str] = None,
        organization_id: Optional[str] = None,
        public: Optional[bool] = None,
    ) -> userv1.Pricing:
        """
        Get pricing.

        :param account_type:
            Whether to get pricing for users or organizations.

            This is not required if organization ID is specified
            and will default to user if no options are specified.
        :param organization_id:
            Show pricing for specified organization.

            If this and account type are not specified, it will default to
            the requesting user for authenticated requests.
        :param public:
            Always get the current public pricing.

            For unauthenticated requests, this is always true.
        """
        req = Request("user.pricing.get", "GET", "/user/v1/pricing")
        req.set_idempotent(True)

        if account_type:
            req.set_query("accountType", account_type)
        if organization_id:
            req.set_query("organizationId", organization_id)
        if public:
            req.set_query("public", public)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Pricing.__json_decode__)


class AsyncPricing:
    """
    The pricing methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get(
        self,
        *,
        account_type: Optional[str] = None,
        organization_id: Optional[str] = None,
        public: Optional[bool] = None,
    ) -> userv1.Pricing:
        """
        Get pricing.

        :param account_type:
            Whether to get pricing for users or organizations.

            This is not required if organization ID is specified
            and will default to user if no options are specified.
        :param organization_id:
            Show pricing for specified organization.

            If this and account type are not specified, it will default to
            the requesting user for authenticated requests.
        :param public:
            Always get the current public pricing.

            For unauthenticated requests, this is always true.
        """
        req = Request("user.pricing.get", "GET", "/user/v1/pricing")
        req.set_idempotent(True)

        if account_type:
            req.set_query("accountType", account_type)
        if organization_id:
            req.set_query("organizationId", organization_id)
        if public:
            req.set_query("public", public)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Pricing.__json_decode__)
