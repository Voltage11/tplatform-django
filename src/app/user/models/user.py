from django.contrib.auth.models import AbstractUser
from django.db import models

from app.core.models import BaseModel


class User(AbstractUser, BaseModel):
    # Добавляем свои поля
    department = models.ForeignKey(
        'Department', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Отдел"
    )
    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username} ({self.first_name} {self.last_name})'       