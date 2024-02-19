# UserHub Python SDK

Stability: alpha

### Requirements

* Python 3.8 or later

### Getting Started

Install SDK

```sh
pip install -U userhub-sdk
```

Example

```python
from userhub_sdk import AdminApi

admin_api = AdminApi("sk_123...")

res = admin_api.users.list(page_size=5)

for user in res.users:
    print(user.id, user.display_name)
```

See the `examples` directory for more examples.
