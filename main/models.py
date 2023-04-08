import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    date_foundation = models.PositiveIntegerField(default=current_year(),
                                                  validators=[MinValueValidator(1800), max_value_current_year])

    def __str__(self):
        return self.name_company


class Category(models.Model):
    type_product = models.CharField(max_length=1, choices=CATEGORY_CLOTHES)


class ProductSize(models.Model):
    size = models.CharField(max_length=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.size


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(ProductSize)
    name_item = models.CharField(max_length=250)
    image_prev = models.ImageField(null=True, blank=True, upload_to="images/")
    gender = models.CharField(max_length=1, choices=GENDER_ID, default='U')
    release = models.DateTimeField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name_item


class ProductPhotos(models.Model):
    product_parent = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/")
