# Code generated. DO NOT EDIT.

import pytest

from userhub_sdk._internal.test_transport import AsyncTestTransport, SyncTestTransport
from userhub_sdk.adminapi._flows import AsyncFlows, Flows


def test_list():
    tr = SyncTestTransport()
    tr.body = """{
  "flows": [
    {
      "id": "string",
      "state": "START_PENDING",
      "stateReason": "UPDATING",
      "type": "JOIN_ORGANIZATION",
      "startTime": "2024-02-05T23:07:46.483Z",
      "expireTime": "2024-02-05T23:07:46.483Z",
      "ttl": "string",
      "secret": "string",
      "view": "BASIC",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = Flows(tr)

    res = n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/flows"


def test_create_join_organization():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "UPDATING",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "signupTime": "2024-02-05T23:07:46.483Z",
    "memberCount": 1,
    "disabled": true,
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "user": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "creator": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "startTime": "2024-02-05T23:07:46.483Z",
  "expireTime": "2024-02-05T23:07:46.483Z",
  "ttl": "string",
  "secret": "string",
  "view": "BASIC",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com",
    "role": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "type": "OWNER",
      "description": "string",
      "seatPolicy": "DEFAULT",
      "permissionSets": [],
      "default": true,
      "archived": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
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
    assert tr.request.path == "/admin/v1/flows:createJoinOrganization"


def test_create_signup():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "UPDATING",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "signupTime": "2024-02-05T23:07:46.483Z",
    "memberCount": 1,
    "disabled": true,
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "user": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "creator": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "startTime": "2024-02-05T23:07:46.483Z",
  "expireTime": "2024-02-05T23:07:46.483Z",
  "ttl": "string",
  "secret": "string",
  "view": "BASIC",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com",
    "role": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "type": "OWNER",
      "description": "string",
      "seatPolicy": "DEFAULT",
      "permissionSets": [],
      "default": true,
      "archived": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = Flows(tr)

    res = n.create_signup(email="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/flows:createSignup"


def test_get():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "UPDATING",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "signupTime": "2024-02-05T23:07:46.483Z",
    "memberCount": 1,
    "disabled": true,
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "user": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "creator": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "startTime": "2024-02-05T23:07:46.483Z",
  "expireTime": "2024-02-05T23:07:46.483Z",
  "ttl": "string",
  "secret": "string",
  "view": "BASIC",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com",
    "role": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "type": "OWNER",
      "description": "string",
      "seatPolicy": "DEFAULT",
      "permissionSets": [],
      "default": true,
      "archived": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
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
    assert tr.request.path == "/admin/v1/flows/flowId"


def test_cancel():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "UPDATING",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "signupTime": "2024-02-05T23:07:46.483Z",
    "memberCount": 1,
    "disabled": true,
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "user": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "creator": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "startTime": "2024-02-05T23:07:46.483Z",
  "expireTime": "2024-02-05T23:07:46.483Z",
  "ttl": "string",
  "secret": "string",
  "view": "BASIC",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com",
    "role": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "type": "OWNER",
      "description": "string",
      "seatPolicy": "DEFAULT",
      "permissionSets": [],
      "default": true,
      "archived": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
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
    assert tr.request.path == "/admin/v1/flows/flowId:cancel"


@pytest.mark.asyncio
async def test_async_list():
    tr = AsyncTestTransport()
    tr.body = """{
  "flows": [
    {
      "id": "string",
      "state": "START_PENDING",
      "stateReason": "UPDATING",
      "type": "JOIN_ORGANIZATION",
      "startTime": "2024-02-05T23:07:46.483Z",
      "expireTime": "2024-02-05T23:07:46.483Z",
      "ttl": "string",
      "secret": "string",
      "view": "BASIC",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = AsyncFlows(tr)

    res = await n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/flows"


@pytest.mark.asyncio
async def test_async_create_join_organization():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "UPDATING",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "signupTime": "2024-02-05T23:07:46.483Z",
    "memberCount": 1,
    "disabled": true,
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "user": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "creator": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "startTime": "2024-02-05T23:07:46.483Z",
  "expireTime": "2024-02-05T23:07:46.483Z",
  "ttl": "string",
  "secret": "string",
  "view": "BASIC",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com",
    "role": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "type": "OWNER",
      "description": "string",
      "seatPolicy": "DEFAULT",
      "permissionSets": [],
      "default": true,
      "archived": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
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
    assert tr.request.path == "/admin/v1/flows:createJoinOrganization"


@pytest.mark.asyncio
async def test_async_create_signup():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "UPDATING",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "signupTime": "2024-02-05T23:07:46.483Z",
    "memberCount": 1,
    "disabled": true,
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "user": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "creator": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "startTime": "2024-02-05T23:07:46.483Z",
  "expireTime": "2024-02-05T23:07:46.483Z",
  "ttl": "string",
  "secret": "string",
  "view": "BASIC",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com",
    "role": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "type": "OWNER",
      "description": "string",
      "seatPolicy": "DEFAULT",
      "permissionSets": [],
      "default": true,
      "archived": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  },
  "signup": {
    "email": "test@example.com",
    "displayName": "Test",
    "createOrganization": true
  }
}"""

    n = AsyncFlows(tr)

    res = await n.create_signup(email="")
    assert res is not None
    assert tr.request.method == "POST"
    assert tr.request.path == "/admin/v1/flows:createSignup"


@pytest.mark.asyncio
async def test_async_get():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "UPDATING",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "signupTime": "2024-02-05T23:07:46.483Z",
    "memberCount": 1,
    "disabled": true,
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "user": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "creator": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "startTime": "2024-02-05T23:07:46.483Z",
  "expireTime": "2024-02-05T23:07:46.483Z",
  "ttl": "string",
  "secret": "string",
  "view": "BASIC",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com",
    "role": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "type": "OWNER",
      "description": "string",
      "seatPolicy": "DEFAULT",
      "permissionSets": [],
      "default": true,
      "archived": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
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
    assert tr.request.path == "/admin/v1/flows/flowId"


@pytest.mark.asyncio
async def test_async_cancel():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "START_PENDING",
  "stateReason": "UPDATING",
  "type": "JOIN_ORGANIZATION",
  "organization": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "signupTime": "2024-02-05T23:07:46.483Z",
    "memberCount": 1,
    "disabled": true,
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "user": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "creator": {
    "id": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
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
    "view": "BASIC",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "startTime": "2024-02-05T23:07:46.483Z",
  "expireTime": "2024-02-05T23:07:46.483Z",
  "ttl": "string",
  "secret": "string",
  "view": "BASIC",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z",
  "joinOrganization": {
    "displayName": "Test",
    "email": "test@example.com",
    "role": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "type": "OWNER",
      "description": "string",
      "seatPolicy": "DEFAULT",
      "permissionSets": [],
      "default": true,
      "archived": true,
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
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
    assert tr.request.path == "/admin/v1/flows/flowId:cancel"
