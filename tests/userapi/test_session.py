# Code generated. DO NOT EDIT.

import pytest

from userhub_sdk._internal.test_transport import AsyncTestTransport, SyncTestTransport
from userhub_sdk.userapi._session import AsyncSession, Session


def test_get():
    tr = SyncTestTransport()
    tr.body = """{
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "memberships": [
    {}
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    },
    "seat": {}
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "scopes": [
    "string"
  ]
}"""

    n = Session(tr)

    res = n.get()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/session"


def test_exchange_token():
    tr = SyncTestTransport()
    tr.body = """{
  "accessToken": "string",
  "expireTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Session(tr)

    res = n.exchange_token(token="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/session:exchangeToken"


def test_create_portal():
    tr = SyncTestTransport()
    tr.body = """{
  "redirectUrl": "https://example.com"
}"""

    n = Session(tr)

    res = n.create_portal()
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/session:createPortal"


@pytest.mark.asyncio
async def test_async_get():
    tr = AsyncTestTransport()
    tr.body = """{
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "memberships": [
    {}
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    },
    "seat": {}
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "scopes": [
    "string"
  ]
}"""

    n = AsyncSession(tr)

    res = await n.get()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/session"


@pytest.mark.asyncio
async def test_async_exchange_token():
    tr = AsyncTestTransport()
    tr.body = """{
  "accessToken": "string",
  "expireTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncSession(tr)

    res = await n.exchange_token(token="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/session:exchangeToken"


@pytest.mark.asyncio
async def test_async_create_portal():
    tr = AsyncTestTransport()
    tr.body = """{
  "redirectUrl": "https://example.com"
}"""

    n = AsyncSession(tr)

    res = await n.create_portal()
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/session:createPortal"
