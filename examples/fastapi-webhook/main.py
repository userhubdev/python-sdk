import os

from fastapi import FastAPI, Request, Response

from userhub_sdk import eventsv1
from userhub_sdk.webhook import AsyncWebhook, WebhookRequest

signing_secret = os.environ.get("SIGNING_SECRET")
if not signing_secret:
    raise RuntimeError("SIGNING_SECRET required")


async def handle_event(event: eventsv1.Event):
    print("Event:", event.type)

    if event.type == "organizations.changed":
        organization = event.organizations_changed.organization
        print(" - Organization:", organization.id, organization.display_name)
    elif event.type == "users.changed":
        user = event.users_changed.user
        print(" - User:", user.id, user.display_name)


webhook = AsyncWebhook(signing_secret)
webhook.on_event(handle_event)


app = FastAPI()


@app.post("/webhook")
async def handle_webhook(req: Request):
    body = await req.body()

    res = await webhook(WebhookRequest(headers=dict(req.headers), body=body))

    return Response(
        status_code=res.status_code,
        headers=res.headers,
        content=res.body,
    )
