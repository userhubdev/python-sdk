# Code generated. DO NOT EDIT.

from typing import Any, Dict, Optional, Union

from userhub_sdk import adminv1, apiv1, commonv1
from userhub_sdk._internal import util
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport
from userhub_sdk.types import UNDEFINED, Undefined


class PaymentMethods:
    """
    The payment method methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def create(
        self,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        connection_id: str,
        external_id: str,
        default: Optional[bool] = None,
    ) -> adminv1.PaymentMethod:
        """
        Create a payment method.

        :param organization_id:
            The identifier of the organization.

            This is required if the user identifier not specified.
        :param user_id:
            The identifier of the user.

            This is required if the organization identifier not specified.
        :param connection_id:
            The identifier of the connection.
        :param external_id:
            The external identifier of the payment method to connect.
        :param default:
            Whether to set the payment method as the default.

            This defaults to true.
        """
        req = Request(
            "admin.payment_methods.create", "POST", "/admin/v1/paymentMethods"
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id
        if connection_id:
            body["connectionId"] = connection_id
        if external_id:
            body["externalId"] = external_id
        if default:
            body["default"] = default

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethod.__json_decode__)

    def create_intent(
        self,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        connection_id: str,
    ) -> adminv1.PaymentMethodIntent:
        """
        Create a payment method intent.

        This can be used with a third-party billing provider API
        to store a payment method.

        :param organization_id:
            The identifier of the organization.

            This is required if the user identifier is not specified.
        :param user_id:
            The identifier of the user.

            This is required if the organization identifier is not not
            specified.
        :param connection_id:
            The identifier of the connection.
        """
        req = Request(
            "admin.payment_methods.createIntent",
            "POST",
            "/admin/v1/paymentMethods:createIntent",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id
        if connection_id:
            body["connectionId"] = connection_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethodIntent.__json_decode__)

    def get(
        self,
        payment_method_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.PaymentMethod:
        """
        Get a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        :param organization_id:
            The identifier of the organization.

            Optionally restrict update to payment methods owned by
            this organization.
        :param user_id:
            The identifier of the user.

            Optionally restrict update to payment methods owned by
            this user.
        """
        req = Request(
            "admin.payment_methods.get",
            "GET",
            f"/admin/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethod.__json_decode__)

    def update(
        self,
        payment_method_id: str,
        *,
        full_name: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        exp_year: Union[Optional[int], Undefined] = UNDEFINED,
        exp_month: Union[Optional[int], Undefined] = UNDEFINED,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.PaymentMethod:
        """
        Update a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        :param full_name:
            The full name of the owner of the payment method (e.g. `Jane Doe`).
        :param address:
            The address for the payment method.
        :param exp_year:
            The card expiration year (e.g. `2030`).
        :param exp_month:
            The card expiration month (e.g. `12`).
        :param organization_id:
            The identifier of the organization.

            Optionally restrict update to payment methods owned by
            this organization.
        :param user_id:
            The identifier of the user.

            Optionally restrict update to payment methods owned by
            this user.
        """
        req = Request(
            "admin.payment_methods.update",
            "PATCH",
            f"/admin/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)
        if full_name is not UNDEFINED:
            body["fullName"] = full_name
        if address is not UNDEFINED:
            body["address"] = address
        if exp_year is not UNDEFINED:
            body["expYear"] = exp_year
        if exp_month is not UNDEFINED:
            body["expMonth"] = exp_month

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethod.__json_decode__)

    def set_default(
        self,
        payment_method_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.PaymentMethod:
        """
        Set a default payment method for an account.

        :param payment_method_id:
            The identifier of the payment method.
        :param organization_id:
            The identifier of the organization.

            Optionally restrict set default to payment methods owned by
            this organization.
        :param user_id:
            The identifier of the user.

            Optionally restrict set default to payment methods owned by
            this user.
        """
        req = Request(
            "admin.payment_methods.setDefault",
            "POST",
            f"/admin/v1/paymentMethods/{util.quote_path(payment_method_id)}:setDefault",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethod.__json_decode__)

    def delete(
        self,
        payment_method_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> apiv1.EmptyResponse:
        """
        Delete a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        :param organization_id:
            The identifier of the organization.

            Optionally restrict delete to payment methods owned by
            this organization.
        :param user_id:
            The identifier of the user.

            Optionally restrict delete to payment methods owned by
            this user.
        """
        req = Request(
            "admin.payment_methods.delete",
            "DELETE",
            f"/admin/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = self._transport.execute(req)

        return res.decode_body(apiv1.EmptyResponse.__json_decode__)


class AsyncPaymentMethods:
    """
    The payment method methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def create(
        self,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        connection_id: str,
        external_id: str,
        default: Optional[bool] = None,
    ) -> adminv1.PaymentMethod:
        """
        Create a payment method.

        :param organization_id:
            The identifier of the organization.

            This is required if the user identifier not specified.
        :param user_id:
            The identifier of the user.

            This is required if the organization identifier not specified.
        :param connection_id:
            The identifier of the connection.
        :param external_id:
            The external identifier of the payment method to connect.
        :param default:
            Whether to set the payment method as the default.

            This defaults to true.
        """
        req = Request(
            "admin.payment_methods.create", "POST", "/admin/v1/paymentMethods"
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id
        if connection_id:
            body["connectionId"] = connection_id
        if external_id:
            body["externalId"] = external_id
        if default:
            body["default"] = default

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethod.__json_decode__)

    async def create_intent(
        self,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        connection_id: str,
    ) -> adminv1.PaymentMethodIntent:
        """
        Create a payment method intent.

        This can be used with a third-party billing provider API
        to store a payment method.

        :param organization_id:
            The identifier of the organization.

            This is required if the user identifier is not specified.
        :param user_id:
            The identifier of the user.

            This is required if the organization identifier is not not
            specified.
        :param connection_id:
            The identifier of the connection.
        """
        req = Request(
            "admin.payment_methods.createIntent",
            "POST",
            "/admin/v1/paymentMethods:createIntent",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id
        if connection_id:
            body["connectionId"] = connection_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethodIntent.__json_decode__)

    async def get(
        self,
        payment_method_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.PaymentMethod:
        """
        Get a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        :param organization_id:
            The identifier of the organization.

            Optionally restrict update to payment methods owned by
            this organization.
        :param user_id:
            The identifier of the user.

            Optionally restrict update to payment methods owned by
            this user.
        """
        req = Request(
            "admin.payment_methods.get",
            "GET",
            f"/admin/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethod.__json_decode__)

    async def update(
        self,
        payment_method_id: str,
        *,
        full_name: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        exp_year: Union[Optional[int], Undefined] = UNDEFINED,
        exp_month: Union[Optional[int], Undefined] = UNDEFINED,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.PaymentMethod:
        """
        Update a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        :param full_name:
            The full name of the owner of the payment method (e.g. `Jane Doe`).
        :param address:
            The address for the payment method.
        :param exp_year:
            The card expiration year (e.g. `2030`).
        :param exp_month:
            The card expiration month (e.g. `12`).
        :param organization_id:
            The identifier of the organization.

            Optionally restrict update to payment methods owned by
            this organization.
        :param user_id:
            The identifier of the user.

            Optionally restrict update to payment methods owned by
            this user.
        """
        req = Request(
            "admin.payment_methods.update",
            "PATCH",
            f"/admin/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)
        if full_name is not UNDEFINED:
            body["fullName"] = full_name
        if address is not UNDEFINED:
            body["address"] = address
        if exp_year is not UNDEFINED:
            body["expYear"] = exp_year
        if exp_month is not UNDEFINED:
            body["expMonth"] = exp_month

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethod.__json_decode__)

    async def set_default(
        self,
        payment_method_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.PaymentMethod:
        """
        Set a default payment method for an account.

        :param payment_method_id:
            The identifier of the payment method.
        :param organization_id:
            The identifier of the organization.

            Optionally restrict set default to payment methods owned by
            this organization.
        :param user_id:
            The identifier of the user.

            Optionally restrict set default to payment methods owned by
            this user.
        """
        req = Request(
            "admin.payment_methods.setDefault",
            "POST",
            f"/admin/v1/paymentMethods/{util.quote_path(payment_method_id)}:setDefault",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.PaymentMethod.__json_decode__)

    async def delete(
        self,
        payment_method_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> apiv1.EmptyResponse:
        """
        Delete a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        :param organization_id:
            The identifier of the organization.

            Optionally restrict delete to payment methods owned by
            this organization.
        :param user_id:
            The identifier of the user.

            Optionally restrict delete to payment methods owned by
            this user.
        """
        req = Request(
            "admin.payment_methods.delete",
            "DELETE",
            f"/admin/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = await self._transport.execute(req)

        return res.decode_body(apiv1.EmptyResponse.__json_decode__)
