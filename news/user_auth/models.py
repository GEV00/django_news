from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    VERIFY_CHOICES = [
        (True, 'Верифицирован'),
        (False, 'Не верифицирован')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона', blank=True)
    is_verify = models.BooleanField(default=False, verbose_name='Верификация',
                                    choices=VERIFY_CHOICES)
    num_of_news = models.IntegerField(default=0, verbose_name='Чисто опубликованных новостей')

    class Meta:
        db_table = 'Информация о пользователе'
        permissions = (
            ('can_verify', 'Может верифицировать'),
        )