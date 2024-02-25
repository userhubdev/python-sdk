import dataclasses
from typing import Dict, List, Optional, Union

from userhub_sdk._internal import constants
from userhub_sdk.types import UserHubError


@dataclasses.dataclass
class WebhookRequest:
    headers: Dict[str, Union[str, List[str]]] = dataclasses.field(default_factory=dict)
    body: bytes = b""

    def get_action(self) -> str:
        name = get_header(self, constants.WEBHOOK_ACTION_HEADER)
        if not name:
            raise UserHubError(f"{constants.WEBHOOK_ACTION_HEADER} header is missing")
        return name

    def get_timestamp(self) -> str:
        timestamp = get_header(self, constants.WEBHOOK_TIMESTAMP_HEADER)
        if not timestamp:
            raise UserHubError(
                f"{constants.WEBHOOK_TIMESTAMP_HEADER} header is missing"
            )

        return timestamp

    def get_signatures(self) -> List[str]:
        signatures = []

        headers = get_headers(self, constants.WEBHOOK_SIGNATURE_HEADER)

        if not headers:
            raise UserHubError(
                f"{constants.WEBHOOK_SIGNATURE_HEADER} header is missing"
            )

        for raw_header in headers:
            header = raw_header.strip()
            if not header:
                continue

            if "," not in header:
                signatures.append(header)

            header_parts = header.split(",")

            for raw_signature in header_parts:
                signature = raw_signature.strip()
                if signature:
                    signatures.append(signature)

        if not signatures:
            raise UserHubError(
                f"{constants.WEBHOOK_SIGNATURE_HEADER} header normalized to nothing"
            )

        return signatures


@dataclasses.dataclass
class WebhookResponse:
    status_code: int = 200
    headers: Dict[str, str] = dataclasses.field(default_factory=dict)
    body: bytes = b""


def get_header(r: Union[WebhookRequest, WebhookResponse], name: str) -> Optional[str]:
    headers = get_headers(r, name)
    return headers[0] if headers else None


def get_headers(
    r: Union[WebhookRequest, WebhookResponse], name: str
) -> Optional[List[str]]:
    name = name.lower()

    for n, v in r.headers.items():
        if n.lower() == name:
            return v if isinstance(v, list) else [v]

    return []


def add_header(r: WebhookRequest, name: str, value: str) -> None:
    name = name.lower()

    for n, v in r.headers.items():
        if n.lower() == name:
            if isinstance(v, list):
                v.append(value)
            else:
                r.headers[n] = [v, value]
            return

    r.headers[name] = value
