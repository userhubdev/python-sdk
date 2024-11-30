import datetime
import json
import os

import pytest
from pytest_httpserver import HTTPServer

from userhub_sdk import (
    AdminApi,
    AsyncAdminApi,
    AsyncUserApi,
    Code,
    UserApi,
    UserHubError,
)
from userhub_sdk._internal import util
from userhub_sdk.adminv1 import AccountConnection, User

SYNC_ASYNC = (False, True)


def get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        pytest.skip(f"{name} not configured")
    return value


def test_admin_api():
    api = AdminApi(get_env("TEST_USERHUB_ADMIN_KEY"))
    res = api.users.list()
    assert res


@pytest.mark.asyncio
async def test_async_admin_api():
    api = AsyncAdminApi(get_env("TEST_USERHUB_ADMIN_KEY"))
    res = await api.users.list()
    assert res


def test_user_api():
    api = UserApi(get_env("TEST_USERHUB_USER_KEY"))
    session = api.session.get()
    assert session is not None
    assert session.scopes


@pytest.mark.asyncio
async def test_async_user_api():
    api = AsyncUserApi(get_env("TEST_USERHUB_USER_KEY"))
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
    assert "displayName" in data
    assert data.get("displayName") == user.display_name

    encoded_json = util.encode_json(user)
    decoded_user = User.__json_decode__(json.loads(encoded_json))
    assert user == decoded_user


@pytest.fixture
def admin_api(httpserver: HTTPServer) -> AdminApi:
    return AdminApi("sk_test", base_url=httpserver.url_for(""))


@pytest.fixture
def async_admin_api(httpserver: HTTPServer) -> AsyncAdminApi:
    return AsyncAdminApi("sk_test", base_url=httpserver.url_for(""))


@pytest.mark.asyncio
async def test_api_get(
    admin_api: AdminApi,
    async_admin_api: AsyncAdminApi,
    httpserver: HTTPServer,
):
    for is_async in SYNC_ASYNC:
        httpserver.expect_oneshot_request(
            uri="/admin/v1/users/usr_1",
            method="GET",
            headers={"Authorization": "Bearer sk_test"},
        ).respond_with_json(
            {
                "id": "usr_1",
                "displayName": "Jane Doe",
            }
        )
        args = ("usr_1",)
        if is_async:
            res = await async_admin_api.users.get(*args)
        else:
            res = admin_api.users.get(*args)
        assert res is not None
        assert res.id == "usr_1"
        assert res.display_name == "Jane Doe"


@pytest.mark.asyncio
async def test_api_post(
    admin_api: AdminApi,
    async_admin_api: AsyncAdminApi,
    httpserver: HTTPServer,
):
    for is_async in SYNC_ASYNC:
        httpserver.expect_oneshot_request(
            uri="/admin/v1/users",
            method="POST",
            headers={"Authorization": "Bearer sk_test"},
            json={"displayName": "Jane Doe"},
        ).respond_with_json(
            {
                "id": "usr_1",
                "displayName": "Jane Doe",
            }
        )

        kwargs = {"display_name": "Jane Doe"}
        if is_async:
            res = await async_admin_api.users.create(**kwargs)
        else:
            res = admin_api.users.create(**kwargs)

        assert res is not None
        assert res.display_name == "Jane Doe"

        httpserver.expect_request(
            uri="/admin/v1/users",
            method="POST",
            headers={"Authorization": "Bearer sk_test"},
            json={},
        ).respond_with_json({"id": "usr_1"})

        kwargs = {"display_name": ""}
        if is_async:
            res = await async_admin_api.users.create(**kwargs)
        else:
            res = admin_api.users.create(**kwargs)
        assert res is not None
        assert res.display_name is None


@pytest.mark.asyncio
async def test_api_patch(
    admin_api: AdminApi,
    async_admin_api: AsyncAdminApi,
    httpserver: HTTPServer,
):
    for is_async in SYNC_ASYNC:
        httpserver.expect_oneshot_request(
            uri="/admin/v1/users/usr_1",
            method="PATCH",
            headers={"Authorization": "Bearer sk_test"},
            json={"displayName": "Jane Doe"},
        ).respond_with_json(
            {
                "id": "usr_1",
                "displayName": "Jane Doe",
            }
        )

        args, kwargs = ("usr_1",), {"display_name": "Jane Doe"}
        if is_async:
            res = await async_admin_api.users.update(*args, **kwargs)
        else:
            res = admin_api.users.update(*args, **kwargs)
        assert res is not None
        assert res.display_name == "Jane Doe"

        httpserver.expect_request(
            uri="/admin/v1/users/usr_1",
            method="PATCH",
            headers={"Authorization": "Bearer sk_test"},
            json={"displayName": ""},
        ).respond_with_json({"id": "usr_1"})

        args, kwargs = ("usr_1",), {"display_name": ""}
        if is_async:
            res = await async_admin_api.users.update(*args, **kwargs)
        else:
            res = admin_api.users.update(*args, **kwargs)
        assert res is not None
        assert res.display_name is None


@pytest.mark.asyncio
async def test_api_delete(
    admin_api: AdminApi,
    async_admin_api: AsyncAdminApi,
    httpserver: HTTPServer,
):
    for is_async in SYNC_ASYNC:
        httpserver.expect_oneshot_request(
            uri="/admin/v1/users/usr_1",
            method="DELETE",
            headers={"Authorization": "Bearer sk_test"},
        ).respond_with_json({"id": "usr_1"})

        args = ("usr_1",)
        if is_async:
            res = await async_admin_api.users.delete(*args)
        else:
            res = admin_api.users.delete(*args)
        assert res is not None
        assert res.id == "usr_1"


@pytest.mark.asyncio
async def test_api_error(
    admin_api: AdminApi,
    async_admin_api: AsyncAdminApi,
    httpserver: HTTPServer,
):
    for is_async in SYNC_ASYNC:
        httpserver.expect_oneshot_request(
            uri="/admin/v1/users/usr_1",
            method="GET",
            headers={"Authorization": "Bearer sk_test"},
        ).respond_with_json(
            {
                "code": "NOT_FOUND",
                "message": "Not Found",
                "metadata": {},
            },
            status=404,
        )

        args = ("usr_1",)
        if is_async:
            with pytest.raises(UserHubError) as ex:
                await async_admin_api.users.get(*args)
        else:
            with pytest.raises(UserHubError) as ex:
                admin_api.users.get(*args)

        assert str(ex.value) == "Not Found (call: admin.users.get, api_code: NOT_FOUND)"
        assert ex.value.api_code == Code.NOT_FOUND
        assert ex.value.message == "Not Found"
        assert ex.value.status_code == 404


@pytest.mark.asyncio
async def test_api_rate_limited(
    admin_api: AdminApi,
    async_admin_api: AsyncAdminApi,
    httpserver: HTTPServer,
):
    if not os.getenv("CI"):
        pytest.skip("Skipping slow test")

    for is_async in SYNC_ASYNC:
        for _ in range(6):
            httpserver.expect_ordered_request(
                uri="/admin/v1/users/usr_1",
                method="GET",
                headers={"Authorization": "Bearer sk_test"},
            ).respond_with_data(
                response_data="API call rate limited",
                status=429,
            )

        start_time = datetime.datetime.now(datetime.timezone.utc)

        args = ("usr_1",)
        if is_async:
            with pytest.raises(UserHubError) as ex:
                await async_admin_api.users.get(*args)
        else:
            with pytest.raises(UserHubError) as ex:
                admin_api.users.get(*args)

        end_time = datetime.datetime.now(datetime.timezone.utc)

        assert (
            str(ex.value)
            == "API call rate limited (call: admin.users.get, api_code: RESOURCE_EXHAUSTED)"
        )
        assert ex.value.api_code == Code.RESOURCE_EXHAUSTED
        assert ex.value.message == "API call rate limited"
        assert ex.value.status_code == 429

        diff = end_time - start_time
        assert diff >= datetime.timedelta(seconds=2)
        assert diff <= datetime.timedelta(seconds=4)
