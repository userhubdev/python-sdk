# Code generated. DO NOT EDIT.

from typing import Any, Dict, List, Optional, Union

from userhub_sdk import commonv1, userv1
from userhub_sdk._internal import util
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport
from userhub_sdk.types import UNDEFINED, Undefined


class Checkouts:
    """
    The checkout methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def create(
        self,
        *,
        organization_id: Optional[str] = None,
        type: Optional[str] = None,
        plan_id: Optional[str] = None,
        submit: Optional[bool] = None,
    ) -> userv1.Checkout:
        """
        Create a new checkout.

        :param organization_id:
            The identifier of the organization.

            This must be provided for organization checkouts.
        :param type:
            The type of the checkout.
        :param plan_id:
            The identifier of the plan.

            This allows you to specify the currently selected plan.
        :param submit:
            Attempt to submit checkout if ready and due amount is zero.
        """
        req = Request("user.checkouts.create", "POST", "/user/v1/checkouts")
        body: Dict[str, Any] = {}

        if submit:
            req.set_query("submit", submit)
        if organization_id:
            body["organizationId"] = organization_id
        if type:
            body["type"] = type
        if plan_id:
            body["planId"] = plan_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def get(
        self,
        checkout_id: str,
    ) -> userv1.Checkout:
        """
        Get a checkout.

        :param checkout_id:
            The identifier of the checkout.
        """
        req = Request(
            "user.checkouts.get",
            "GET",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}",
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def set_plan(
        self,
        checkout_id: str,
        *,
        plan_id: Optional[str] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set plan for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param plan_id:
            The identifier of the plan.

            This is required if completed isn't set to true.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setPlan",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setPlan",
        )
        body: Dict[str, Any] = {}

        if plan_id:
            body["planId"] = plan_id
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def set_terms(
        self,
        checkout_id: str,
        *,
        plan_id: Optional[str] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set terms for a checkout.

        This is generally used to select a billing cycle for
        the plan.

        :param checkout_id:
            The identifier of the checkout.
        :param plan_id:
            The identifier of the plan.

            This is required if completed isn't set to true.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setTerms",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setTerms",
        )
        body: Dict[str, Any] = {}

        if plan_id:
            body["planId"] = plan_id
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def set_items(
        self,
        checkout_id: str,
        *,
        items: Optional[List[userv1.CheckoutItemInput]] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set item quantities for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param items:
            The items to update.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setItems",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setItems",
        )
        body: Dict[str, Any] = {}

        if items:
            body["items"] = items
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def set_payment_method(
        self,
        checkout_id: str,
        *,
        payment_method_id: Optional[str] = None,
        external_id: Optional[str] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set payment method for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param payment_method_id:
            The identifier of the payment method.

            This is required if external ID isn't specified or completed
            isn't set to true.
        :param external_id:
            The external identifier of the payment method to connect.

            This is required if payment method ID isn't specified or
            completed isn't set to true.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setPaymentMethod",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setPaymentMethod",
        )
        body: Dict[str, Any] = {}

        if payment_method_id:
            body["paymentMethodId"] = payment_method_id
        if external_id:
            body["externalId"] = external_id
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def set_billing_details(
        self,
        checkout_id: str,
        *,
        full_name: Optional[str] = None,
        address: Optional[commonv1.Address] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set billing details for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param full_name:
            The company or individual's full name.

            The maximum length is 200 characters.
        :param address:
            The billing details address.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setBillingDetails",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setBillingDetails",
        )
        body: Dict[str, Any] = {}

        if full_name:
            body["fullName"] = full_name
        if address:
            body["address"] = address
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def add_discount(
        self,
        checkout_id: str,
        *,
        code: Optional[str] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Add discount to a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param code:
            The discount code.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.addDiscount",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:addDiscount",
        )
        body: Dict[str, Any] = {}

        if code:
            body["code"] = code
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def remove_discount(
        self,
        checkout_id: str,
        *,
        checkout_discount_id: str,
    ) -> userv1.Checkout:
        """
        Remove discount from a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param checkout_discount_id:
            The identifier of the checkout discount.
        """
        req = Request(
            "user.checkouts.removeDiscount",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:removeDiscount",
        )
        body: Dict[str, Any] = {}

        if checkout_discount_id:
            body["checkoutDiscountId"] = checkout_discount_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def complete_payment(
        self,
        checkout_id: str,
    ) -> userv1.Checkout:
        """
        Complete payment for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        """
        req = Request(
            "user.checkouts.completePayment",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:completePayment",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def submit(
        self,
        checkout_id: str,
    ) -> userv1.Checkout:
        """
        Submit a checkout for processing.

        :param checkout_id:
            The identifier of the checkout.
        """
        req = Request(
            "user.checkouts.submit",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:submit",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    def cancel(
        self,
        checkout_id: str,
    ) -> userv1.Checkout:
        """
        Cancel a checkout.

        :param checkout_id:
            The identifier of the checkout.
        """
        req = Request(
            "user.checkouts.cancel",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:cancel",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)


class AsyncCheckouts:
    """
    The checkout methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def create(
        self,
        *,
        organization_id: Optional[str] = None,
        type: Optional[str] = None,
        plan_id: Optional[str] = None,
        submit: Optional[bool] = None,
    ) -> userv1.Checkout:
        """
        Create a new checkout.

        :param organization_id:
            The identifier of the organization.

            This must be provided for organization checkouts.
        :param type:
            The type of the checkout.
        :param plan_id:
            The identifier of the plan.

            This allows you to specify the currently selected plan.
        :param submit:
            Attempt to submit checkout if ready and due amount is zero.
        """
        req = Request("user.checkouts.create", "POST", "/user/v1/checkouts")
        body: Dict[str, Any] = {}

        if submit:
            req.set_query("submit", submit)
        if organization_id:
            body["organizationId"] = organization_id
        if type:
            body["type"] = type
        if plan_id:
            body["planId"] = plan_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def get(
        self,
        checkout_id: str,
    ) -> userv1.Checkout:
        """
        Get a checkout.

        :param checkout_id:
            The identifier of the checkout.
        """
        req = Request(
            "user.checkouts.get",
            "GET",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}",
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def set_plan(
        self,
        checkout_id: str,
        *,
        plan_id: Optional[str] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set plan for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param plan_id:
            The identifier of the plan.

            This is required if completed isn't set to true.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setPlan",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setPlan",
        )
        body: Dict[str, Any] = {}

        if plan_id:
            body["planId"] = plan_id
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def set_terms(
        self,
        checkout_id: str,
        *,
        plan_id: Optional[str] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set terms for a checkout.

        This is generally used to select a billing cycle for
        the plan.

        :param checkout_id:
            The identifier of the checkout.
        :param plan_id:
            The identifier of the plan.

            This is required if completed isn't set to true.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setTerms",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setTerms",
        )
        body: Dict[str, Any] = {}

        if plan_id:
            body["planId"] = plan_id
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def set_items(
        self,
        checkout_id: str,
        *,
        items: Optional[List[userv1.CheckoutItemInput]] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set item quantities for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param items:
            The items to update.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setItems",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setItems",
        )
        body: Dict[str, Any] = {}

        if items:
            body["items"] = items
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def set_payment_method(
        self,
        checkout_id: str,
        *,
        payment_method_id: Optional[str] = None,
        external_id: Optional[str] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set payment method for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param payment_method_id:
            The identifier of the payment method.

            This is required if external ID isn't specified or completed
            isn't set to true.
        :param external_id:
            The external identifier of the payment method to connect.

            This is required if payment method ID isn't specified or
            completed isn't set to true.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setPaymentMethod",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setPaymentMethod",
        )
        body: Dict[str, Any] = {}

        if payment_method_id:
            body["paymentMethodId"] = payment_method_id
        if external_id:
            body["externalId"] = external_id
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def set_billing_details(
        self,
        checkout_id: str,
        *,
        full_name: Optional[str] = None,
        address: Optional[commonv1.Address] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Set billing details for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param full_name:
            The company or individual's full name.

            The maximum length is 200 characters.
        :param address:
            The billing details address.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.setBillingDetails",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:setBillingDetails",
        )
        body: Dict[str, Any] = {}

        if full_name:
            body["fullName"] = full_name
        if address:
            body["address"] = address
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def add_discount(
        self,
        checkout_id: str,
        *,
        code: Optional[str] = None,
        completed: Union[Optional[bool], Undefined] = UNDEFINED,
    ) -> userv1.Checkout:
        """
        Add discount to a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param code:
            The discount code.
        :param completed:
            Mark the step completed if it is optional.
        """
        req = Request(
            "user.checkouts.addDiscount",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:addDiscount",
        )
        body: Dict[str, Any] = {}

        if code:
            body["code"] = code
        if completed is not UNDEFINED:
            body["completed"] = completed

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def remove_discount(
        self,
        checkout_id: str,
        *,
        checkout_discount_id: str,
    ) -> userv1.Checkout:
        """
        Remove discount from a checkout.

        :param checkout_id:
            The identifier of the checkout.
        :param checkout_discount_id:
            The identifier of the checkout discount.
        """
        req = Request(
            "user.checkouts.removeDiscount",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:removeDiscount",
        )
        body: Dict[str, Any] = {}

        if checkout_discount_id:
            body["checkoutDiscountId"] = checkout_discount_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def complete_payment(
        self,
        checkout_id: str,
    ) -> userv1.Checkout:
        """
        Complete payment for a checkout.

        :param checkout_id:
            The identifier of the checkout.
        """
        req = Request(
            "user.checkouts.completePayment",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:completePayment",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def submit(
        self,
        checkout_id: str,
    ) -> userv1.Checkout:
        """
        Submit a checkout for processing.

        :param checkout_id:
            The identifier of the checkout.
        """
        req = Request(
            "user.checkouts.submit",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:submit",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)

    async def cancel(
        self,
        checkout_id: str,
    ) -> userv1.Checkout:
        """
        Cancel a checkout.

        :param checkout_id:
            The identifier of the checkout.
        """
        req = Request(
            "user.checkouts.cancel",
            "POST",
            f"/user/v1/checkouts/{util.quote_path(checkout_id)}:cancel",
        )
        body: Dict[str, Any] = {}

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Checkout.__json_decode__)
