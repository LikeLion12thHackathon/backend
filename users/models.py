from django.db import models
from django.contrib.auth.models import AbstractUser


class GenderChoices(models.TextChoices):
    MALE = ("male", "Male")
    FEMALE = ("female", "Female")


class User(AbstractUser):
    """사용자 모델"""

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )

    avatar = models.URLField(
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices,
        default="",
    )

    is_admin = models.BooleanField(
        default=False,
    )
