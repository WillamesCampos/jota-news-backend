from django.db import models
from core.mixins.models.uuid import UUIDMixin


class AuditableMixin(UUIDMixin):

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    created_by_id = models.IntegerField(
        blank=True,
        null=True,
        editable=False
    )
    updated_by_id = models.IntegerField(
        blank=True,
        null=True,
        editable=False
    )

    class Meta:
        abstract = True
