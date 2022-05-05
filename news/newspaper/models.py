from secrets import choice
from django.db import models
from matplotlib.pyplot import cla
# Получим таблицу пользователей (модель по умолчанию):
from django.contrib.auth import get_user_model

# Create your models here.
class Comments(models.Model):
  
    DELETE_CHOICES = [
        (True, 'Удалено администратором'),
        (False, '')
    ]

    username = models.CharField(max_length=30, verbose_name='Имя')
    content = models.TextField(verbose_name='Текст')
    delete_status = models.BooleanField(default=False, choices=DELETE_CHOICES,
                                         verbose_name='Статус')

    new = models.ForeignKey('News', on_delete=models.CASCADE, null=True,
                            related_name='news', verbose_name='Новость')
    # один пользователь ко многим комментариям:
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True,
                            related_name='user', verbose_name='Пользователь')

    def __str__(self):
        return f"{self.username}, {self.content[:15]}..."
    
    class Meta:
        db_table = 'Комментарии'


class News(models.Model):

    #Список тьюплов для параметра choices для групповых действий
    ACTIVITY_CHOICES = [
        (True, 'Active'),
        (False, 'Deactive')
    ]

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #параметр choices задаеся для групповых действий
    active = models.BooleanField(default=True, choices=ACTIVITY_CHOICES)

    def __str__(self):
        #через split убираем отображение долей секунды
        return f"{self.title} | {str(self.created_at).split('.')[0]} | Активность: {self.active}"

    class Meta:
        db_table = 'Список новостей'
        #Отсортируем по дате публикации: сначала свежие.
        #для сортировки в обратном порядке указываем "-" перед параметром:
        ordering = ['-created_at']
