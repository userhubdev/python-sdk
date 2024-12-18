import os
from contextlib import suppress
from http.server import BaseHTTPRequestHandler, HTTPServer

from userhub_sdk import eventsv1
from userhub_sdk.webhook import Webhook

port = int(os.environ.get("PORT") or "8000")

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


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_POST(self):
        res = webhook(
            headers=dict(self.headers),
            body=self.rfile.read(int(self.headers.get("Content-Length"))),
        )

        self.send_response(res.status_code)

        for name, value in res.headers.items():
            self.send_header(name, value)

        self.send_header("Content-Length", str(len(res.body)))
        self.end_headers()
        self.wfile.write(res.body)


print(f"Listening on http://127.0.0.1:{port}")


server = HTTPServer(("", port), Handler)
with suppress(KeyboardInterrupt):
    server.serve_forever()
