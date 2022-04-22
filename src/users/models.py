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

    @classmethod
    def get_default_deleted_user(cls):
        default_deleted_user, created = cls.objects.get_or_create(
            username='deleted',
            defaults=dict(
                email='deleted@user.com',
                first_name='deleted',
                last_nmae='deleted',
            )
        )
        return default_deleted_user

    class Meta:
        ordering = ['-id']
