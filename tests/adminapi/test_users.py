# Code generated. DO NOT EDIT.

import pytest

from userhub_sdk._internal.test_transport import AsyncTestTransport, SyncTestTransport
from userhub_sdk.adminapi._users import AsyncUsers, Users


def test_list():
    tr = SyncTestTransport()
    tr.body = """{
  "users": [
    {
      "id": "string",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "uniqueId": "test",
      "displayName": "Test",
      "email": "test@example.com",
      "emailVerified": true,
      "phoneNumber": "+12125550123",
      "phoneNumberVerified": true,
      "imageUrl": "https://example.com/test.png",
      "currencyCode": "USD",
      "languageCode": "en",
      "regionCode": "US",
      "timeZone": "America/New_York",
      "signupTime": "2024-02-05T23:07:46.483Z",
      "disabled": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = Users(tr)

    res = n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/users"


def test_create():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.create()
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users"


def test_get():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.get(user_id="userId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/users/userId"


def test_update():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.update(user_id="userId")
    assert res is not None
    assert tr.request.method == "PATCH"
    assert tr.request.path == "/admin/v1/users/userId"


def test_delete():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.delete(user_id="userId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/admin/v1/users/userId"


def test_undelete():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.undelete(user_id="userId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:undelete"


def test_connect():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.connect(user_id="userId", connection_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:connect"


def test_disconnect():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.disconnect(user_id="userId", connection_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:disconnect"


def test_import_account():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.import_account(user_id="userId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:import"


def test_create_api_session():
    tr = SyncTestTransport()
    tr.body = """{
  "accessToken": "string",
  "expireTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Users(tr)

    res = n.create_api_session(user_id="userId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:createApiSession"


def test_create_portal_session():
    tr = SyncTestTransport()
    tr.body = """{
  "redirectUrl": "https://example.com"
}"""

    n = Users(tr)

    res = n.create_portal_session(user_id="userId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:createPortalSession"


@pytest.mark.asyncio
async def test_async_list():
    tr = AsyncTestTransport()
    tr.body = """{
  "users": [
    {
      "id": "string",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "uniqueId": "test",
      "displayName": "Test",
      "email": "test@example.com",
      "emailVerified": true,
      "phoneNumber": "+12125550123",
      "phoneNumberVerified": true,
      "imageUrl": "https://example.com/test.png",
      "currencyCode": "USD",
      "languageCode": "en",
      "regionCode": "US",
      "timeZone": "America/New_York",
      "signupTime": "2024-02-05T23:07:46.483Z",
      "disabled": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = AsyncUsers(tr)

    res = await n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/users"


@pytest.mark.asyncio
async def test_async_create():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.create()
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users"


@pytest.mark.asyncio
async def test_async_get():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.get(user_id="userId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/users/userId"


@pytest.mark.asyncio
async def test_async_update():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.update(user_id="userId")
    assert res is not None
    assert tr.request.method == "PATCH"
    assert tr.request.path == "/admin/v1/users/userId"


@pytest.mark.asyncio
async def test_async_delete():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.delete(user_id="userId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/admin/v1/users/userId"


@pytest.mark.asyncio
async def test_async_undelete():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.undelete(user_id="userId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:undelete"


@pytest.mark.asyncio
async def test_async_connect():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.connect(user_id="userId", connection_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:connect"


@pytest.mark.asyncio
async def test_async_disconnect():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.disconnect(user_id="userId", connection_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:disconnect"


@pytest.mark.asyncio
async def test_async_import_account():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "DELETED",
  "uniqueId": "test",
  "displayName": "Test",
  "email": "test@example.com",
  "emailVerified": true,
  "phoneNumber": "+12125550123",
  "phoneNumberVerified": true,
  "imageUrl": "https://example.com/test.png",
  "currencyCode": "USD",
  "languageCode": "en",
  "regionCode": "US",
  "timeZone": "America/New_York",
  "address": {
    "lines": [
      "string"
    ],
    "city": "Brooklyn",
    "state": "string",
    "postalCode": "11222",
    "country": "US"
  },
  "accountConnections": [
    {
      "externalId": "string",
      "adminUrl": "https://example.com",
      "state": "ACTIVE",
      "stateReason": "DELETED",
      "balanceAmount": "string",
      "currencyCode": "USD",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "subscription": {
    "id": "string",
    "state": "ACTIVE",
    "anchorTime": "2024-02-05T23:07:46.483Z",
    "plan": {
      "id": "string",
      "displayName": "Test"
    }
  },
  "memberships": [
    {
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "signupTime": "2024-02-05T23:07:46.483Z",
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.import_account(user_id="userId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:import"


@pytest.mark.asyncio
async def test_async_create_api_session():
    tr = AsyncTestTransport()
    tr.body = """{
  "accessToken": "string",
  "expireTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncUsers(tr)

    res = await n.create_api_session(user_id="userId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:createApiSession"


@pytest.mark.asyncio
async def test_async_create_portal_session():
    tr = AsyncTestTransport()
    tr.body = """{
  "redirectUrl": "https://example.com"
}"""

    n = AsyncUsers(tr)

    res = await n.create_portal_session(user_id="userId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/users/userId:createPortalSession"
