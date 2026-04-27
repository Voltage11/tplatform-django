from django.db import models
from .base_model import BaseModel


class Answer(BaseModel):
    """ Вариант ответа модель """
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name='answers',
    )
    title = models.CharField('Заголовок', max_length=1000)
    is_correct = models.BooleanField('Верный ответ', default=False)

    class Meta:
        db_table = 'answer'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.title[:50] if len(self.title) > 50 else self.title
