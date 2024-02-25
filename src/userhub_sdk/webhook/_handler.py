import json
from typing import Any, Awaitable, Callable, Generic, TypeVar

from userhub_sdk._internal.util import summarize_body
from userhub_sdk.types import Code, UserHubError

from ._http import WebhookRequest, WebhookResponse
from ._util import create_response

InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")
Handler = Callable[[WebhookRequest], WebhookResponse]
AsyncHandler = Callable[[WebhookRequest], Awaitable[WebhookResponse]]


def challenge_handler(req: WebhookRequest) -> WebhookResponse:
    return create_response(req.body)


def unimplemented_handler(req: WebhookRequest) -> WebhookResponse:
    name = req.get_action()
    raise UserHubError(f"Handler not implemented: {name}", api_code=Code.UNIMPLEMENTED)


class DecodeHandler(Generic[InputType, OutputType]):
    def __init__(
        self,
        handler: Callable[[InputType], OutputType],
        decoder: Callable[[Any], InputType],
    ) -> None:
        self._handler = handler
        self._decoder = decoder

    def __call__(self, req: WebhookRequest, /) -> WebhookResponse:
        try:
            handler_input = self._decoder(json.loads(req.body.decode("utf-8")))
        except Exception as ex:
            raise UserHubError(
                f"Failed to decode error request{summarize_body(req.body)}",
            ) from ex

        data = self._handler(handler_input)

        return create_response(data)


class AsyncDecodeHandler(Generic[InputType, OutputType]):
    def __init__(
        self,
        handler: Callable[[InputType], Awaitable[OutputType]],
        decoder: Callable[[Any], InputType],
    ) -> None:
        self._handler = handler
        self._decoder = decoder

    async def __call__(self, req: WebhookRequest, /) -> WebhookResponse:
        try:
            handler_input = self._decoder(json.loads(req.body.decode("utf-8")))
        except Exception as ex:
            raise UserHubError(
                f"Failed to decode error request{summarize_body(req.body)}",
            ) from ex

        data = await self._handler(handler_input)

        return create_response(data)
