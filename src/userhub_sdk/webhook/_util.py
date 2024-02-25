import logging
from typing import Any

from userhub_sdk._internal import constants, util
from userhub_sdk.types import UserHubError

from ._http import WebhookResponse

logger = logging.getLogger("userhub_sdk.webhooks")


def default_on_error(ex: Exception) -> None:
    if ex:
        logger.error("UserHub webhook: %s", ex)


def create_response(data: Any, /) -> WebhookResponse:
    status_code = 200

    if data is None:
        body = b"{}"
    elif isinstance(data, bytes):
        body = data
    elif isinstance(data, WebhookResponse):
        return data
    elif isinstance(data, Exception):
        if isinstance(data, UserHubError):
            status_code = data.api_code.webhook_status_code
            body = util.encode_json(data)
        else:
            status_code = 500
            body = constants.WEBHOOK_SERVER_ERROR_JSON
    else:
        body = util.encode_json(data)

    return WebhookResponse(
        status_code=status_code,
        headers={
            "Content-Type": "application/json",
            constants.WEBHOOK_AGENT_HEADER: constants.USER_AGENT,
        },
        body=body,
    )
