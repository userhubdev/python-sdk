from ..types import Code, UserHubError


class WebhookUserNotFound(UserHubError):
    """
    WebhookUserNotFound is an error which can be used to indicate a user was
    not found in the on_get_user, on_update_user, and on_delete_user methods.
    """

    def __init__(self) -> None:
        super().__init__(message="User not found", api_code=Code.NOT_FOUND)
