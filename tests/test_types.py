from userhub_sdk import (
    Code,
    UserHubError,
)
from userhub_sdk._internal import util


def test_code():
    assert Code.OK == "OK"
    assert Code.CANCELED == Code.CANCELED
    assert Code.CANCELED == "CANCELLED"
    assert Code.OK.webhook_status_code == 200
    assert Code.NOT_FOUND.webhook_status_code == 404


def test_error():
    error = UserHubError()
    assert util.encode_json(error) == b'{"message": "<no message>", "code": "UNKNOWN"}'

    error2 = error.clone(message="Canceled", api_code=Code.CANCELED)
    assert util.encode_json(error2) == b'{"message": "Canceled", "code": "CANCELLED"}'

    assert error.message != error2.message
