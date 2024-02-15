# Code generated. DO NOT EDIT.

import pytest

from userhub_sdk._internal.test_transport import AsyncTestTransport, SyncTestTransport
from userhub_sdk.userapi._organizations import AsyncOrganizations, Organizations


def test_list():
    tr = SyncTestTransport()
    tr.body = """{
  "organizations": [
    {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "email": "test@example.com",
      "emailVerified": true,
      "imageUrl": "https://example.com/test.png",
      "disabled": true
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = Organizations(tr)

    res = n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/organizations"


def test_create():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "imageUrl": "https://example.com/test.png",
  "disabled": true
}"""

    n = Organizations(tr)

    res = n.create()
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/organizations"


def test_get():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "imageUrl": "https://example.com/test.png",
  "disabled": true
}"""

    n = Organizations(tr)

    res = n.get(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/organizations/organizationId"


def test_update():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "imageUrl": "https://example.com/test.png",
  "disabled": true
}"""

    n = Organizations(tr)

    res = n.update(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "PATCH"
    assert tr.request.path == "/user/v1/organizations/organizationId"


def test_delete():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "imageUrl": "https://example.com/test.png",
  "disabled": true
}"""

    n = Organizations(tr)

    res = n.delete(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/user/v1/organizations/organizationId"


def test_leave():
    tr = SyncTestTransport()
    tr.body = """{}"""

    n = Organizations(tr)

    res = n.leave(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/user/v1/organizations/organizationId:leave"


@pytest.mark.asyncio
async def test_async_list():
    tr = AsyncTestTransport()
    tr.body = """{
  "organizations": [
    {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "email": "test@example.com",
      "emailVerified": true,
      "imageUrl": "https://example.com/test.png",
      "disabled": true
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = AsyncOrganizations(tr)

    res = await n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/organizations"


@pytest.mark.asyncio
async def test_async_create():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "imageUrl": "https://example.com/test.png",
  "disabled": true
}"""

    n = AsyncOrganizations(tr)

    res = await n.create()
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/organizations"


@pytest.mark.asyncio
async def test_async_get():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "imageUrl": "https://example.com/test.png",
  "disabled": true
}"""

    n = AsyncOrganizations(tr)

    res = await n.get(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/organizations/organizationId"


@pytest.mark.asyncio
async def test_async_update():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "imageUrl": "https://example.com/test.png",
  "disabled": true
}"""

    n = AsyncOrganizations(tr)

    res = await n.update(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "PATCH"
    assert tr.request.path == "/user/v1/organizations/organizationId"


@pytest.mark.asyncio
async def test_async_delete():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "imageUrl": "https://example.com/test.png",
  "disabled": true
}"""

    n = AsyncOrganizations(tr)

    res = await n.delete(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/user/v1/organizations/organizationId"


@pytest.mark.asyncio
async def test_async_leave():
    tr = AsyncTestTransport()
    tr.body = """{}"""

    n = AsyncOrganizations(tr)

    res = await n.leave(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/user/v1/organizations/organizationId:leave"
