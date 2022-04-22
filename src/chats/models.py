from django.db import models

from djangochat.models import DefaultModel
from users.models import User


class Chat(DefaultModel):
    me = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=User.get_default_deleted_user,
        related_name='chats_me',
    )
    companion = models.ForeignKey(
        'users.User',
        on_delete=models.SET(User.get_default_deleted_user),
        null=False,
        blank=False,
        related_name='chats_companion',
    )

    is_archived = models.BooleanField(
        default=False,
    )
    is_unread = models.BooleanField(
        default=False,
    )
