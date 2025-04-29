# Code generated. DO NOT EDIT.

from typing import Optional

from userhub_sdk import types
from userhub_sdk._internal import constants
from userhub_sdk._internal.http_transport import AsyncHttpTransport, HttpTransport

from . import _client


class UserApi(_client.Client):
    """
    The client for the User API.

    :param user_key: The User API key `pk_8anj...`.
    :param access_token: The user's API access token. You can get this by calling `admin_api.users.create_api_session`.
    """

    def __init__(
        self,
        user_key: str,
        access_token: Optional[str] = None,
        *,
        api_version: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        if not api_version:
            api_version = constants.API_VERSION
        if not base_url:
            base_url = constants.API_BASE_URL

        headers = {}

        headers[constants.API_VERSION_HEADER] = api_version

        user_key = (user_key or "").strip()
        if not user_key:
            raise types.UserHubError("user_key required")

        headers[constants.API_KEY_HEADER] = user_key

        access_token = (access_token or "").strip()
        if access_token:
            headers[constants.AUTH_HEADER] = f"Bearer {access_token}"

        transport = HttpTransport(base_url, headers)

        super().__init__(transport)


class AsyncUserApi(_client.AsyncClient):
    """
    The client for the User API.

    :param user_key: The User API key `pk_8anj...`.
    :param access_token: The user's API access token. You can get this by calling `admin_api.users.create_api_session`.
    """

    def __init__(
        self,
        user_key: str,
        access_token: Optional[str] = None,
        *,
        api_version: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        if not api_version:
            api_version = constants.API_VERSION
        if not base_url:
            base_url = constants.API_BASE_URL

        headers = {}

        headers[constants.API_VERSION_HEADER] = api_version

        user_key = (user_key or "").strip()
        if not user_key:
            raise types.UserHubError("user_key required")

        headers[constants.API_KEY_HEADER] = user_key

        access_token = (access_token or "").strip()
        if access_token:
            headers[constants.AUTH_HEADER] = f"Bearer {access_token}"

        transport = AsyncHttpTransport(base_url, headers)

        super().__init__(transport)
