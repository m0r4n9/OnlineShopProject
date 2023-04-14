from django.contrib import admin
from .models import *


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Название компании", {'fields': ['name_company']}),
        ("Страна", {'fields': ['country']}),
        ("Дата основания", {'fields': ['date_foundation']}),
    ]

    search_fields = ['name_company']
    list_display = ['name_company', 'date_foundation']


class ProductPhotosInline(admin.StackedInline):
    model = ProductPhotos
    max_num = 10
    extra = 0


class ProductSizesInline(admin.StackedInline):
    model = ProductSize
    max_num = 20
    extra = 0


class ReviewPhotosInline(admin.StackedInline):
    model = ReviewPhotos
    max_num = 4
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizesInline, ProductPhotosInline]


class ReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewPhotosInline]


admin.site.register(Company)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductSize)
admin.site.register(FavoriteList)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Purchase)
