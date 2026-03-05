from django.db import models

from app.core.models import BaseModel


class Section(BaseModel):
    """ Отдел """
    name = models.CharField('Наименование', max_length=150)
    is_active = models.BooleanField('Активен', default=True)
    
    class Meta:
        db_table = 'sections'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        
    def __str__(self):
        return self.name