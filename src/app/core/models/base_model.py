from django.db import models
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        # По умолчанию возвращаем только те записи, где deleted_at IS NULL
        return super().get_queryset().filter(deleted_at__isnull=True)


class BaseModel(models.Model):
    """ Базовая модель """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Стандартный менеджер (будет фильтровать удаленные)
    objects = SoftDeleteManager()
    # Менеджер для доступа ко ВСЕМ записям (включая удаленные)
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """Мягкое удаление: вместо удаления ставим метку времени"""
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        """Для полного удаления из базы, если это всё же нужно"""
        super().delete()

    def restore(self):
        """Метод для восстановления записи"""
        self.deleted_at = None
        self.save()
