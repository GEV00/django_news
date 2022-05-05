from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


def index(request):
    return render(request, 'user_auth/index.html', context={})

class UserLogin(LoginView):
    template_name = 'user_auth/login_form.html'


class UserLogout(LogoutView):
    next_page = '/newspaper'
# Create your views here.
