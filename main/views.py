from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm, CategoryForm
from .models import Product, Company, ProductPhotos, ProductSize


# Create your views here.
def home(request):
    recent_release = Product.objects.order_by('release')[:5]
    return render(request, 'main/home.html', {
        'recent_release': recent_release
    })


def catalog(request):
    # category = None
    items_list = Product.objects.all()
    form_category = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form_category.is_valid():
            categories = form_category.cleaned_data['categories']
            gender = form_category.cleaned_data['gender']
            filter = form_category.cleaned_data['sort_by']
            if categories:
                items_list = items_list.filter(category__in=categories)
            if gender:
                items_list = items_list.filter(gender__in=gender)
            if filter == 'price_asc':
                items_list = items_list.order_by('price')
            elif filter == 'price_desc':
                items_list = items_list.order_by('-price')
            elif filter == 'release_asc':
                items_list = items_list.order_by('release')
            elif filter == 'release_desc':
                items_list = items_list.order_by('-release')


            # elif filter == 'release_desc':

            # items_list = items_list.order_by('release')

    return render(request, 'main/catalog.html', {
        'items_list': items_list,
        'category_form': form_category,
    })


def check_out(request):
    cart = Cart(request)
    products = Product.objects.filter(id__in=cart.cart.keys())
    for product in products:
        print(cart.cart[str(product.id)]['price'])
    print(products)
    return render(request, 'main/test.html', {
        'products': products
    })


# @login_required
def brands(request):
    brands_list = Company.objects.order_by('name_company')
    return render(request, 'main/brands.html', {
        'title': 'Бренды',
        'brands_list': brands_list,
    })


def detail(request, item_id, size_id=0):
    item = Product.objects.get(pk=item_id)
    sizes = ProductSize.objects.filter(product=item).order_by('size')

    photos_product = ProductPhotos.objects.select_related().all()
    cart_product_form = CartAddProductForm()

    if size_id != 0:
        context = {
            'item': item,
            'sizes': sizes,
            'choiceSize': sizes.get(pk=size_id),
            'photos': photos_product,
            'cart_product_form': cart_product_form
        }
        return render(request, 'main/detailItem.html', context)
    context = {
        'item': item,
        'sizes': sizes,
        'photos': photos_product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'main/detailItem.html', context)


@require_POST
@login_required(login_url='/users/login')
def cart_add(request, product_id, size_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    size = ProductSize.objects.filter(product=product).get(pk=size_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, size)
        messages.success(request, 'Товар успешно добавлен в корзину!')
    else:
        messages.success(request, 'Произошла ошибка!')
    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id, size_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    size = ProductSize.objects.get(pk=size_id)
    cart.remove(product, size)
    return redirect('main:cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'main/cart.html', {
        'cart': cart,
    })
