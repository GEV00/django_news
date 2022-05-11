from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'user_auth/index.html', context={})

class UserLogin(LoginView):
    template_name = 'user_auth/login_form.html'


class UserLogout(LogoutView):
    next_page = '/newspaper'
# Create your views here.


class UserRegister(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'user_auth/register_form.html', context={'form':form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()#внесли в БД
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            phone = form.cleaned_data['phone']
            Profile.objects.create(
                user=user,
                phone=phone
            )
            user = authenticate(username=username, password=password)#аутенцифицировали
            login(request, user)#залогинили
            user.groups.add(1)#внесли в группу пользователей по умолчанию
            return HttpResponseRedirect('/profile')#направили на страницу новостей

        return render(request, 'user_auth/register_form.html', context={'form':form})


def profile(request):
    return render(request, 'user_auth/profile.html', context={})