from django.db import models

from djangochat.models import DefaultModel


class Message(DefaultModel):
    sender = models.ForeignKey(
        'users.User',
        related_name='messages',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )
    body = models.TextField(
        verbose_name='Message body',
        max_length=1000,
        blank=False,
    )
    chat = models.ForeignKey(
        'chats.Chat',
        null=False,
        blank=False,
        related_name='messages',
        on_delete=models.PROTECT,
    )
