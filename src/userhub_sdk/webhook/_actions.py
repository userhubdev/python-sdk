# Code generated. DO NOT EDIT.

from typing import Awaitable, Callable, Dict, List, NoReturn, Optional, Union

from userhub_sdk import connectionsv1, eventsv1

from ._base import BaseWebhook
from ._handler import (
    AsyncDecodeHandler,
    AsyncHandler,
    DecodeHandler,
    Handler,
    challenge_handler,
    unimplemented_handler,
)
from ._http import WebhookRequest, WebhookResponse


class Webhook(BaseWebhook[Handler]):
    """
    Webhook is a parsing and dispatch helper for UserHub webhooks.
    """

    def handle_action(self, req: WebhookRequest, /) -> WebhookResponse:
        """
        Executes a handler based on specified WebhookRequest.
        """
        try:
            self.verify(req)

            action = req.get_action()

            handler = self._handlers.get(action)
            if handler is None:
                if action == "challenge":
                    return challenge_handler(req)

                handler = self._handlers.get("")

            if handler is None:
                return unimplemented_handler(req)

            return handler(req)
        except Exception as ex:
            return self.create_response(ex)

    def __call__(
        self,
        *,
        headers: Optional[Dict[str, Union[str, List[str]]]] = None,
        body: Optional[Union[str, bytes]] = None,
    ) -> WebhookResponse:
        """
        Executes a handler based on specified headers/body.
        """
        if not body:
            body = b""
        elif isinstance(body, str):
            body = body.encode("utf-8")

        if not headers:
            headers = {}

        return self.handle_action(WebhookRequest(headers=headers, body=body))

    def on_action(self, name: str, handler: Optional[Handler], /) -> "Webhook":
        """
        Registers a handler for the specified action.
        """
        super().on_action(name, handler)
        return self

    def on_default(self, handler: Optional[Handler], /) -> "Webhook":
        """
        Registers a fallback action handler.
        """
        return self.on_action("", handler)

    def on_challenge(
        self,
        handler: Optional[Callable[[connectionsv1.Challenge], connectionsv1.Challenge]],
        /,
    ) -> "Webhook":
        """
        Registers a handler for the `challenge` action.
        """
        if handler is not None:
            return self.on_action(
                "challenge",
                DecodeHandler(handler, connectionsv1.Challenge.__json_decode__),
            )

        return self.on_action("challenge", None)

    def on_event(
        self, handler: Optional[Callable[[eventsv1.Event], NoReturn]], /
    ) -> "Webhook":
        """
        Registers a handler for the `events.handle` action.
        """
        if handler is not None:
            return self.on_action(
                "events.handle", DecodeHandler(handler, eventsv1.Event.__json_decode__)
            )

        return self.on_action("events.handle", None)

    def on_list_users(
        self,
        handler: Optional[
            Callable[
                [connectionsv1.ListCustomUsersRequest],
                connectionsv1.ListCustomUsersResponse,
            ]
        ],
        /,
    ) -> "Webhook":
        """
        Registers a handler for the `users.list` action.
        """
        if handler is not None:
            return self.on_action(
                "users.list",
                DecodeHandler(
                    handler, connectionsv1.ListCustomUsersRequest.__json_decode__
                ),
            )

        return self.on_action("users.list", None)

    def on_create_user(
        self,
        handler: Optional[
            Callable[[connectionsv1.CustomUser], connectionsv1.CustomUser]
        ],
        /,
    ) -> "Webhook":
        """
        Registers a handler for the `users.create` action.
        """
        if handler is not None:
            return self.on_action(
                "users.create",
                DecodeHandler(handler, connectionsv1.CustomUser.__json_decode__),
            )

        return self.on_action("users.create", None)

    def on_get_user(
        self,
        handler: Optional[
            Callable[[connectionsv1.GetCustomUserRequest], connectionsv1.CustomUser]
        ],
        /,
    ) -> "Webhook":
        """
        Registers a handler for the `users.get` action.
        """
        if handler is not None:
            return self.on_action(
                "users.get",
                DecodeHandler(
                    handler, connectionsv1.GetCustomUserRequest.__json_decode__
                ),
            )

        return self.on_action("users.get", None)

    def on_update_user(
        self,
        handler: Optional[
            Callable[[connectionsv1.CustomUser], connectionsv1.CustomUser]
        ],
        /,
    ) -> "Webhook":
        """
        Registers a handler for the `users.update` action.
        """
        if handler is not None:
            return self.on_action(
                "users.update",
                DecodeHandler(handler, connectionsv1.CustomUser.__json_decode__),
            )

        return self.on_action("users.update", None)

    def on_delete_user(
        self,
        handler: Optional[Callable[[connectionsv1.DeleteCustomUserRequest], NoReturn]],
        /,
    ) -> "Webhook":
        """
        Registers a handler for the `users.delete` action.
        """
        if handler is not None:
            return self.on_action(
                "users.delete",
                DecodeHandler(
                    handler, connectionsv1.DeleteCustomUserRequest.__json_decode__
                ),
            )

        return self.on_action("users.delete", None)


class AsyncWebhook(BaseWebhook[AsyncHandler]):
    """
    AsyncWebhook is a parsing and dispatch helper for UserHub webhooks.
    """

    async def handle_action(self, req: WebhookRequest, /) -> WebhookResponse:
        """
        Executes a handler based on specified WebhookRequest.
        """
        try:
            self.verify(req)

            action = req.get_action()

            handler = self._handlers.get(action)
            if handler is None:
                if action == "challenge":
                    return challenge_handler(req)

                handler = self._handlers.get("")

            if handler is None:
                return unimplemented_handler(req)

            return await handler(req)
        except Exception as ex:
            return self.create_response(ex)

    async def __call__(
        self,
        *,
        headers: Optional[Dict[str, Union[str, List[str]]]] = None,
        body: Optional[Union[str, bytes]] = None,
    ) -> WebhookResponse:
        """
        Executes a handler based on specified headers/body.
        """
        if not body:
            body = b""
        elif isinstance(body, str):
            body = body.encode("utf-8")

        if not headers:
            headers = {}

        return await self.handle_action(WebhookRequest(headers=headers, body=body))

    def on_action(
        self, name: str, handler: Optional[AsyncHandler], /
    ) -> "AsyncWebhook":
        """
        Registers a handler for the specified action.
        """
        super().on_action(name, handler)
        return self

    def on_default(self, handler: Optional[AsyncHandler], /) -> "AsyncWebhook":
        """
        Registers a fallback action handler.
        """
        return self.on_action("", handler)

    def on_challenge(
        self,
        handler: Optional[
            Callable[[connectionsv1.Challenge], Awaitable[connectionsv1.Challenge]]
        ],
        /,
    ) -> "AsyncWebhook":
        """
        Registers a handler for the `challenge` action.
        """
        if handler is not None:
            return self.on_action(
                "challenge",
                AsyncDecodeHandler(handler, connectionsv1.Challenge.__json_decode__),
            )

        return self.on_action("challenge", None)

    def on_event(
        self, handler: Optional[Callable[[eventsv1.Event], Awaitable[NoReturn]]], /
    ) -> "AsyncWebhook":
        """
        Registers a handler for the `events.handle` action.
        """
        if handler is not None:
            return self.on_action(
                "events.handle",
                AsyncDecodeHandler(handler, eventsv1.Event.__json_decode__),
            )

        return self.on_action("events.handle", None)

    def on_list_users(
        self,
        handler: Optional[
            Callable[
                [connectionsv1.ListCustomUsersRequest],
                Awaitable[connectionsv1.ListCustomUsersResponse],
            ]
        ],
        /,
    ) -> "AsyncWebhook":
        """
        Registers a handler for the `users.list` action.
        """
        if handler is not None:
            return self.on_action(
                "users.list",
                AsyncDecodeHandler(
                    handler, connectionsv1.ListCustomUsersRequest.__json_decode__
                ),
            )

        return self.on_action("users.list", None)

    def on_create_user(
        self,
        handler: Optional[
            Callable[[connectionsv1.CustomUser], Awaitable[connectionsv1.CustomUser]]
        ],
        /,
    ) -> "AsyncWebhook":
        """
        Registers a handler for the `users.create` action.
        """
        if handler is not None:
            return self.on_action(
                "users.create",
                AsyncDecodeHandler(handler, connectionsv1.CustomUser.__json_decode__),
            )

        return self.on_action("users.create", None)

    def on_get_user(
        self,
        handler: Optional[
            Callable[
                [connectionsv1.GetCustomUserRequest],
                Awaitable[connectionsv1.CustomUser],
            ]
        ],
        /,
    ) -> "AsyncWebhook":
        """
        Registers a handler for the `users.get` action.
        """
        if handler is not None:
            return self.on_action(
                "users.get",
                AsyncDecodeHandler(
                    handler, connectionsv1.GetCustomUserRequest.__json_decode__
                ),
            )

        return self.on_action("users.get", None)

    def on_update_user(
        self,
        handler: Optional[
            Callable[[connectionsv1.CustomUser], Awaitable[connectionsv1.CustomUser]]
        ],
        /,
    ) -> "AsyncWebhook":
        """
        Registers a handler for the `users.update` action.
        """
        if handler is not None:
            return self.on_action(
                "users.update",
                AsyncDecodeHandler(handler, connectionsv1.CustomUser.__json_decode__),
            )

        return self.on_action("users.update", None)

    def on_delete_user(
        self,
        handler: Optional[
            Callable[[connectionsv1.DeleteCustomUserRequest], Awaitable[NoReturn]]
        ],
        /,
    ) -> "AsyncWebhook":
        """
        Registers a handler for the `users.delete` action.
        """
        if handler is not None:
            return self.on_action(
                "users.delete",
                AsyncDecodeHandler(
                    handler, connectionsv1.DeleteCustomUserRequest.__json_decode__
                ),
            )

        return self.on_action("users.delete", None)
