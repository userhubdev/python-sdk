import datetime
import json
import sys
import urllib.parse
from typing import Optional, Union

from . import constants


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if obj is not None:
            if isinstance(obj, datetime.datetime):
                obj = encode_datetime(obj)
            elif hasattr(obj, "__json_encode__"):
                obj = obj.__encode_json__()
        return json.JSONEncoder.default(self, obj)


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

    if type(value) is int:
        return value

    return int(value)


def quote_path(value: str) -> str:
    return urllib.parse.quote(value, safe=constants.QUOTE_PATH_SAFE)
