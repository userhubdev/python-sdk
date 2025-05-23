# UserHub Python SDK
[![PyPI Latest Version](https://img.shields.io/pypi/v/userhub_sdk?color=0173b4)](https://pypi.org/project/userhub-sdk/)

The official [UserHub](https://userhub.com) Python SDK.

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

admin_api = AdminApi("userhub_admin_123...")

res = admin_api.users.list(page_size=5)

for user in res.users:
    print(user.id, user.display_name)
```

See the `examples` directory for more examples.
