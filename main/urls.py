from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
                  path('', views.home, name='home'),
                  path('catalog/', views.catalog, name='catalog'),
                  path('catalog/goods/<int:item_id>', views.detail, name='details_product'),
                  path('catalog/goods/<int:item_id>/<int:size_id>', views.detail, name='details_product'),
                  path('favorite_products/', views.favorite_products, name='favorite_products'),
                  path('brands/', views.brands, name='brands'),
                  path('cart/', views.cart_detail, name='cart'),
                  path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
                  path('cart/add/<int:product_id>/<int:size_id>', views.cart_add, name='cart_addTrue'),
                  path('cart/remove/<int:product_id>/<int:size_id>/', views.cart_remove, name='cart_remove'),
                  path('catalog/goods/favorite_<int:item_id>', views.add_favorite, name='favorite_add'),
                  path('catalog/goods/favorite_remove_<int:item_id>', views.remove_favorite, name='remove_favorite'),
                  path('review/', views.add_review, name='review'),
                  # path('test/', views.test, name='test')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
