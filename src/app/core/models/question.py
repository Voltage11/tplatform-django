from django.db import models

from .base_model import BaseModel


class QuestionType(models.TextChoices):
    ONE = 'one', 'один вариант ответа'
    MULTI = 'multi', 'несколько вариантов ответа'


class Question(BaseModel):
    """ Вопрос модель """
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name='questions', verbose_name='Тема')
    title = models.CharField('Заголовок', max_length=1000)
    question_type = models.CharField(
        'Тип вопроса', 
        max_length=10, 
        choices=QuestionType.choices, 
        default=QuestionType.ONE
    )
    points_check = models.PositiveIntegerField('Баллы за правильный ответ', default=1)
    
    class Meta:
        db_table = 'question'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        
    def __str__(self):
        return self.title[:50] + '...' if len(self.title) > 50 else self.title
            
    