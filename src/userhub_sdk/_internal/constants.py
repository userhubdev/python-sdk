# Code generated. DO NOT EDIT.

import datetime
import sys

API_BASE_URL = "https://api.userhub.com"
API_VERSION = "2022-11-15"
USER_AGENT = "UserHub-Python/0.7.0"
VERSION = "0.7.0"

AUTH_HEADER = "Authorization"
API_KEY_HEADER = "UserHub-Api-Key"
API_VERSION_HEADER = "UserHub-Api-Version"

WEBHOOK_ACTION_HEADER = "UserHub-Action"
WEBHOOK_AGENT_HEADER = "Webhook-Agent"
WEBHOOK_MAX_REQUEST_SIZE_BYTES = 5242880
WEBHOOK_MAX_TIMESTAMP_DIFF = datetime.timedelta(milliseconds=300000)
WEBHOOK_SIGNATURE_HEADER = "UserHub-Signature"
WEBHOOK_TIMESTAMP_HEADER = "UserHub-Timestamp"
WEBHOOK_SERVER_ERROR_JSON = b"""{"message":"Webhook server error","code":"INTERNAL"}"""

SUMMARIZE_BODY_LENGTH = 20

CONNECT_TIMEOUT = datetime.timedelta(milliseconds=30000)
CONNECTION_IDLE_TIMEOUT = datetime.timedelta(milliseconds=30000)
MAX_BODY_SIZE_BYTES = 5242880
MAX_CONNECTIONS = 100
MAX_IDLE_CONNECTIONS = 5
READ_TIMEOUT = datetime.timedelta(milliseconds=30000)
REQUEST_TIMEOUT = datetime.timedelta(milliseconds=60000)
RETRY_MAX_ATTEMPTS = 5
RETRY_MAX_SLEEP = datetime.timedelta(milliseconds=20000)
RETRY_MULTIPLIER = datetime.timedelta(milliseconds=100)
RETRY_OVERHEAD = datetime.timedelta(milliseconds=100)
TLS_TIMEOUT = datetime.timedelta(milliseconds=10000)
WRITE_TIMEOUT = datetime.timedelta(milliseconds=30000)

EMPTY_DATETIME = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
ISOFORMAT_SUFFIX = "+00:00"
ISOFORMAT_FALLBACK = sys.version_info < (3, 11, 0)
QUOTE_PATH_SAFE = "-._~!$&'()*+,;=:@'"
