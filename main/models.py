import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from users.models import CustomUser

# Create your models here.

CATEGORY_CLOTHES = [
    ('S', 'Shoes'),
    ('O', 'Outerwear'),
    ('P', 'Pants'),
]

GENDER_ID = [
    ('W', 'Man'),
    ('M', 'Woman'),
    ('U', 'Unisex'),
]


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Company(models.Model):
    name_company = models.CharField(max_length=250, unique=True)
    country = models.CharField(max_length=50)
    image_link = models.CharField(max_length=250)
    date_foundation = models.PositiveIntegerField(default=current_year(),
                                                  validators=[MinValueValidator(1800), max_value_current_year])

    def __str__(self):
        return self.name_company

    def get_length_products(self):
        return len(Product.objects.filter(company_id=self.id))


class Category(models.Model):
    type_product = models.CharField(max_length=1, choices=CATEGORY_CLOTHES)

    def __str__(self):
        if self.type_product == 'S':
            return 'Обувь'
        elif self.type_product == 'O':
            return 'Верхняя одежда'
        elif self.type_product == 'P':
            return 'Штаны'


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_item = models.CharField(max_length=250)
    image_prev = models.ImageField(null=True, blank=True, upload_to="images/")
    gender = models.CharField(max_length=1, choices=GENDER_ID, default='U')
    release = models.DateTimeField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name_item

    def get_all_photos(self):
        return ProductPhotos.objects.filter(product_parent=self)


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=4)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.size


class ProductPhotos(models.Model):
    product_parent = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/")


class FavoriteList(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username + 'favorite list'

    def get_all_products(self):
        return self.products.all()


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.rating}'

    def get_all_photos(self):
        return ReviewPhotos.objects.filter(review=self).all()


class ReviewPhotos(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='photos')
    images = models.ImageField(upload_to='images/')


class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    check_products = models.ManyToManyField(Product)
    products = models.JSONField(default=dict)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    street = models.CharField(max_length=100, default=None)
    city = models.CharField(max_length=100, default=None)
    postcode = models.CharField(max_length=20, default=None)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Order {self.id}'

    def count_products(self):
        return len(self.products)
