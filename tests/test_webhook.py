# Code generated. DO NOT EDIT.

import hashlib
import hmac
import json
import time
from dataclasses import dataclass

import pytest

from userhub_sdk._internal import constants
from userhub_sdk.connectionsv1 import (
    CustomUser,
    GetCustomUserRequest,
    ListCustomUsersRequest,
    ListCustomUsersResponse,
)
from userhub_sdk.eventsv1 import Event
from userhub_sdk.types import Code, UserHubError
from userhub_sdk.webhook import (
    Webhook,
    WebhookRequest,
    WebhookResponse,
    WebhookUserNotFound,
)
from userhub_sdk.webhook._http import add_header, get_header


@dataclass
class WebhookTest:
    name: str
    secret: str
    request: WebhookRequest
    response: WebhookResponse
    set_timestamp: bool = False
    set_signature: bool = False
    add_signature: bool = False


@pytest.mark.parametrize(
    "test",
    [
        WebhookTest(
            name="Signing secret is required",
            secret="",
            request=WebhookRequest(),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"Signing secret is required","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="Headers are required",
            secret="test",
            request=WebhookRequest(),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"Headers are required","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="Body is required",
            secret="test",
            request=WebhookRequest(
                headers={
                    "content-type": "application/json",
                },
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"Body is required","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="UserHub-Action header is missing",
            secret="test",
            request=WebhookRequest(
                headers={
                    "content-type": "application/json",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"UserHub-Action header is missing","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="UserHub-Timestamp header is missing",
            secret="test",
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"UserHub-Timestamp header is missing","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="UserHub-Signature header is missing",
            secret="test",
            set_timestamp=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"UserHub-Signature header is missing","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="Signatures normalized to nothing",
            secret="test",
            set_timestamp=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                    "UserHub-Signature": ",",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"UserHub-Signature header normalized to nothing","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="Timestamp is invalid",
            secret="test",
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                    "UserHub-Timestamp": "timestamp",
                    "UserHub-Signature": "fail",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"Timestamp is invalid: timestamp","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="Timestamp is too far in the past",
            secret="test",
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                    "UserHub-Timestamp": "1",
                    "UserHub-Signature": "fail",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"Timestamp is too far in the past: 1","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="Timestamp is too far in the past",
            secret="test",
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                    "UserHub-Timestamp": "5000000000",
                    "UserHub-Signature": "fail",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"Timestamp is too far in the future: 5000000000","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="Signatures do not match",
            secret="test",
            set_timestamp=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                    "UserHub-Signature": "fail",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=500,
                body=b'{"message":"Signatures do not match","code":"UNKNOWN"}',
            ),
        ),
        WebhookTest(
            name="Challenge",
            secret="test",
            set_timestamp=True,
            add_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "challenge",
                },
                body=b'{"challenge": "some-value"}',
            ),
            response=WebhookResponse(
                status_code=200,
                body=b'{"challenge": "some-value"}',
            ),
        ),
        WebhookTest(
            name="Handle multiple signature headers",
            secret="test",
            set_timestamp=True,
            add_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "challenge",
                    "UserHub-Signature": "fail",
                },
                body=b'{"challenge": "some-value"}',
            ),
            response=WebhookResponse(
                status_code=200,
                body=b'{"challenge": "some-value"}',
            ),
        ),
        WebhookTest(
            name="Handle combined signature headers",
            secret="test",
            set_timestamp=True,
            set_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "challenge",
                    "UserHub-Signature": "fail, {signature}",
                },
                body=b'{"challenge": "some-value"}',
            ),
            response=WebhookResponse(
                status_code=200,
                body=b'{"challenge": "some-value"}',
            ),
        ),
        WebhookTest(
            name="Handler not implemented",
            secret="test",
            set_timestamp=True,
            add_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "unknown",
                },
                body=b"{}",
            ),
            response=WebhookResponse(
                status_code=501,
                body=b'{"message":"Handler not implemented: unknown","code":"UNIMPLEMENTED"}',
            ),
        ),
        WebhookTest(
            name="Event handler succeeds",
            secret="test",
            set_timestamp=True,
            add_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                },
                body=b'{"type": "ok"}',
            ),
            response=WebhookResponse(
                status_code=200,
                body=b"{}",
            ),
        ),
        WebhookTest(
            name="Event handler errors",
            secret="test",
            set_timestamp=True,
            add_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "events.handle",
                },
                body=b'{"type": "fail"}',
            ),
            response=WebhookResponse(
                status_code=400,
                body=b'{"message":"Event failed: fail","code":"INVALID_ARGUMENT"}',
            ),
        ),
        WebhookTest(
            name="List users",
            secret="test",
            set_timestamp=True,
            add_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "users.list",
                },
                body=b'{"pageSize":100}',
            ),
            response=WebhookResponse(
                status_code=200,
                body=b'{"nextPageToken":"","users":[]}',
            ),
        ),
        WebhookTest(
            name="Get user",
            secret="test",
            set_timestamp=True,
            add_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "users.get",
                },
                body=b'{"id": "1"}',
            ),
            response=WebhookResponse(
                status_code=200,
                body=b'{"id":"1","displayName":"","email":"","emailVerified":false,"phoneNumber":"","phoneNumberVerified":false,"imageUrl":"","disabled":false}',
            ),
        ),
        WebhookTest(
            name="Get user not found",
            secret="test",
            set_timestamp=True,
            add_signature=True,
            request=WebhookRequest(
                headers={
                    "UserHub-Action": "users.get",
                },
                body=b'{"id": "not-found"}',
            ),
            response=WebhookResponse(
                status_code=404,
                body=b'{"message":"User not found","code":"NOT_FOUND"}',
            ),
        ),
    ],
    ids=lambda test: test.name.lower().replace(" ", "-"),
)
def test_handler(test: WebhookTest):
    def handle_event(input: Event):
        if input.type != "ok":
            raise UserHubError(
                f"Event failed: {input.type}", api_code=Code.INVALID_ARGUMENT
            )

    def handle_list_users(input: ListCustomUsersRequest) -> ListCustomUsersResponse:
        if input.page_size != 100:
            raise Exception(f"unexpected page size: {input.page_size}")

        return ListCustomUsersResponse(users=[], next_page_token="")

    def handle_get_user(input: GetCustomUserRequest) -> CustomUser:
        if input.id == "not-found":
            raise WebhookUserNotFound

        return CustomUser(
            id=input.id,
            display_name="",
            email="",
            email_verified=False,
            phone_number="",
            phone_number_verified=False,
            image_url="",
            disabled=False,
        )

    webhook = Webhook(test.secret)
    webhook.on_event(handle_event)
    webhook.on_list_users(handle_list_users)
    webhook.on_get_user(handle_get_user)

    req = test.request
    if test.set_timestamp:
        req.headers["UserHub-Timestamp"] = str(int(time.time()))
    if test.set_signature or test.add_signature:
        timestamp = get_header(req, "UserHub-Timestamp")

        h = hmac.new(
            test.secret.encode("utf-8"),
            msg=timestamp.encode("utf-8") + b"." + req.body,
            digestmod=hashlib.sha256,
        )
        signature = h.hexdigest()

        if test.set_signature:
            header = get_header(req, "UserHub-Signature")

            if "{signature}" in header:
                header = header.replace("{signature}", signature)
            else:
                header = signature

            req.headers["UserHub-Signature"] = header
        else:
            add_header(req, "UserHub-Signature", signature)

    res = webhook.handle_action(req)

    assert res.status_code == test.response.status_code, str(res.body or "")

    assert get_header(res, "content-type") == "application/json"
    assert get_header(res, constants.WEBHOOK_AGENT_HEADER) == constants.USER_AGENT

    expected = json.loads(test.response.body) if test.response.body else {}
    actual = json.loads(res.body) if res.body else {}

    assert actual == expected
