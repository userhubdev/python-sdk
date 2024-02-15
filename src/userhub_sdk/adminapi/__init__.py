# Code generated. DO NOT EDIT.

from typing import Optional

from userhub_sdk import types
from userhub_sdk._internal import constants
from userhub_sdk._internal.http_transport import AsyncHttpTransport, HttpTransport

from . import _client


class AdminApi(_client.Client):
    """
    The client for the Admin API.

    :param admin_key: The Admin API key (e.g. `sk_2vm8...`).
    """

    def __init__(
        self,
        admin_key: str,
        *,
        base_url: Optional[str] = None,
    ):
        if not base_url:
            base_url = constants.API_BASE_URL

        headers = {}

        admin_key = (admin_key or "").strip()
        if not admin_key:
            raise types.UserHubError("admin_key required")
        if not admin_key.startswith(constants.ADMIN_KEY_PREFIX):
            raise types.UserHubError(
                f"admin_key must start with `{constants.ADMIN_KEY_PREFIX}`"
            )

        headers[constants.AUTH_HEADER] = f"Bearer {admin_key}"

        transport = HttpTransport(base_url, headers)

        super().__init__(transport)


class AsyncAdminApi(_client.AsyncClient):
    """
    The async client for the Admin API.

    :param admin_key: The Admin API key (e.g. `sk_2vm8...`).
    """

    def __init__(
        self,
        admin_key: str,
        *,
        base_url: Optional[str] = None,
    ):
        if not base_url:
            base_url = constants.API_BASE_URL

        headers = {}

        admin_key = (admin_key or "").strip()
        if not admin_key:
            raise types.UserHubError("admin_key required")
        if not admin_key.startswith(constants.ADMIN_KEY_PREFIX):
            raise types.UserHubError(
                f"admin_key must start with `{constants.ADMIN_KEY_PREFIX}`"
            )

        headers[constants.AUTH_HEADER] = f"Bearer {admin_key}"

        transport = AsyncHttpTransport(base_url, headers)

        super().__init__(transport)
