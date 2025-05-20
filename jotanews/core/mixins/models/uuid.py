from django.db import models
import uuid


class UUIDMixin:
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    class Meta:
        abstract = True
