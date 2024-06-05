from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    @staticmethod
    def get_user_or_none_by_username(username):
        try:
            return User.objects.get(username=username)
        except Exception:
            return None

    @staticmethod
    def get_user_or_none_by_email(email):
        try:

            return User.objects.get(email=email)
        except Exception:
            return None