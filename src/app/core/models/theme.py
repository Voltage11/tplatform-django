import uuid

from django.db import models
from django.utils import timezone

from app.core.models import BaseModel
from config.settings import AUTH_USER_MODEL


class Theme(BaseModel):
    """ Тема тестирования """
    name = models.CharField('Наименование', max_length=150)
    comment = models.TextField('Комментарий', null=True, blank=True)
    slug = models.UUIDField('Идентификатор', default=uuid.uuid4, editable=False, unique=True, db_index=True, help_text='Идентификатор темы')
    is_active = models.BooleanField('Активна', default=True)
    date_from = models.DateField('Дата начала', null=True, blank=True)
    date_to = models.DateField('Дата окончания', null=True, blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.PROTECT, related_name='themes')
    
    class Meta:
        db_table = 'themes'
        verbose_name = 'Тема тестирования'
        verbose_name_plural = 'Темы тестирования'
        
    def __str__(self):
        return self.name
    
    def ia_available(self) -> bool:
        """ Доступен для прохождения """
        return (
            self.is_active and 
            (self.date_from is None or self.date_from <= timezone.now()) and 
            (self.date_to is None or self.date_to >= timezone.now())
        )
        
    