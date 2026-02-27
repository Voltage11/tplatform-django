from django.contrib.auth.models import AbstractUser
from django.db import models
from .section import Section
from .company import Company



class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True, 
                                verbose_name='Организация', related_name='companies')
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, blank=True, null=True, 
                                verbose_name='Отдел', related_name='sections')
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    def __str__(self):
        return f'{self.first_name}' or self.username