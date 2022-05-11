from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=True, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=True, help_text='Фамилия')
    phone = forms.CharField(max_length=11, help_text='Номер телефона')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'password1', 'password2')
