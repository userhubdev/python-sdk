# Code generated. DO NOT EDIT.

import pytest

from userhub_sdk.userapi._flows import AsyncFlows, Flows
from userhub_sdk._internal.test_transport import AsyncTestTransport, SyncTestTransport


def test_list():
    tr = SyncTestTransport()
    tr.body = """{
  "flows": [
    {
      "id": "string",
      "state": "START_PENDING",
      "stateReason": "DELETED",
      "type": "JOIN_ORGANIZATION",
      "expireTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = Flows(tr)

    res = n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/flows"


def test_create_join_organization():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "DELETED",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "creator": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com"
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = Flows(tr)

    res = n.create_join_organization(organization_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/flows:createJoinOrganization"


def test_get():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "DELETED",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "creator": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com"
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = Flows(tr)

    res = n.get(flow_id="flowId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/flows/flowId"


def test_consume():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "DELETED",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "creator": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com"
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = Flows(tr)

    res = n.consume(flow_id="flowId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/flows/flowId:consume"


def test_cancel():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "DELETED",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "creator": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com"
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = Flows(tr)

    res = n.cancel(flow_id="flowId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/flows/flowId:cancel"


@pytest.mark.asyncio
async def test_async_list():
    tr = AsyncTestTransport()
    tr.body = """{
  "flows": [
    {
      "id": "string",
      "state": "START_PENDING",
      "stateReason": "DELETED",
      "type": "JOIN_ORGANIZATION",
      "expireTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = AsyncFlows(tr)

    res = await n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/flows"


@pytest.mark.asyncio
async def test_async_create_join_organization():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "DELETED",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "creator": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com"
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = AsyncFlows(tr)

    res = await n.create_join_organization(organization_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/flows:createJoinOrganization"


@pytest.mark.asyncio
async def test_async_get():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "DELETED",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "creator": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com"
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = AsyncFlows(tr)

    res = await n.get(flow_id="flowId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/user/v1/flows/flowId"


@pytest.mark.asyncio
async def test_async_consume():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "DELETED",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "creator": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com"
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = AsyncFlows(tr)

    res = await n.consume(flow_id="flowId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/flows/flowId:consume"


@pytest.mark.asyncio
async def test_async_cancel():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "DELETED",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "user": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "creator": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "email": "test@example.com",
    "emailVerified": true,
    "imageUrl": "https://example.com/test.png",
    "disabled": true
  },
  "expireTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com"
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = AsyncFlows(tr)

    res = await n.cancel(flow_id="flowId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/user/v1/flows/flowId:cancel"
