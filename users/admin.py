from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'phone_no']
    fieldsets = (
        ('Личная информация', {'fields': ('username', 'password', 'first_name', 'last_name', 'gender')}),
        ('Адресса', {'fields': ('city', 'street', 'postcode')}),
        ('Контакты', {'fields': ('email', 'phone_no')}),
        ('Даты', {'fields': ('last_login', 'date_joined')})
    )


admin.site.register(CustomUser, CustomUserAdmin)
