# UserHub Python SDK

Stability: alpha

## Usage

```python
from userhub_sdk import AdminApi

admin_api = AdminApi("sk_123...")

res = admin_api.users.list(page_size=5)

for user in res.users:
    print(user.id, user.display_name)
```
