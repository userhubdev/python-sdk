# Code generated. DO NOT EDIT.

import pytest

from userhub_sdk._internal.test_transport import AsyncTestTransport, SyncTestTransport
from userhub_sdk.adminapi._organizations import AsyncOrganizations, Organizations


def test_list():
    tr = SyncTestTransport()
    tr.body = """{
  "organizations": [
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
      "memberCount": 1,
      "disabled": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = Organizations(tr)

    res = n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/organizations"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.create()
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.get(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/organizations/organizationId"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.update(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "PATCH"
    assert tr.request.path == "/admin/v1/organizations/organizationId"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.delete(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/admin/v1/organizations/organizationId"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.undelete(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations/organizationId:undelete"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.connect(organization_id="organizationId", connection_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations/organizationId:connect"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.disconnect(organization_id="organizationId", connection_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations/organizationId:disconnect"


def test_list_members():
    tr = SyncTestTransport()
    tr.body = """{
  "members": [
    {
      "state": "ACTIVE",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = Organizations(tr)

    res = n.list_members(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members"


def test_add_member():
    tr = SyncTestTransport()
    tr.body = """{
  "state": "ACTIVE",
  "user": {
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
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    },
    "accountConnections": [],
    "subscription": {
      "id": "string",
      "state": "ACTIVE",
      "anchorTime": "2024-02-05T23:07:46.483Z"
    },
    "memberships": [],
    "signupTime": "2024-02-05T23:07:46.483Z",
    "disabled": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "role": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "type": "OWNER",
    "description": "string",
    "permissionSets": [
      "string"
    ],
    "default": true,
    "archived": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "seat": {
    "product": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test"
    }
  },
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.add_member(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members"


def test_get_member():
    tr = SyncTestTransport()
    tr.body = """{
  "state": "ACTIVE",
  "user": {
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
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    },
    "accountConnections": [],
    "subscription": {
      "id": "string",
      "state": "ACTIVE",
      "anchorTime": "2024-02-05T23:07:46.483Z"
    },
    "memberships": [],
    "signupTime": "2024-02-05T23:07:46.483Z",
    "disabled": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "role": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "type": "OWNER",
    "description": "string",
    "permissionSets": [
      "string"
    ],
    "default": true,
    "archived": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "seat": {
    "product": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test"
    }
  },
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.get_member(organization_id="organizationId", user_id="userId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members/userId"


def test_update_member():
    tr = SyncTestTransport()
    tr.body = """{
  "state": "ACTIVE",
  "user": {
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
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    },
    "accountConnections": [],
    "subscription": {
      "id": "string",
      "state": "ACTIVE",
      "anchorTime": "2024-02-05T23:07:46.483Z"
    },
    "memberships": [],
    "signupTime": "2024-02-05T23:07:46.483Z",
    "disabled": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "role": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "type": "OWNER",
    "description": "string",
    "permissionSets": [
      "string"
    ],
    "default": true,
    "archived": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "seat": {
    "product": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test"
    }
  },
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Organizations(tr)

    res = n.update_member(organization_id="organizationId", user_id="userId")
    assert res is not None
    assert tr.request.method == "PATCH"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members/userId"


def test_remove_member():
    tr = SyncTestTransport()
    tr.body = """{}"""

    n = Organizations(tr)

    res = n.remove_member(organization_id="organizationId", user_id="userId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members/userId"


@pytest.mark.asyncio
async def test_async_list():
    tr = AsyncTestTransport()
    tr.body = """{
  "organizations": [
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
      "memberCount": 1,
      "disabled": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = AsyncOrganizations(tr)

    res = await n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/organizations"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.create()
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.get(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/organizations/organizationId"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.update(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "PATCH"
    assert tr.request.path == "/admin/v1/organizations/organizationId"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.delete(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/admin/v1/organizations/organizationId"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.undelete(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations/organizationId:undelete"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.connect(organization_id="organizationId", connection_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations/organizationId:connect"


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
  "signupTime": "2024-02-05T23:07:46.483Z",
  "memberCount": 1,
  "disabled": true,
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.disconnect(organization_id="organizationId", connection_id="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations/organizationId:disconnect"


@pytest.mark.asyncio
async def test_async_list_members():
    tr = AsyncTestTransport()
    tr.body = """{
  "members": [
    {
      "state": "ACTIVE",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = AsyncOrganizations(tr)

    res = await n.list_members(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members"


@pytest.mark.asyncio
async def test_async_add_member():
    tr = AsyncTestTransport()
    tr.body = """{
  "state": "ACTIVE",
  "user": {
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
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    },
    "accountConnections": [],
    "subscription": {
      "id": "string",
      "state": "ACTIVE",
      "anchorTime": "2024-02-05T23:07:46.483Z"
    },
    "memberships": [],
    "signupTime": "2024-02-05T23:07:46.483Z",
    "disabled": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "role": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "type": "OWNER",
    "description": "string",
    "permissionSets": [
      "string"
    ],
    "default": true,
    "archived": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "seat": {
    "product": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test"
    }
  },
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.add_member(organization_id="organizationId")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members"


@pytest.mark.asyncio
async def test_async_get_member():
    tr = AsyncTestTransport()
    tr.body = """{
  "state": "ACTIVE",
  "user": {
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
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    },
    "accountConnections": [],
    "subscription": {
      "id": "string",
      "state": "ACTIVE",
      "anchorTime": "2024-02-05T23:07:46.483Z"
    },
    "memberships": [],
    "signupTime": "2024-02-05T23:07:46.483Z",
    "disabled": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "role": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "type": "OWNER",
    "description": "string",
    "permissionSets": [
      "string"
    ],
    "default": true,
    "archived": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "seat": {
    "product": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test"
    }
  },
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.get_member(organization_id="organizationId", user_id="userId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members/userId"


@pytest.mark.asyncio
async def test_async_update_member():
    tr = AsyncTestTransport()
    tr.body = """{
  "state": "ACTIVE",
  "user": {
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
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    },
    "accountConnections": [],
    "subscription": {
      "id": "string",
      "state": "ACTIVE",
      "anchorTime": "2024-02-05T23:07:46.483Z"
    },
    "memberships": [],
    "signupTime": "2024-02-05T23:07:46.483Z",
    "disabled": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "role": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "type": "OWNER",
    "description": "string",
    "permissionSets": [
      "string"
    ],
    "default": true,
    "archived": true,
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "seat": {
    "product": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test"
    }
  },
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncOrganizations(tr)

    res = await n.update_member(organization_id="organizationId", user_id="userId")
    assert res is not None
    assert tr.request.method == "PATCH"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members/userId"


@pytest.mark.asyncio
async def test_async_remove_member():
    tr = AsyncTestTransport()
    tr.body = """{}"""

    n = AsyncOrganizations(tr)

    res = await n.remove_member(organization_id="organizationId", user_id="userId")
    assert res is not None
    assert tr.request.method == "DELETE"
    assert tr.request.path == "/admin/v1/organizations/organizationId/members/userId"
