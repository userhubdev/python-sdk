# Code generated. DO NOT EDIT.

from typing import Any
from typing import Dict

from .. import userv1
from .._internal.request import Request
from .._internal.transport import AsyncTransport
from .._internal.transport import Transport


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
        Get current session details.
        """
        req = Request("user.session.get", "GET", "/user/v1/session")
        req.set_idempotent(True)

        res = self._transport.execute(req)

        return res.decode_body(userv1.Session.__json_decode__)


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
        Get current session details.
        """
        req = Request("user.session.get", "GET", "/user/v1/session")
        req.set_idempotent(True)

        res = await self._transport.execute(req)

        return res.decode_body(userv1.Session.__json_decode__)
