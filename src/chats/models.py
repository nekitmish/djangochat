from django.db import models

from djangochat.models import DefaultModel
from djangochat.models import SoftDeleteMixin


class Chat(DefaultModel, SoftDeleteMixin):
    participants = models.ManyToManyField(
        'users.User',
        blank=False,
        related_name='chats',
    )
