from django.db import models

from djangochat.models import DefaultModel
from users.models import User


class Message(DefaultModel):
    sender = models.ForeignKey(
        'users.User',
        related_name='sent_messages',
        on_delete=models.SET(User.get_default_deleted_user),
        null=False,
        blank=False,
    )
    sender_chat = models.ForeignKey(
        'chats.Chat',
        related_name='sent_messages',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    recipient = models.ForeignKey(
        'users.User',
        related_name='received_messages',
        on_delete=models.SET(User.get_default_deleted_user),
        null=False,
        blank=False,
    )
    recipient_chat = models.ForeignKey(
        'chats.Chat',
        related_name='received_messages',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    body = models.TextField(
        verbose_name='Message body',
        max_length=1000,
        blank=False,
    )
