from django.db import models


class DefaultModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True,
    )

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(
        verbose_name='Удален',
        default=False,
    )
    deleted_at = models.DateTimeField(
        verbose_name='Когда удалён',
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
