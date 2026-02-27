from django.db import models
from .company import Company


class Section(models.Model):
    """ Модель Отдел организации """
    name = models.CharField('Наименование', max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Организация', related_name='sections')
    is_active = models.BooleanField('Активная', default=True)
    
    class Meta:
        db_table = 'section'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        
    def __str__(self):
        return self.name
    