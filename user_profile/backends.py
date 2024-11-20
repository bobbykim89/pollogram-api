from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.http import HttpRequest


class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None = None, password: str | None = None, **kwargs: Any) -> AbstractBaseUser | None:
        if username is None:
            username = kwargs.get('email')
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None
