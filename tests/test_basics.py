import datetime
import json
import os

import pytest

from userhub_sdk import AdminApi, AsyncAdminApi, AsyncUserApi, UserApi
from userhub_sdk.adminv1 import AccountConnection, User
from userhub_sdk._internal.util import encode_json


def get_env(name: str) -> str:
    user_key = os.getenv(name)
    if not user_key:
        pytest.skip(f"{name} not configured")
    return user_key


def test_admin_api():
    api = AdminApi(get_env("TEST_ADMIN_KEY"))
    users = api.users.list()
    assert users


@pytest.mark.asyncio
async def test_async_admin_api():
    api = AsyncAdminApi(get_env("TEST_ADMIN_KEY"))
    users = await api.users.list()
    assert users


def test_user_api():
    api = UserApi(get_env("TEST_USER_KEY"))
    session = api.session.get()
    assert session is not None
    assert session.scopes


@pytest.mark.asyncio
async def test_async_user_api():
    api = AsyncUserApi(get_env("TEST_USER_KEY"))
    session = await api.session.get()
    assert session is not None
    assert session.scopes


def test_model():
    user = User(
        id="usr_1",
        display_name="Jane Doe",
        create_time=datetime.datetime.now(datetime.timezone.utc),
        account_connections=[AccountConnection(external_id="cus_1")],
    )
    assert user.display_name == "Jane Doe"

    data = user.__json_encode__()
    assert data.get("displayName") == user.display_name

    encoded_json = encode_json(user)
    decoded_user = User.__json_decode__(json.loads(encoded_json))
    assert user == decoded_user
