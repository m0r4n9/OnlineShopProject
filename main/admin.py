from django.contrib import admin
from .models import Company, Product, ProductPhotos, Category, SizeProduct


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


class CategoryInline(admin.StackedInline):
    model = Category
    max_num = 1
    extra = 0


class ProductSizeInline(admin.StackedInline):
    model = SizeProduct
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_item', 'category', 'gender']
    inlines = [ProductPhotosInline, CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
