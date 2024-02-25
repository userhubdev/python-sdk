import datetime
import hashlib
import hmac
from contextlib import suppress
from typing import Any, Callable, Dict, Generic, Optional, TypeVar

from .._internal import constants
from ..types import UserHubError
from ._http import WebhookRequest, WebhookResponse
from ._util import create_response, default_on_error

T = TypeVar("T")
OnError = Callable[[Exception], None]


class BaseWebhook(Generic[T]):
    _handlers: Dict[str, T]
    _signing_secret: bytes
    _on_error: Optional[OnError]

    def __init__(
        self,
        signing_secret: str,
        /,
        *,
        on_error: Optional[OnError] = default_on_error,
    ):
        self._signing_secret = signing_secret.encode("utf-8")
        self._handlers = {}
        self._on_error = on_error

    def on_action(self, name: str, handler: Optional[T], /) -> "BaseWebhook[T]":
        if handler is None:
            self._handlers.pop(name, None)
        else:
            self._handlers[name] = handler
        return self

    def verify(self, req: WebhookRequest, /) -> None:
        """
        Ensures the body matches the specified signature/timestamp and throws
        an error if verification fails.
        """
        if not self._signing_secret:
            raise UserHubError("Signing secret is required")
        if not req:
            raise UserHubError("Request is required")
        if not req.headers:
            raise UserHubError("Headers are required")
        if not req.body:
            raise UserHubError("Body is required")
        if not isinstance(req.body, bytes):
            raise UserHubError(f"Body has type {type(req.body)}, expected bytes")

        _ = req.get_action()
        timestamp = req.get_timestamp()
        signatures = req.get_signatures()

        try:
            dt = datetime.datetime.fromtimestamp(
                int(timestamp), tz=datetime.timezone.utc
            )
        except Exception as ex:
            raise UserHubError(f"Timestamp is invalid: {timestamp}") from ex

        diff = datetime.datetime.now(datetime.timezone.utc) - dt
        if diff > constants.WEBHOOK_MAX_TIMESTAMP_DIFF:
            raise UserHubError(f"Timestamp is too far in the past: {timestamp}")
        if diff < -constants.WEBHOOK_MAX_TIMESTAMP_DIFF:
            raise UserHubError(f"Timestamp is too far in the future: {timestamp}")

        h = hmac.new(
            self._signing_secret,
            msg=timestamp.encode("utf-8") + b"." + req.body,
            digestmod=hashlib.sha256,
        )
        digest = h.hexdigest()

        matched = False

        for signature in signatures:
            if hmac.compare_digest(digest, signature):
                matched = True
                break

        if not matched:
            raise UserHubError("Signatures do not match")

    def create_response(self, data: Any, /) -> WebhookResponse:
        """
        Creates a response from an object that can be encoded
        using json.dumps or an Exception.
        """
        if self._on_error is not None:
            with suppress(Exception):
                self._on_error(data)

        return create_response(data)
