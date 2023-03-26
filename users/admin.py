from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'phone_no']
    fieldsets = (
        ('Person Informations', {'fields': ('username', 'password', 'first_name', 'last_name', 'gender')}),
        ('Contacts', {'fields': ('email', 'phone_no')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )


admin.site.register(CustomUser, CustomUserAdmin)
