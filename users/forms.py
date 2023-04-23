from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput, EmailInput

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_no')
        widgets = {
            'username': TextInput(attrs={
                'class': 'login__username',
            }),
            'email': EmailInput(attrs={
                'class': 'login__email',
            }),
            'phone_no': TextInput(attrs={
                'class': 'login__phone'
            })
        }


class UserEdit(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_no')
        widgets = {
            'first_name': TextInput(attrs={
                'class': "person-input",
            }),
            'last_name': TextInput(attrs={
                'class': 'person-input',
            }),
            'email': EmailInput(attrs={
                'class': "person-input",
                'style': 'width: 480px;'
            }),
            'phone_no': TextInput(attrs={
                'class': 'person-input',
                'style': 'width: 480px;'
            })
        }


class PersonalInformation(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'city', 'street', 'postcode', 'phone_no']
        required = ['first_name', 'last_name', 'city', 'street', 'postcode', 'phone_no']


