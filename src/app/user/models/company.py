from django.db import models

from app.core.models import BaseModel


class Company(BaseModel):
    """ Компания """
    name = models.CharField('Наименование', max_length=150)
    is_active = models.BooleanField('Активен', default=True)
    
    class Meta:
        db_table = 'companies'
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        
    def __str__(self):
        return self.name