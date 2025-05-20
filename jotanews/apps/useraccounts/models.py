
from core.mixins.models.audit import AuditableMixin
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAccount(AbstractUser, AuditableMixin):

    class Profile(models.TextChoices):
        ADMIN = 'admin'
        EDITOR = 'editor'
        READER = 'reader'

    profile = models.CharField(
        max_length='3',
        choices=Profile,
        default=Profile.READER
    )


# Create your models here.
