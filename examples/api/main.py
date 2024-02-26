import os

from userhub_sdk import AdminApi, UserApi, UserHubError

admin_key = os.environ.get("ADMIN_KEY")
if not admin_key:
    raise RuntimeError("ADMIN_KEY required")

user_key = os.environ.get("USER_KEY")
if not user_key:
    raise RuntimeError("USER_KEY required")

admin_api = AdminApi(admin_key)

res = admin_api.users.list(page_size=5)

for user in res.users:
    if user.disabled:
        continue

    api_session = admin_api.users.create_api_session(user.id)

    user_api = UserApi(user_key, api_session.access_token)

    session = user_api.session.get()

    print("User:")
    print(" - ID:", session.user.id)
    print(" - Name:", session.user.display_name)
    print(" - Memberships:", len(session.memberships))

    break

try:
    admin_api.users.get("fail")
except UserHubError as ex:
    print()
    print(ex)
    print()
    print("UserHub error:")
    print(" - ApiCode:", ex.api_code)
    print(" - Message:", ex.message)
    print(" - Reason:", ex.reason)
    print(" - Param:", ex.param)
    print(" - Call:", ex.call)
