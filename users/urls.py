from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registration/', views.sign_up, name='signup'),
    path('login/', views.sing_in, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/', views.profile_edit, name='profile_edit'),
              ]
