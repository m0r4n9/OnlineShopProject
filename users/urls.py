from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_in, name='login_in'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/', views.profile_edit, name='profile_edit'),
]
