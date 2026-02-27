from django.db import models

from .company import Company


class Section(models.Model):
    """ Модель Отдел организации """
    name = models.CharField('Наименование', max_length=150)
    is_active = models.BooleanField('Активная', default=True)
    
    class Meta:
        db_table = 'section'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        
    def __str__(self):
        return self.name
        