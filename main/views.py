from django.shortcuts import render

from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Item, Company


# Create your views here.
def index(request):
    return render(request, 'main/layout.html')


def catalog(request):
    items_list = Item.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'main/catalog.html', {
        'items_list': items_list,
        'cart_product_form': cart_product_form,
    })


# @login_required
def brands(request):
    brands_list = Company.objects.all()
    return render(request, 'main/brands.html', {
        'title': 'Бренды',
        'brands_list': brands_list,
    })


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/detailItem.html', {
        'item': item,
        'cart_product_form': cart_product_form,
    })
