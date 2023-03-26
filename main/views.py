from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.urls import reverse

from .cart import Cart
from .forms import CartAddProductForm
from .models import Item, Company


# Create your views here.
def home(request):
    recent_release = Item.objects.order_by('-release')[:5]
    return render(request, 'main/home.html', {
        'products': recent_release
    })


def catalog(request):
    items_list = Item.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'main/catalog.html', {
        'items_list': items_list,
        'cart_product_form': cart_product_form,
    })


# @login_required
def brands(request):
    brands_list = Company.objects.order_by('name_company')
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

@require_POST
@login_required(login_url='/users/login')
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product)
        return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=product_id)
    cart.remove(product)
    return redirect('main:cart')
    # return redirect(reverse('main:details_product', args=(product.id,)))


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'main/cart.html', {
        'cart': cart
    })
