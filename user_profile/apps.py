from django.apps import AppConfig
from user_profile import signals


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    def ready(self) -> None:
        return signals
