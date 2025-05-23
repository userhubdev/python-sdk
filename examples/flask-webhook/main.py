import os

from flask import Flask, Response, request

from userhub_sdk import eventsv1
from userhub_sdk.webhook import Webhook

signing_secret = os.environ.get("USERHUB_SIGNING_SECRET")
if not signing_secret:
    raise RuntimeError("USERHUB_SIGNING_SECRET required")


def handle_event(event: eventsv1.Event):
    print("Event:", event.type)

    if event.type == "organizations.changed":
        organization = event.organizations_changed.organization
        print(" - Organization:", organization.id, organization.display_name)
    elif event.type == "users.changed":
        user = event.users_changed.user
        print(" - User:", user.id, user.display_name)


webhook = Webhook(signing_secret)
webhook.on_event(handle_event)


app = Flask("flask-webhook")


@app.post("/webhook")
def handle_webhook():
    res = webhook(headers=dict(request.headers), body=request.get_data())
    return Response(res.body, status=res.status_code, headers=res.headers)
