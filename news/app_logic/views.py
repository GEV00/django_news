from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailSendForm
from news import settings
from django.contrib.auth.models import User


def reset_password(request):
    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            mail_to = form.cleaned_data['mail_to']
            new_user_password = User.objects.make_random_password() # создает случайный пароль
            user = User.objects.get(email=mail_to) # берем пользователя по почте
            if user: # если такой находится
                user.set_password(new_user_password) # ставим новый пароль и сохраняем
                user.save()

                # send_mail(
                #     'Password changing!',
                #     f'Hi, {user.username}! Its your new password: {new_user_password}. Dont tell it anybody!',
                #     settings.EMAIL_HOST_USER,
                #     [mail_to]
                # )
            else:
                return HttpResponse('Пользователя с такой почтой не существует')
            send_mail(
                'test',
                'test',
                'some@mail.ru',
                [mail_to]
            )
            return HttpResponse('Письмо с новым паролем отправлено Вам на почту')
        return HttpResponse('Форма не валидна')
    
    form = EmailSendForm()
    return render(request, 'app_logic/send_email.html', {'form':form})