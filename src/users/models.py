from django.contrib.auth.models import AbstractUser
from django.db import models
from djangochat.models import DefaultModel
from djangochat.models import SoftDeleteMixin


class User(AbstractUser, DefaultModel, SoftDeleteMixin):
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        db_index=True,
    )
    bio = models.CharField(
        max_length=150,
        verbose_name='Bio',
        blank=True
    )

    class Meta:
        ordering = ['-id']
