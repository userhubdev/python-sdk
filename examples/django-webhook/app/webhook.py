from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from userhub_sdk import eventsv1
from userhub_sdk.webhook import Webhook, WebhookRequest


def handle_event(event: eventsv1.Event):
    print("Event:", event.type)

    if event.type == "organizations.changed":
        organization = event.organizations_changed.organization
        print(" - Organization:", organization.id, organization.display_name)
    elif event.type == "users.changed":
        user = event.users_changed.user
        print(" - User:", user.id, user.display_name)


webhook = Webhook(settings.SIGNING_SECRET)
webhook.on_event(handle_event)


@csrf_exempt
def webhook_view(request):
    res = webhook(WebhookRequest(headers=dict(request.headers), body=request.body))

    return HttpResponse(
        status=res.status_code,
        headers=res.headers,
        content=res.body,
    )
