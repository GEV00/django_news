from django.urls import path
from user_auth.views import UserLogin, UserLogout, index


urlpatterns = [
    path('', index, name="main"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', UserLogout.as_view(), name="logout")
]
