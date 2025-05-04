# Code generated. DO NOT EDIT.

from typing import Optional

from userhub_sdk import adminv1
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
        user_id: Optional[str] = None,
    ) -> adminv1.Pricing:
        """
        Get pricing.

        :param account_type:
            Whether to get pricing for users or organizations.

            This is not required if either user ID or organization ID is specified
            and will default to user if no options are specified.
        :param organization_id:
            Show pricing for specified organization.
        :param user_id:
            Show pricing for the specified user.
        """
        req = Request("admin.pricing.get", "GET", "/admin/v1/pricing")
        req.set_idempotent(True)

        if account_type:
            req.set_query("accountType", account_type)
        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Pricing.__json_decode__)


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
        user_id: Optional[str] = None,
    ) -> adminv1.Pricing:
        """
        Get pricing.

        :param account_type:
            Whether to get pricing for users or organizations.

            This is not required if either user ID or organization ID is specified
            and will default to user if no options are specified.
        :param organization_id:
            Show pricing for specified organization.
        :param user_id:
            Show pricing for the specified user.
        """
        req = Request("admin.pricing.get", "GET", "/admin/v1/pricing")
        req.set_idempotent(True)

        if account_type:
            req.set_query("accountType", account_type)
        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Pricing.__json_decode__)
