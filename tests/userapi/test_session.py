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
