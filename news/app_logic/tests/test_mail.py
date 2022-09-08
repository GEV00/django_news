from urllib import response
from django.shortcuts import reverse
from django.test import TestCase
from django.contrib.auth.models import User
#from sympy import im
#from app_logic.views import reset_password

USER_EMAIL = 'test@mail.ru'
OLD_PASSWORD = '123123'

class TestResetPassword(TestCase):

    def test_reset_password_url_exist_right_location(self): # проверка url
        response = self.client.get('/send_email/')
        self.assertEqual(response.status_code, 200)

    def test_reset_password_correct_template(self):
        response = self.client.get(reverse('reset_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_logic/send_email.html')

    def test_reset_password_post(self):
        '''Хотим проверить правильность выполнения post
        запроса и заполнение формы.
        Создаем тут одного тестового пользователя и сверяем его почту
        с той, что ввели в форму'''
        user = User.objects.create(
            username='test_user',
            email=USER_EMAIL
        )
        user.save()
        response = self.client.post(reverse('reset_password'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 200) # проверяем отвечает ли post запрос
        from django.core.mail import outbox # список для тестовых писем. Создается при тесте
        self.assertEqual(len(outbox), 1) # число элементов в списке = числу писем. Отправили одно, => проверяем, одно ли письмо в outbox
        self.assertIn(USER_EMAIL, outbox[0].to) # проверяет лежит ли USER_EMAIL, переданный post запросом, в outbox

    def test_reset_password_password_was_changed(self):
        '''Создадим пользователя с некоторым паролем, сделаем пост запрос
        на страницу смены пароля, обновим пароль пользователя и сравним со
        старым'''
        user = User.objects.create(
            username='test_user',
            email=USER_EMAIL
        )   # создали юзера, пока без пароля     
        user.set_password(OLD_PASSWORD)  # добавили пароль
        user.save() # сохранили в тестовую БД
        old_password_hash = user.password # не сохранем OLD_PASSWORD, потому что пароли в БД хранятся хешированными. Хеши и сравним
        response = self.client.post(reverse('reset_password'), {'mail_to': USER_EMAIL})
        self.assertEqual(response.status_code, 200) # проверим на всякий соединение
        # тут срабатывает логика и пароль меняется. Обновим его в БД
        user.refresh_from_db() # теперь в БД тот же юзер, но с другим паролем
        self.assertNotEqual(old_password_hash, user.password) # сравниваем пароли, должны быть разными
