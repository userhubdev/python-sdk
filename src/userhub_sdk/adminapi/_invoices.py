# Code generated. DO NOT EDIT.

from typing import Any, Dict, Optional

from userhub_sdk import adminv1
from userhub_sdk._internal import util
from userhub_sdk._internal.request import Request
from userhub_sdk._internal.transport import AsyncTransport, Transport


class Invoices:
    """
    The invoice methods.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    def list(
        self,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListInvoicesResponse:
        """
        List invoices.

        :param organization_id:
            Filter results by organization identifier.

            This is required if the user identifier is not specified.
        :param user_id:
            Filter results by user identifier.

            This is required if the organization identifier is not specified.
        :param page_size:
            The maximum number of invoices to return. The API may return fewer than
            this value.

            If unspecified, at most 20 invoices will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list invoices call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list invoices must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by.
        :param view:
            The Invoice view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.invoices.list", "GET", "/admin/v1/invoices")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)
        if view:
            req.set_query("view", view)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.ListInvoicesResponse.__json_decode__)

    def get(
        self,
        invoice_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.Invoice:
        """
        Get an invoice.

        :param invoice_id:
            The identifier of the invoice.
        :param organization_id:
            Restrict by organization identifier.
        :param user_id:
            Restrict by user identifier.
        """
        req = Request(
            "admin.invoices.get",
            "GET",
            f"/admin/v1/invoices/{util.quote_path(invoice_id)}",
        )
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Invoice.__json_decode__)

    def pay(
        self,
        invoice_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        payment_method_id: Optional[str] = None,
    ) -> adminv1.Invoice:
        """
        Pay an invoice.

        :param invoice_id:
            The identifier of the invoice.
        :param organization_id:
            Restrict by organization identifier.
        :param user_id:
            Restrict by user identifier.
        :param payment_method_id:
            The identifier of the payment method.

            The default payment method will be used if not specified.
        """
        req = Request(
            "admin.invoices.pay",
            "POST",
            f"/admin/v1/invoices/{util.quote_path(invoice_id)}:pay",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id
        if payment_method_id:
            body["paymentMethodId"] = payment_method_id

        req.set_body(body)

        res = self._transport.execute(req)

        return res.decode_body(adminv1.Invoice.__json_decode__)


class AsyncInvoices:
    """
    The invoice methods.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    async def list(
        self,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
        view: Optional[str] = None,
    ) -> adminv1.ListInvoicesResponse:
        """
        List invoices.

        :param organization_id:
            Filter results by organization identifier.

            This is required if the user identifier is not specified.
        :param user_id:
            Filter results by user identifier.

            This is required if the organization identifier is not specified.
        :param page_size:
            The maximum number of invoices to return. The API may return fewer than
            this value.

            If unspecified, at most 20 invoices will be returned.
            The maximum value is 100; values above 100 will be coerced to 100.
        :param page_token:
            A page token, received from a previous list invoices call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to list invoices must match
            the call that provided the page token.
        :param order_by:
            A comma-separated list of fields to order by.
        :param view:
            The Invoice view to return in the results.

            This defaults to the `BASIC` view.
        """
        req = Request("admin.invoices.list", "GET", "/admin/v1/invoices")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)
        if view:
            req.set_query("view", view)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.ListInvoicesResponse.__json_decode__)

    async def get(
        self,
        invoice_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> adminv1.Invoice:
        """
        Get an invoice.

        :param invoice_id:
            The identifier of the invoice.
        :param organization_id:
            Restrict by organization identifier.
        :param user_id:
            Restrict by user identifier.
        """
        req = Request(
            "admin.invoices.get",
            "GET",
            f"/admin/v1/invoices/{util.quote_path(invoice_id)}",
        )
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if user_id:
            req.set_query("userId", user_id)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Invoice.__json_decode__)

    async def pay(
        self,
        invoice_id: str,
        *,
        organization_id: Optional[str] = None,
        user_id: Optional[str] = None,
        payment_method_id: Optional[str] = None,
    ) -> adminv1.Invoice:
        """
        Pay an invoice.

        :param invoice_id:
            The identifier of the invoice.
        :param organization_id:
            Restrict by organization identifier.
        :param user_id:
            Restrict by user identifier.
        :param payment_method_id:
            The identifier of the payment method.

            The default payment method will be used if not specified.
        """
        req = Request(
            "admin.invoices.pay",
            "POST",
            f"/admin/v1/invoices/{util.quote_path(invoice_id)}:pay",
        )
        body: Dict[str, Any] = {}

        if organization_id:
            body["organizationId"] = organization_id
        if user_id:
            body["userId"] = user_id
        if payment_method_id:
            body["paymentMethodId"] = payment_method_id

        req.set_body(body)

        res = await self._transport.execute(req)

        return res.decode_body(adminv1.Invoice.__json_decode__)
