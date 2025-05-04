# Code generated. DO NOT EDIT.

from typing import Any, Dict, Optional, Union

from userhub_sdk import apiv1, commonv1, userv1
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

    def list(
        self,
        *,
        organization_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> userv1.ListPaymentMethodsResponse:
        """
        List payment methods for an account.

        :param organization_id:
            Show results for specified organization.

            If this is not provided the user's individual subscription(s)
            will be returned.
        :param page_size:
            The maximum number of payment methods to return. The API may return fewer than
            this value.

            If unspecified, at most 20 payment methods will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list payment methods call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list payment methods must match
            the call that provided the page token.
        """
        req = Request("user.payment_methods.list", "GET", "/user/v1/paymentMethods")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)

        res = self._transport.execute(req)

        return res.decode_body(userv1.ListPaymentMethodsResponse.__json_decode__)

    def create(
        self,
        *,
        organization_id: Optional[str] = None,
        external_id: str,
    ) -> userv1.PaymentMethod:
        """
        Create a new payment method.

        :param organization_id:
            The identifier of the organization.
        :param external_id:
            The external identifier of the payment method to connect.
        """
        req = Request("user.payment_methods.create", "POST", "/user/v1/paymentMethods")
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if external_id:
            body["externalId"] = external_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.PaymentMethod.__json_decode__)

    def create_intent(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> userv1.PaymentMethodIntent:
        """
        Create a new payment method intent.

        This can be used with a third-party billing provider to
        store a payment method.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "user.payment_methods.createIntent",
            "POST",
            "/user/v1/paymentMethods:createIntent",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.PaymentMethodIntent.__json_decode__)

    def get(
        self,
        payment_method_id: str,
    ) -> userv1.PaymentMethod:
        """
        Get a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        """
        req = Request(
            "user.payment_methods.get",
            "GET",
            f"/user/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(userv1.PaymentMethod.__json_decode__)

    def update(
        self,
        payment_method_id: str,
        *,
        full_name: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        exp_year: Union[Optional[int], Undefined] = UNDEFINED,
        exp_month: Union[Optional[int], Undefined] = UNDEFINED,
    ) -> userv1.PaymentMethod:
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
        """
        req = Request(
            "user.payment_methods.update",
            "PATCH",
            f"/user/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

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

        return res.decode_body(userv1.PaymentMethod.__json_decode__)

    def set_default(
        self,
        payment_method_id: str,
    ) -> userv1.PaymentMethod:
        """
        Set a default payment method for an account.

        :param payment_method_id:
            The identifier of the payment method.
        """
        req = Request(
            "user.payment_methods.setDefault",
            "POST",
            f"/user/v1/paymentMethods/{util.quote_path(payment_method_id)}:setDefault",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.PaymentMethod.__json_decode__)

    def delete(
        self,
        payment_method_id: str,
    ) -> apiv1.EmptyResponse:
        """
        Delete a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        """
        req = Request(
            "user.payment_methods.delete",
            "DELETE",
            f"/user/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        res = self._transport.execute(req)

        return res.decode_body(apiv1.EmptyResponse.__json_decode__)


class AsyncPaymentMethods:
    """
    The payment method methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list(
        self,
        *,
        organization_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> userv1.ListPaymentMethodsResponse:
        """
        List payment methods for an account.

        :param organization_id:
            Show results for specified organization.

            If this is not provided the user's individual subscription(s)
            will be returned.
        :param page_size:
            The maximum number of payment methods to return. The API may return fewer than
            this value.

            If unspecified, at most 20 payment methods will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list payment methods call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list payment methods must match
            the call that provided the page token.
        """
        req = Request("user.payment_methods.list", "GET", "/user/v1/paymentMethods")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.ListPaymentMethodsResponse.__json_decode__)

    async def create(
        self,
        *,
        organization_id: Optional[str] = None,
        external_id: str,
    ) -> userv1.PaymentMethod:
        """
        Create a new payment method.

        :param organization_id:
            The identifier of the organization.
        :param external_id:
            The external identifier of the payment method to connect.
        """
        req = Request("user.payment_methods.create", "POST", "/user/v1/paymentMethods")
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if external_id:
            body["externalId"] = external_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.PaymentMethod.__json_decode__)

    async def create_intent(
        self,
        *,
        organization_id: Optional[str] = None,
    ) -> userv1.PaymentMethodIntent:
        """
        Create a new payment method intent.

        This can be used with a third-party billing provider to
        store a payment method.

        :param organization_id:
            The identifier of the organization.
        """
        req = Request(
            "user.payment_methods.createIntent",
            "POST",
            "/user/v1/paymentMethods:createIntent",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.PaymentMethodIntent.__json_decode__)

    async def get(
        self,
        payment_method_id: str,
    ) -> userv1.PaymentMethod:
        """
        Get a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        """
        req = Request(
            "user.payment_methods.get",
            "GET",
            f"/user/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.PaymentMethod.__json_decode__)

    async def update(
        self,
        payment_method_id: str,
        *,
        full_name: Union[Optional[str], Undefined] = UNDEFINED,
        address: Union[Optional[commonv1.Address], Undefined] = UNDEFINED,
        exp_year: Union[Optional[int], Undefined] = UNDEFINED,
        exp_month: Union[Optional[int], Undefined] = UNDEFINED,
    ) -> userv1.PaymentMethod:
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
        """
        req = Request(
            "user.payment_methods.update",
            "PATCH",
            f"/user/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        req.set_idempotent(True)

        body: Dict[str, Any] = {}

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

        return res.decode_body(userv1.PaymentMethod.__json_decode__)

    async def set_default(
        self,
        payment_method_id: str,
    ) -> userv1.PaymentMethod:
        """
        Set a default payment method for an account.

        :param payment_method_id:
            The identifier of the payment method.
        """
        req = Request(
            "user.payment_methods.setDefault",
            "POST",
            f"/user/v1/paymentMethods/{util.quote_path(payment_method_id)}:setDefault",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.PaymentMethod.__json_decode__)

    async def delete(
        self,
        payment_method_id: str,
    ) -> apiv1.EmptyResponse:
        """
        Delete a payment method.

        :param payment_method_id:
            The identifier of the payment method.
        """
        req = Request(
            "user.payment_methods.delete",
            "DELETE",
            f"/user/v1/paymentMethods/{util.quote_path(payment_method_id)}",
        )
        res = await self._transport.execute(req)

        return res.decode_body(apiv1.EmptyResponse.__json_decode__)
