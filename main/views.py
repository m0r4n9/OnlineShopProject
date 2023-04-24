from _decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from django.core.mail import send_mail

from OnlineShopProject import settings
from users.forms import PersonalInformation
from .cart import Cart
from .forms import CartAddProductForm, ReviewFormImages, ProductFilterSet, ReviewFilterSet
from .models import Product, Company, ProductSize, FavoriteList, Review, Purchase, ReviewPhotos


def home(request):
    recent_release = Product.objects.order_by('-release')[:5]
    return render(request, 'main/home.html', {
        'recent_release': recent_release
    })


def brands(request):
    brands_list = Company.objects.order_by('name_company')
    return render(request, 'main/brands.html', {
        'title': 'Бренды',
        'brands_list': brands_list,
    })


def catalog(request):
    products = Product.objects.all()
    filterset = ProductFilterSet(request.GET, queryset=products)

    if 'price' in request.GET:
        direction = '-' if request.GET['price'] == 'desc' else ''
        filterset.qs = filterset.qs.order_by(direction + 'price')

    if 'release_date' in request.GET:
        direction = '-' if request.GET['release_date'] == 'desc' else ''
        filterset.qs = filterset.qs.order_by(direction + 'release_date')

    filtered_params = request.GET.copy()
    if 'page' in filtered_params:
        del filtered_params['page']
    filtered_query_string = filtered_params.urlencode()

    paginator = Paginator(filterset.qs, per_page=6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'filterset': filterset,
        'page_obj': page_obj,
        'filtered_query_string': filtered_query_string
    }
    return render(request, 'main/catalog.html', context)


def detail(request, item_id, size_id=0):
    item = Product.objects.get(pk=item_id)
    sizes = ProductSize.objects.filter(product=item, quantity__gt=0).order_by('size')
    review_list = Review.objects.filter(product=item).order_by('-created_at')
    cart_product_form = CartAddProductForm()
    include_item = False
    purchases = None
    review = None

    if request.user.is_authenticated:
        purchases = Purchase.objects.filter(check_products__in=[item], user=request.user)
        is_favorite = FavoriteList.objects.get(user=request.user).products.all().filter(id=item_id)
        if is_favorite:
            include_item = True

    if purchases:
        review = ReviewFormImages(initial={'product': item})

    context = {
        'item': item,
        'sizes': sizes,
        'choiceSize': sizes.get(pk=size_id) if size_id != 0 else None,
        'cart_product_form': cart_product_form,
        'include_item': include_item,
        'review': review,
        'review_list': review_list,
    }
    return render(request, 'main/detailItem.html', context)


def detail_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    products = Product.objects.filter(company_id=company.id)
    filterset = ProductFilterSet(request.GET, queryset=products)

    context = {
        'company': company,
        'produts': filterset.qs,
        'filterset': filterset,
    }
    return render(request, 'main/companyDetail.html', context)


@login_required(login_url='/users/login')
def favorite_products(request):
    favorite = FavoriteList.objects.get(user=request.user).get_all_products()
    return render(request, 'main/favoriteItems.html', {
        'favorite_products': favorite,
    })


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


@login_required(login_url='/users/login')
def cart_remove(request, product_id, size_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    size = ProductSize.objects.get(pk=size_id)
    cart.remove(product, size)
    return redirect('main:cart')


def cart_detail(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = PersonalInformation(request.POST, instance=request.user)
        if form.is_valid() and len(cart.cart) != 0:
            for field in form.cleaned_data:
                if not form.cleaned_data[field]:
                    form.add_error(field, 'Это поле обязательное')
                    return render(request, 'main/cart.html', {
                        'cart': cart,
                        'form': form,
                    })
            form.save()

            total_price = 0
            list_products = []

            for item in cart.cart.values():
                total_price += Decimal(item['price'] * item['quantity'])
                product = Product.objects.get(id=item['id'])
                list_products.append(product)
                size = ProductSize.objects.get(product=product, size=item['size'])
                if size.quantity >= item['quantity']:
                    size.quantity -= item['quantity']
                else:
                    return render(request, 'main/cart.html', {
                        'cart': cart,
                        'form': form,
                    })
                size.save()

            userPurches = request.user
            Purchase.objects.create(user=userPurches, total_price=total_price, street=userPurches.street,
                                    city=userPurches.city,
                                    products=cart.cart,
                                    postcode=userPurches.postcode).check_products.set(list_products),

            # send_email_purches(subject='Покупка', message='Спасибо за покупку', userName=request.user,
            #                    products=products,
            #                    recipient_list=[request.user.email])
            # cart.clear()
            return redirect('main:cart')
    else:
        form = PersonalInformation(instance=request.user)
    return render(request, 'main/cart.html', {
        'cart': cart,
        'form': form
    })


@login_required(login_url='/users/login')
def add_favorite(request, item_id):
    product = Product.objects.get(id=item_id)
    favorite_list = FavoriteList.objects.get(user=request.user)
    favorite_list.products.add(product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
def remove_favorite(request, item_id):
    product = Product.objects.get(id=item_id)
    favorite_list = FavoriteList.objects.get(user=request.user)
    favorite_list.products.remove(product)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
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
            form = ReviewFormImages()


def send_email_purches(subject, message, userName, products, recipient_list):
    html_message = render_to_string('message/message.html', {
        'subject': subject,
        'message': message,
        'user': userName,
        'products': products,
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, html_message=html_message)


def list_purchases(request):
    purchases = Purchase.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'list_purchases': purchases
    }
    return render(request, 'main/listPurchases.html', context)


def purchase_detail(request, purchase_id):
    purchase = Purchase.objects.get(pk=purchase_id)
    list_products = []
    for key in purchase.products.values():
        product = Product.objects.get(id=key['id'])
        list_products.append((product, key['size']))
    for product in list_products:
        print(product[0].name_item)
    context = {
        'purchase': purchase,
        'list_products': list_products,
    }
    return render(request, 'main/purchaseDetail.html', context)
