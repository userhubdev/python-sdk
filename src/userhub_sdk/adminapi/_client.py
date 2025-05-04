# Code generated. DO NOT EDIT.

from types import TracebackType
from typing import Optional, Type

from userhub_sdk._internal.transport import AsyncTransport, Transport

from ._checkouts import AsyncCheckouts, Checkouts
from ._flows import AsyncFlows, Flows
from ._invoices import AsyncInvoices, Invoices
from ._organizations import AsyncOrganizations, Organizations
from ._payment_methods import AsyncPaymentMethods, PaymentMethods
from ._pricing import AsyncPricing, Pricing
from ._roles import AsyncRoles, Roles
from ._subscriptions import AsyncSubscriptions, Subscriptions
from ._users import AsyncUsers, Users


class Client:
    """
    The Admin API.
    """

    def __init__(self, transport: Transport):
        self._transport = transport

    @property
    def checkouts(self) -> Checkouts:
        """
        The checkout methods.
        """
        return Checkouts(self._transport)

    @property
    def flows(self) -> Flows:
        """
        The flow methods.
        """
        return Flows(self._transport)

    @property
    def invoices(self) -> Invoices:
        """
        The invoice methods.
        """
        return Invoices(self._transport)

    @property
    def organizations(self) -> Organizations:
        """
        The organization methods.
        """
        return Organizations(self._transport)

    @property
    def payment_methods(self) -> PaymentMethods:
        """
        The payment method methods.
        """
        return PaymentMethods(self._transport)

    @property
    def pricing(self) -> Pricing:
        """
        The pricing methods.
        """
        return Pricing(self._transport)

    @property
    def roles(self) -> Roles:
        """
        The role methods.
        """
        return Roles(self._transport)

    @property
    def subscriptions(self) -> Subscriptions:
        """
        The subscription methods.
        """
        return Subscriptions(self._transport)

    @property
    def users(self) -> Users:
        """
        The user methods.
        """
        return Users(self._transport)

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> "Client":
        self._transport.__enter__()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        exc_tb: Optional[TracebackType] = None,
    ) -> None:
        self._transport.__exit__(exc_type, exc_value, exc_tb)


class AsyncClient:
    """
    The Admin API.
    """

    def __init__(self, transport: AsyncTransport):
        self._transport = transport

    @property
    def checkouts(self) -> AsyncCheckouts:
        """
        The checkout methods.
        """
        return AsyncCheckouts(self._transport)

    @property
    def flows(self) -> AsyncFlows:
        """
        The flow methods.
        """
        return AsyncFlows(self._transport)

    @property
    def invoices(self) -> AsyncInvoices:
        """
        The invoice methods.
        """
        return AsyncInvoices(self._transport)

    @property
    def organizations(self) -> AsyncOrganizations:
        """
        The organization methods.
        """
        return AsyncOrganizations(self._transport)

    @property
    def payment_methods(self) -> AsyncPaymentMethods:
        """
        The payment method methods.
        """
        return AsyncPaymentMethods(self._transport)

    @property
    def pricing(self) -> AsyncPricing:
        """
        The pricing methods.
        """
        return AsyncPricing(self._transport)

    @property
    def roles(self) -> AsyncRoles:
        """
        The role methods.
        """
        return AsyncRoles(self._transport)

    @property
    def subscriptions(self) -> AsyncSubscriptions:
        """
        The subscription methods.
        """
        return AsyncSubscriptions(self._transport)

    @property
    def users(self) -> AsyncUsers:
        """
        The user methods.
        """
        return AsyncUsers(self._transport)

    async def aclose(self) -> None:
        await self._transport.aclose()

    async def __aenter__(self) -> "AsyncClient":
        await self._transport.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        exc_tb: Optional[TracebackType] = None,
    ) -> None:
        await self._transport.__aexit__(exc_type, exc_value, exc_tb)
