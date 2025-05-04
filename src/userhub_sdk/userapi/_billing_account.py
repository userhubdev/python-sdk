# Code generated. DO NOT EDIT.

from typing import Any, Dict, Optional, Union

from userhub_sdk import commonv1, userv1
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport
from userhub_sdk.types import UNDEFINED, Undefined


class BillingAccount:
    """
    The billing account methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def get(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> userv1.BillingAccount:
        """
        Get the default billing account.

        :param organization_id:
            The identifier of the organization.

            If not specified the billing account for the user is returned.
        """
        req = Request("user.billing_account.get", "GET", "/user/v1/billingAccount")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)

        res = self._transport.execute(req)

        return res.decode_body(userv1.BillingAccount.__json_decode__)

    def update(
        self,
        *,
        display_name: Union[Optional[str], Undefined] = UNDEFINED,
        email: Union[Optional[str], Undefined] = UNDEFINED,
        phone_number: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        organization_id: Optional[str] = None,
    ) -> userv1.BillingAccount:
        """
        Update the default billing account.

        :param display_name:
            The human-readable display name of the billing account.

            The maximum length is 200 characters.

            This might be further restricted by the billing provider.
        :param email:
            The email address of the billing account.

            The maximum length is 320 characters.

            This might be further restricted by the billing provider.
        :param phone_number:
            The E164 phone number of the billing account (e.g. `+12125550123`).
        :param address:
            The address for the billing account.
        :param organization_id:
            The identifier of the organization.

            If not specified the billing account for the user is used.
        """
        req = Request("user.billing_account.update", "PATCH", "/user/v1/billingAccount")
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if organization_id:
            req.set_query("organizationId", organization_id)
        if display_name is not UNDEFINED:
            body["displayName"] = display_name
        if email is not UNDEFINED:
            body["email"] = email
        if phone_number is not UNDEFINED:
            body["phoneNumber"] = phone_number
        if address is not UNDEFINED:
            body["address"] = address

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.BillingAccount.__json_decode__)


class AsyncBillingAccount:
    """
    The billing account methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def get(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> userv1.BillingAccount:
        """
        Get the default billing account.

        :param organization_id:
            The identifier of the organization.

            If not specified the billing account for the user is returned.
        """
        req = Request("user.billing_account.get", "GET", "/user/v1/billingAccount")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.BillingAccount.__json_decode__)

    async def update(
        self,
        *,
        display_name: Union[Optional[str], Undefined] = UNDEFINED,
        email: Union[Optional[str], Undefined] = UNDEFINED,
        phone_number: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        organization_id: Optional[str] = None,
    ) -> userv1.BillingAccount:
        """
        Update the default billing account.

        :param display_name:
            The human-readable display name of the billing account.

            The maximum length is 200 characters.

            This might be further restricted by the billing provider.
        :param email:
            The email address of the billing account.

            The maximum length is 320 characters.

            This might be further restricted by the billing provider.
        :param phone_number:
            The E164 phone number of the billing account (e.g. `+12125550123`).
        :param address:
            The address for the billing account.
        :param organization_id:
            The identifier of the organization.

            If not specified the billing account for the user is used.
        """
        req = Request("user.billing_account.update", "PATCH", "/user/v1/billingAccount")
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if organization_id:
            req.set_query("organizationId", organization_id)
        if display_name is not UNDEFINED:
            body["displayName"] = display_name
        if email is not UNDEFINED:
            body["email"] = email
        if phone_number is not UNDEFINED:
            body["phoneNumber"] = phone_number
        if address is not UNDEFINED:
            body["address"] = address

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.BillingAccount.__json_decode__)
