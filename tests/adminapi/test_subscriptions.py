# Code generated. DO NOT EDIT.

import pytest

from userhub_sdk._internal.test_transport import AsyncTestTransport, SyncTestTransport
from userhub_sdk.adminapi._subscriptions import AsyncSubscriptions, Subscriptions


def test_list():
    tr = SyncTestTransport()
    tr.body = """{
  "subscriptions": [
    {
      "id": "string",
      "state": "ACTIVE",
      "stateReason": "UPDATING",
      "externalId": "string",
      "currencyCode": "USD",
      "cancelPeriodEnd": true,
      "anchorTime": "2024-02-05T23:07:46.483Z",
      "startTime": "2024-02-05T23:07:46.483Z",
      "endTime": "2024-02-05T23:07:46.483Z",
      "default": true,
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = Subscriptions(tr)

    res = n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/subscriptions"


def test_get():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "UPDATING",
  "connection": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
    "type": "AMAZON_COGNITO",
    "delegate": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "state": "ACTIVE",
      "stateReason": "UPDATING",
      "type": "AMAZON_COGNITO"
    },
    "providers": [],
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z",
    "amazonCognito": {
      "userPoolId": "string",
      "region": "string",
      "accessKeyId": "string",
      "accessKeySecret": "string"
    },
    "auth0": {
      "domain": "string",
      "clientId": "string",
      "clientSecret": "string"
    },
    "builtinEmail": {
      "allowedEmails": []
    },
    "googleCloudIdentityPlatform": {
      "credentials": "string",
      "projectId": "string"
    },
    "postmark": {
      "serverToken": "string",
      "serverId": "string",
      "allowedEmails": []
    },
    "stripe": {
      "accountId": "string",
      "live": true
    },
    "webhook": {
      "url": "https://example.com",
      "headers": {}
    }
  },
  "externalId": "string",
  "plan": {
    "id": "string",
    "displayName": "Test",
    "description": "string",
    "currencyCode": "USD",
    "billingInterval": {
      "quantity": 1,
      "unit": "DAY"
    },
    "tags": [
      "string"
    ],
    "items": []
  },
  "currencyCode": "USD",
  "items": [
    {
      "id": "string",
      "quantity": 1
    }
  ],
  "seats": [
    {
      "currentPeriodQuantity": 1,
      "nextPeriodQuantity": 1,
      "assignedQuantity": 1,
      "unassignedQuantity": 1,
      "totalQuantity": 1
    }
  ],
  "paymentMethod": {
    "id": "string",
    "externalId": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
    "type": "CARD",
    "displayName": "Test",
    "fullName": "Jane Doe",
    "address": {
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    },
    "default": true,
    "lastPaymentError": {
      "code": "OK",
      "message": "string",
      "reason": "string",
      "param": "string",
      "metadata": {},
      "localeMessage": "string"
    },
    "pullTime": "2024-02-05T23:07:46.483Z",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z",
    "card": {
      "brand": "AMERICAN_EXPRESS",
      "last4": "string",
      "fundingType": "CREDIT",
      "expYear": 1,
      "expMonth": 1
    }
  },
  "cancelPeriodEnd": true,
  "anchorTime": "2024-02-05T23:07:46.483Z",
  "startTime": "2024-02-05T23:07:46.483Z",
  "endTime": "2024-02-05T23:07:46.483Z",
  "trial": {
    "startTime": "2024-02-05T23:07:46.483Z",
    "endTime": "2024-02-05T23:07:46.483Z",
    "days": 1,
    "remainingDays": 1
  },
  "currentPeriod": {
    "startTime": "2024-02-05T23:07:46.483Z",
    "endTime": "2024-02-05T23:07:46.483Z"
  },
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
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "default": true,
  "pullTime": "2024-02-05T23:07:46.483Z",
  "pushTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Subscriptions(tr)

    res = n.get(subscription_id="subscriptionId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/subscriptions/subscriptionId"


@pytest.mark.asyncio
async def test_async_list():
    tr = AsyncTestTransport()
    tr.body = """{
  "subscriptions": [
    {
      "id": "string",
      "state": "ACTIVE",
      "stateReason": "UPDATING",
      "externalId": "string",
      "currencyCode": "USD",
      "cancelPeriodEnd": true,
      "anchorTime": "2024-02-05T23:07:46.483Z",
      "startTime": "2024-02-05T23:07:46.483Z",
      "endTime": "2024-02-05T23:07:46.483Z",
      "default": true,
      "pullTime": "2024-02-05T23:07:46.483Z",
      "pushTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = AsyncSubscriptions(tr)

    res = await n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/subscriptions"


@pytest.mark.asyncio
async def test_async_get():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "ACTIVE",
  "stateReason": "UPDATING",
  "connection": {
    "id": "string",
    "uniqueId": "test",
    "displayName": "Test",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
    "type": "AMAZON_COGNITO",
    "delegate": {
      "id": "string",
      "uniqueId": "test",
      "displayName": "Test",
      "state": "ACTIVE",
      "stateReason": "UPDATING",
      "type": "AMAZON_COGNITO"
    },
    "providers": [],
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z",
    "amazonCognito": {
      "userPoolId": "string",
      "region": "string",
      "accessKeyId": "string",
      "accessKeySecret": "string"
    },
    "auth0": {
      "domain": "string",
      "clientId": "string",
      "clientSecret": "string"
    },
    "builtinEmail": {
      "allowedEmails": []
    },
    "googleCloudIdentityPlatform": {
      "credentials": "string",
      "projectId": "string"
    },
    "postmark": {
      "serverToken": "string",
      "serverId": "string",
      "allowedEmails": []
    },
    "stripe": {
      "accountId": "string",
      "live": true
    },
    "webhook": {
      "url": "https://example.com",
      "headers": {}
    }
  },
  "externalId": "string",
  "plan": {
    "id": "string",
    "displayName": "Test",
    "description": "string",
    "currencyCode": "USD",
    "billingInterval": {
      "quantity": 1,
      "unit": "DAY"
    },
    "tags": [
      "string"
    ],
    "items": []
  },
  "currencyCode": "USD",
  "items": [
    {
      "id": "string",
      "quantity": 1
    }
  ],
  "seats": [
    {
      "currentPeriodQuantity": 1,
      "nextPeriodQuantity": 1,
      "assignedQuantity": 1,
      "unassignedQuantity": 1,
      "totalQuantity": 1
    }
  ],
  "paymentMethod": {
    "id": "string",
    "externalId": "string",
    "state": "ACTIVE",
    "stateReason": "UPDATING",
    "type": "CARD",
    "displayName": "Test",
    "fullName": "Jane Doe",
    "address": {
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    },
    "default": true,
    "lastPaymentError": {
      "code": "OK",
      "message": "string",
      "reason": "string",
      "param": "string",
      "metadata": {},
      "localeMessage": "string"
    },
    "pullTime": "2024-02-05T23:07:46.483Z",
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z",
    "card": {
      "brand": "AMERICAN_EXPRESS",
      "last4": "string",
      "fundingType": "CREDIT",
      "expYear": 1,
      "expMonth": 1
    }
  },
  "cancelPeriodEnd": true,
  "anchorTime": "2024-02-05T23:07:46.483Z",
  "startTime": "2024-02-05T23:07:46.483Z",
  "endTime": "2024-02-05T23:07:46.483Z",
  "trial": {
    "startTime": "2024-02-05T23:07:46.483Z",
    "endTime": "2024-02-05T23:07:46.483Z",
    "days": 1,
    "remainingDays": 1
  },
  "currentPeriod": {
    "startTime": "2024-02-05T23:07:46.483Z",
    "endTime": "2024-02-05T23:07:46.483Z"
  },
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
    "createTime": "2024-02-05T23:07:46.483Z",
    "updateTime": "2024-02-05T23:07:46.483Z"
  },
  "default": true,
  "pullTime": "2024-02-05T23:07:46.483Z",
  "pushTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncSubscriptions(tr)

    res = await n.get(subscription_id="subscriptionId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/subscriptions/subscriptionId"
