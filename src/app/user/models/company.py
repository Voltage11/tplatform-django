from django.db import models


class Company(models.Model):
    """ Модель Организация """
    
    name = models.CharField('Наименование', max_length=150)
    is_active = models.BooleanField('Активная', default=True)
    
    class Meta:
        db_table = 'company'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        
    def __str__(self):
        return self.name