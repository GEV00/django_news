from django.urls import path
from user_auth.views import *

urlpatterns = [
    path('', index, name="main"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', UserLogout.as_view(), name="logout"),
    path('register/', UserRegister.as_view(), name='register'),
    path('profile/', profile, name='profile')
]
