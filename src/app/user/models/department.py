from django.db import models
from app.core.models import BaseModel


class Department(BaseModel):
    """ Модель Отдел """
    name = models.CharField('Наименование', max_length=100)
    
    class Meta:
        db_table = 'department'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        
    def __str__(self):
        return self.name