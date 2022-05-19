from secrets import choice
from django.db import models
# Получим таблицу пользователей (модель по умолчанию):
from django.contrib.auth.models import User

# Create your models here.


class Tags(models.Model):

    title = models.CharField(max_length=20, verbose_name='Тег', default='Другое')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Новостные теги'


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
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
    #теги для фильтрации:
    tag = models.ForeignKey(Tags, on_delete=models.SET_DEFAULT, null=True, default='Другое',
                            related_name='tag', verbose_name='Тег')
    #параметр choices задаеся для групповых действий
    active = models.BooleanField(default=False, choices=ACTIVITY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                related_name='author', verbose_name='Автор')

    def __str__(self):
        #через split убираем отображение долей секунды
        return f"{self.title} | {str(self.created_at).split('.')[0]} | Активность: {self.active}"

    class Meta:
        db_table = 'Список новостей'
        #Отсортируем по дате публикации: сначала свежие.
        #для сортировки в обратном порядке указываем "-" перед параметром:
        ordering = ['-created_at']

        permissions = (
            ('can_activate', 'Can activate news'),
        )

