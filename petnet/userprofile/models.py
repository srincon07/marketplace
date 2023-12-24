from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    is_vendor = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, related_name="userprofile", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.user.username
