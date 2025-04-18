# Code generated. DO NOT EDIT.

import pytest

from userhub_sdk._internal.test_transport import AsyncTestTransport, SyncTestTransport
from userhub_sdk.adminapi._invoices import AsyncInvoices, Invoices


def test_list():
    tr = SyncTestTransport()
    tr.body = """{
  "invoices": [
    {
      "id": "string",
      "state": "DRAFT",
      "stateReason": "UPDATING",
      "stateTime": "2024-02-05T23:07:46.483Z",
      "externalId": "string",
      "number": "string",
      "currencyCode": "USD",
      "description": "string",
      "effectiveTime": "2024-02-05T23:07:46.483Z",
      "subtotalAmount": "10",
      "discountAmount": "0",
      "taxAmount": "0",
      "totalAmount": "10",
      "dueAmount": "10",
      "remainingDueAmount": "0",
      "dueTime": "2024-02-05T23:07:46.483Z",
      "paidAmount": "10",
      "paymentState": "PAYMENT_METHOD_REQUIRED",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = Invoices(tr)

    res = n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/invoices"


def test_get():
    tr = SyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "DRAFT",
  "stateReason": "UPDATING",
  "stateTime": "2024-02-05T23:07:46.483Z",
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
    "view": "BASIC",
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
  "number": "string",
  "currencyCode": "USD",
  "description": "string",
  "account": {
    "fullName": "Jane Doe",
    "email": "test@example.com",
    "phoneNumber": "+12125550123",
    "address": {
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    }
  },
  "effectiveTime": "2024-02-05T23:07:46.483Z",
  "period": {
    "startTime": "2024-02-05T23:07:46.483Z",
    "endTime": "2024-02-05T23:07:46.483Z"
  },
  "subtotalAmount": "10",
  "discountAmount": "0",
  "balance": {
    "startAmount": "10",
    "endAmount": "10",
    "appliedAmount": "10"
  },
  "taxAmount": "0",
  "totalAmount": "10",
  "dueAmount": "10",
  "remainingDueAmount": "0",
  "dueTime": "2024-02-05T23:07:46.483Z",
  "paidAmount": "10",
  "paymentState": "PAYMENT_METHOD_REQUIRED",
  "paymentIntent": {
    "stripe": {
      "accountId": "string",
      "live": true,
      "clientSecret": "string"
    }
  },
  "items": [
    {
      "id": "string",
      "quantity": 1,
      "subtotalAmount": "10",
      "discountAmount": "0",
      "description": "string",
      "externalId": "string",
      "proration": true
    }
  ],
  "changes": [
    {
      "time": "2024-02-05T23:07:46.483Z",
      "description": "string",
      "subtotalAmount": "10",
      "discountAmount": "0",
      "startQuantity": 1,
      "endQuantity": 1,
      "startItemIds": [],
      "endItemIds": []
    }
  ],
  "pullTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = Invoices(tr)

    res = n.get(invoice_id="invoiceId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/invoices/invoiceId"


@pytest.mark.asyncio
async def test_async_list():
    tr = AsyncTestTransport()
    tr.body = """{
  "invoices": [
    {
      "id": "string",
      "state": "DRAFT",
      "stateReason": "UPDATING",
      "stateTime": "2024-02-05T23:07:46.483Z",
      "externalId": "string",
      "number": "string",
      "currencyCode": "USD",
      "description": "string",
      "effectiveTime": "2024-02-05T23:07:46.483Z",
      "subtotalAmount": "10",
      "discountAmount": "0",
      "taxAmount": "0",
      "totalAmount": "10",
      "dueAmount": "10",
      "remainingDueAmount": "0",
      "dueTime": "2024-02-05T23:07:46.483Z",
      "paidAmount": "10",
      "paymentState": "PAYMENT_METHOD_REQUIRED",
      "pullTime": "2024-02-05T23:07:46.483Z",
      "createTime": "2024-02-05T23:07:46.483Z",
      "updateTime": "2024-02-05T23:07:46.483Z"
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}"""

    n = AsyncInvoices(tr)

    res = await n.list()
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/invoices"


@pytest.mark.asyncio
async def test_async_get():
    tr = AsyncTestTransport()
    tr.body = """{
  "id": "string",
  "state": "DRAFT",
  "stateReason": "UPDATING",
  "stateTime": "2024-02-05T23:07:46.483Z",
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
    "view": "BASIC",
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
  "number": "string",
  "currencyCode": "USD",
  "description": "string",
  "account": {
    "fullName": "Jane Doe",
    "email": "test@example.com",
    "phoneNumber": "+12125550123",
    "address": {
      "lines": [],
      "city": "Brooklyn",
      "state": "string",
      "postalCode": "11222",
      "country": "US"
    }
  },
  "effectiveTime": "2024-02-05T23:07:46.483Z",
  "period": {
    "startTime": "2024-02-05T23:07:46.483Z",
    "endTime": "2024-02-05T23:07:46.483Z"
  },
  "subtotalAmount": "10",
  "discountAmount": "0",
  "balance": {
    "startAmount": "10",
    "endAmount": "10",
    "appliedAmount": "10"
  },
  "taxAmount": "0",
  "totalAmount": "10",
  "dueAmount": "10",
  "remainingDueAmount": "0",
  "dueTime": "2024-02-05T23:07:46.483Z",
  "paidAmount": "10",
  "paymentState": "PAYMENT_METHOD_REQUIRED",
  "paymentIntent": {
    "stripe": {
      "accountId": "string",
      "live": true,
      "clientSecret": "string"
    }
  },
  "items": [
    {
      "id": "string",
      "quantity": 1,
      "subtotalAmount": "10",
      "discountAmount": "0",
      "description": "string",
      "externalId": "string",
      "proration": true
    }
  ],
  "changes": [
    {
      "time": "2024-02-05T23:07:46.483Z",
      "description": "string",
      "subtotalAmount": "10",
      "discountAmount": "0",
      "startQuantity": 1,
      "endQuantity": 1,
      "startItemIds": [],
      "endItemIds": []
    }
  ],
  "pullTime": "2024-02-05T23:07:46.483Z",
  "createTime": "2024-02-05T23:07:46.483Z",
  "updateTime": "2024-02-05T23:07:46.483Z"
}"""

    n = AsyncInvoices(tr)

    res = await n.get(invoice_id="invoiceId")
    assert res is not None
    assert tr.request.method == "GET"
    assert tr.request.path == "/admin/v1/invoices/invoiceId"
