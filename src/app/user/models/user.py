from django.contrib.auth.models import AbstractUser
from django.db import models
from .section import Section



class User(AbstractUser):
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Отдел')
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    def __str__(self):
        return f'{self.first_name} {self.second_name}' | self.username