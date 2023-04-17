from _decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm, CategoryForm, ReviewForm, ReviewFormImages
from .models import Product, Company, ProductSize, FavoriteList, Review, Purchase, ReviewPhotos


def home(request):
    recent_release = Product.objects.order_by('release')[:5]
    return render(request, 'main/home.html', {
        'recent_release': recent_release
    })


def catalog(request):
    items_list = Product.objects.all()
    form_category = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form_category.is_valid():
            categories = form_category.cleaned_data['categories']
            gender = form_category.cleaned_data['gender']
            filter_by = form_category.cleaned_data['sort_by']

            if categories:
                items_list = items_list.filter(category__in=categories)
            if gender:
                items_list = items_list.filter(gender__in=gender)
            if filter_by == 'price_asc':
                items_list = items_list.order_by('price')
            elif filter_by == 'price_desc':
                items_list = items_list.order_by('-price')
            elif filter_by == 'release_asc':
                items_list = items_list.order_by('release')
            elif filter_by == 'release_desc':
                items_list = items_list.order_by('-release')

    return render(request, 'main/catalog.html', {
        'items_list': items_list,
        'category_form': form_category,
    })


def brands(request):
    brands_list = Company.objects.order_by('name_company')
    return render(request, 'main/brands.html', {
        'title': 'Бренды',
        'brands_list': brands_list,
    })


def detail(request, item_id, size_id=0):
    item = Product.objects.get(pk=item_id)
    sizes = ProductSize.objects.filter(product=item, quantity__gt=0).order_by('size')
    purchases = Purchase.objects.filter(products__in=[item], user=request.user)
    review_list = Review.objects.filter(product=item)
    cart_product_form = CartAddProductForm()
    include_item = False
    review = None

    if purchases:
        review = ReviewFormImages(initial={'product': item})

    if request.user.is_authenticated:
        is_favorite = FavoriteList.objects.get(user=request.user).products.all().filter(id=item_id)
        if is_favorite:
            include_item = True

    if size_id != 0:
        context = {
            'item': item,
            'sizes': sizes,
            'choiceSize': sizes.get(pk=size_id),
            'cart_product_form': cart_product_form,
            'include_item': include_item,
            'review': review,
            'purchases': purchases,
            'review_list': review_list,
        }
    else:
        context = {
            'item': item,
            'sizes': sizes,
            'cart_product_form': cart_product_form,
            'include_item': include_item,
            'review': review,
            'purchases': purchases,
            'review_list': review_list,
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
    for item in cart.cart:
        print(item)
    return render(request, 'main/cart.html', {
        'cart': cart,
    })


@login_required(login_url='/users/login')
def add_favorite(request, item_id):
    favorite = FavoriteList.objects.get(user=request.user)
    product = Product.objects.get(id=item_id)
    favorite_list = FavoriteList.objects.get(user=request.user)
    favorite_list.products.add(product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
def remove_favorite(request, item_id):
    favorite = FavoriteList.objects.get(user=request.user)
    product = Product.objects.get(id=item_id)
    favorite_list = FavoriteList.objects.get(user=request.user)
    favorite_list.products.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))


def check_out(request):
    cart = Cart(request)
    products = []
    product_ids = []
    product_size = {}
    total_price = 0
    for item in cart.cart.values():
        total_price += Decimal(item['price'] * item['quantity'])
        product_size[item['id']] = item['size']
        product_ids.append(item['id'])

    for size in product_size.keys():
        product = Product.objects.get(id=size)
        products.append(product)
        size = ProductSize.objects.get(product=product, size=product_size[size])
        size.quantity -= 1
        size.save()

    Purchase.objects.create(user=request.user, total_price=total_price).products.set(products)
    cart.clear()
    return redirect('users:profile')


def add_review(request):
    if request.method == 'POST':
        form = ReviewFormImages(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']
            product = form.cleaned_data['product']
            review_obj = Review.objects.create(user=user, comment=comment, rating=rating, product=product)
            for photo in files:
                print(photo)
                ReviewPhotos.objects.create(review=review_obj, images=photo)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            print("Form invalid")

