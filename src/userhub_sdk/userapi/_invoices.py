# Code generated. DO NOT EDIT.

from typing import Optional

from userhub_sdk import userv1
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
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> userv1.ListInvoicesResponse:
        """
        Lists invoices.

        :param organization_id:
            Show results for specified organization.

            If this is not provided the user's individual subscription(s)
            will be returned.
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
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `state`
            - `dueTime`
            - `createTime`
            - `updateTime`
        """
        req = Request("user.invoices.list", "GET", "/user/v1/invoices")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = self._transport.execute(req)

        return res.decode_body(userv1.ListInvoicesResponse.__json_decode__)

    def get(
        self,
        invoice_id: str,
    ) -> userv1.Invoice:
        """
        Retrieves specified invoice.

        :param invoice_id:
            The identifier of the invoice.
        """
        req = Request(
            "user.invoices.get",
            "GET",
            f"/user/v1/invoices/{util.quote_path(invoice_id)}",
        )
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Invoice.__json_decode__)


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
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
        order_by: Optional[str] = None,
    ) -> userv1.ListInvoicesResponse:
        """
        Lists invoices.

        :param organization_id:
            Show results for specified organization.

            If this is not provided the user's individual subscription(s)
            will be returned.
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
            A comma-separated list of fields to order by, sorted in ascending order.
            Use `desc` after a field name for descending.

            Supported fields:
            - `state`
            - `dueTime`
            - `createTime`
            - `updateTime`
        """
        req = Request("user.invoices.list", "GET", "/user/v1/invoices")
        req.set_idempotent(True)

        if organization_id:
            req.set_query("organizationId", organization_id)
        if page_size:
            req.set_query("pageSize", page_size)
        if page_token:
            req.set_query("pageToken", page_token)
        if order_by:
            req.set_query("orderBy", order_by)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.ListInvoicesResponse.__json_decode__)

    async def get(
        self,
        invoice_id: str,
    ) -> userv1.Invoice:
        """
        Retrieves specified invoice.

        :param invoice_id:
            The identifier of the invoice.
        """
        req = Request(
            "user.invoices.get",
            "GET",
            f"/user/v1/invoices/{util.quote_path(invoice_id)}",
        )
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Invoice.__json_decode__)
