from _decimal import Decimal
from django.conf import settings
from main.models import Product

from django.shortcuts import get_object_or_404
from .models import Product, ProductSize


# class Cart:
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get('cart')
#         if not cart:
#             cart = self.session['cart'] = {}
#         self.cart = cart
#
#     def add_product(self, product_id, size_id):
#         product = get_object_or_404(Product, id=product_id)
#         size = get_object_or_404(ProductSize, id=size_id)
#         item_id = str(product_id) + '_' + str(size_id)
#         if item_id in self.cart:
#             self.cart[item_id]['quantity'] += 1
#         else:
#             self.cart[item_id] = {'quantity': 1, 'product_id': product_id, 'size_id': size_id}
#
#     def remove_product(self, product_id, size_id):
#         item_id = str(product_id) + '_' + str(size_id)
#         if item_id in self.cart:
#             del self.cart[item_id]
#
#     def __iter__(self):
#         product_ids = [self.cart[item]['product_id'] for item in self.cart]
#         products = Product.objects.filter(id__in=product_ids)
#         cart = self.cart.copy()
#         for product in products:
#             for item_id, item_data in cart.items():
#                 if item_data['product_id'] == product.id:
#                     cart[item_id]['product'] = product
#                     cart[item_id]['size'] = ProductSize.objects.get(id=item_data['size_id'])
#                     yield cart[item_id]
#
#     def __len__(self):
#         return sum(item['quantity'] for item in self.cart.values())

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product, size, quantity=1, update_quantity=False):
        product_id = f"{str(product.id)}_{str(size.id)}"
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'quantity': 0, 'id': product.id, 'size': size.size,
                                     'size_id': size.id}
        if update_quantity:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # product_ids = self.cart.keys()
        # products = Product.objects.filter(id__in=product_ids)
        product_ids = [self.cart[item]['id'] for item in self.cart]
        products = Product.objects.filter(id__in=product_ids)

        # for product in products:
        #     self.cart[str(product.id)]['product'] = product

        for product in products:
            for item_id, item_data in self.cart.items():
                if item_data['id'] == product.id:
                    self.cart[item_id]['product'] = product
                    self.cart[item_id]['size'] = ProductSize.objects.get(id=item_data['size_id'])
                    yield self.cart[item_id]

        # for product in products:
        #     for item in self.cart.values():
        #         item['price'] = Decimal(item['price'])
        #         item['total_price'] = item['price'] * item['quantity']
        #         yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
