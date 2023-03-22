from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/goods/<int:item_id>/', views.detail, name='details'),
    path('brands/', views.brands, name='brands'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
