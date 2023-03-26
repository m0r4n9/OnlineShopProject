from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/goods/<int:item_id>/', views.detail, name='details_product'),
    path('brands/', views.brands, name='brands'),
    path('cart/', views.cart_detail, name='cart'),
    path('cart/add/<int:product_id>', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
