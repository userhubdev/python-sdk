import datetime
import enum
import json
import re
import urllib.parse
from typing import Any, Optional, Union

from . import constants

_WHITESPACE_RE = re.compile(r"\s+", re.MULTILINE)


def encode(obj: Any) -> Any:
    if obj is not None:
        if hasattr(obj, "__json_encode__"):
            obj = obj.__json_encode__()
        elif isinstance(obj, dict):
            obj = {k: encode(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            obj = [encode(v) for v in obj]
        elif isinstance(obj, datetime.datetime):
            obj = encode_datetime(obj)
        elif isinstance(obj, enum.Enum):
            obj = obj.value
    return obj


def encode_json(obj: Any) -> bytes:
    return json.dumps(encode(obj)).encode("utf-8")


def decode_datetime(value: Optional[str]) -> Optional[datetime.datetime]:
    if not value:
        return None

    if value.endswith("Z"):
        value = value[:-1]
    elif "+" in value:
        value, _, _ = value.rpartition("+")

    # manually parse fractional seconds for older versions of Python
    if constants.ISOFORMAT_FALLBACK and "." in value:
        value, _, frac = value.rpartition(".")
    else:
        frac = None

    dt = datetime.datetime.fromisoformat(value + constants.ISOFORMAT_SUFFIX)
    if frac:
        dt += datetime.timedelta(seconds=float("." + frac))

    return dt


def encode_datetime(dt: Optional[datetime.datetime]) -> Optional[str]:
    if dt is None:
        return dt

    value = dt.astimezone(datetime.timezone.utc).isoformat()

    if value.endswith(constants.ISOFORMAT_SUFFIX):
        value = value[: -len(constants.ISOFORMAT_SUFFIX)] + "Z"

    return value


def decode_int64(value: Union[int, str, None]) -> Optional[int]:
    if value is None or value == "":
        return None

    if isinstance(value, int):
        return value

    return int(value)


def encode_int64(value: Union[int, None]) -> Optional[str]:
    if value is None:
        return None

    return str(value)


def quote_path(value: str) -> str:
    return urllib.parse.quote(value, safe=constants.QUOTE_PATH_SAFE)


def summarize_body(body: Optional[Union[bytes, str]]) -> str:
    if not body:
        return ""
    if isinstance(body, bytes):
        body = body.decode("utf-8")
    body = _WHITESPACE_RE.sub(" ", body[: constants.SUMMARIZE_BODY_LENGTH * 2]).strip()
    if not body:
        return ""
    if len(body) <= constants.SUMMARIZE_BODY_LENGTH:
        return f": {body}"
    return f": {body[:constants.SUMMARIZE_BODY_LENGTH]}..."
