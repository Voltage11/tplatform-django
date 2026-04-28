import uuid

from django.db import models
from django.utils import timezone

from django.conf import settings

from .base_model import BaseModel


class ThemeType(models.TextChoices):
    ALL = 'all', 'все отделы'
    CUSTOM = 'custom', 'указанные'
    

class Theme(BaseModel):
    """ Тема для тестирования модель """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('Тема', max_length=150)
    description = models.TextField('Описание', null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        related_name='themes', 
        verbose_name='Автор'
    )    
    points_max = models.PositiveIntegerField('Макс. кол. баллов', default=0)
    points_check = models.PositiveIntegerField('Кол. баллов для зачета', default=0)    
    theme_type = models.CharField(
        'Доступность', 
        max_length=10, 
        choices=ThemeType.choices, 
        default=ThemeType.ALL
    )    
    departments = models.ManyToManyField(
        'user.Department', 
        verbose_name='Доступность для отделов',
        blank=True 
    )
    is_active = models.BooleanField('Доступен для прохождения', default=True)
    date_begin = models.DateField('Досупен с', null=True, blank=True)
    date_end = models.DateField('Досупен до', null=True, blank=True)
    
    class Meta:
        db_table = 'theme' 
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title
    
    def is_available(self) -> bool:
        """Доступность теста по статусу и датам"""
        if not self.is_active:
            return False
        
        now = timezone.now().date()
        
        # Если дата начала установлена и она еще не наступила
        if self.date_begin and self.date_begin > now:
            return False
        
        # Если дата окончания установлена и она уже прошла
        if self.date_end and self.date_end < now:
            return False
        
        return True
    
    def is_available_for_user(self, user: 'User') -> bool:
        """Доступность для конкретного пользователя"""
        if not self.is_available():
            return False
        
        if self.theme_type == ThemeType.ALL:
            return True
        
        # Используем getattr, чтобы не упасть, если у объекта нет department_id
        dept_id = getattr(user, 'department_id', None)
        return self.is_available_for_department(dept_id)
    
    def is_available_for_department(self, department_id: int | None) -> bool:
        if not self.is_available():
            return False
        
        if self.theme_type == ThemeType.ALL:
            return True
        
        if not department_id:
            return False
            
        return self.departments.filter(id=department_id).exists()