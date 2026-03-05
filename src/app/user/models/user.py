from django.contrib.auth.models import AbstractUser
from django.db import models

from .company import Company
from .section import Section


class User(AbstractUser):
    """ Пользователи """
    company = models.ForeignKey(Company, verbose_name='Компания', on_delete=models.SET_NULL, null=True, blank=True)
    section = models.ForeignKey(Section, verbose_name='Отдел', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    def __str__(self):
        return self.name