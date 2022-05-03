from django.db import models
from matplotlib.pyplot import cla

# Create your models here.
class Comments(models.Model):

    username = models.CharField(max_length=30, verbose_name='Имя')
    content = models.TextField(verbose_name='Текст')

    new = models.ForeignKey('News', on_delete=models.CASCADE, null=True,
                            related_name='news', verbose_name='Новость')

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'Комментарии'


class News(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Список новостей'
        #Отсортируем по дате публикации: сначала свежие.
        #для сортировки в обратном порядке указываем "-" перед параметром:
        ordering = ['-created_at']
