from django.contrib import admin

from .models import *


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Название компании", {'fields': ('name_company',)}),
        ("Страна", {'fields': ('country',)}),
        ("Дата основания", {'fields': ('date_foundation',)}),
        ("Лого", {'fields': ('image_link',)})
    ]

    list_display = ['name_company', 'date_foundation']
    list_filter = ['country']
    search_fields = ['name_company']


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


class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Диапазон цен:'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0-1500', '0 - 1500'),
            ('1500-5000', '1500 - 5000'),
            ('5000-15000', '5000 - 15000'),
            ('15000+', '15000 и выше'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-1500':
            return queryset.filter(price__gte=0, price__lte=1500)
        elif self.value() == '1500-5000':
            return queryset.filter(price__gte=1500, price__lte=5000)
        elif self.value() == '5000-15000':
            return queryset.filter(price__gte=5000, price__lte=15000)
        elif self.value() == '15000+':
            return queryset.filter(price__gte=15000)


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Информация о товаре", {'fields': ('company', 'category', 'name_item', 'price', 'gender')}),
        ("Превью товара", {'fields': ('image_prev',)}),
        ("Дата выпуска", {'fields': ('release',)}),
    ]
    inlines = [ProductSizesInline, ProductPhotosInline]
    list_display = ['name_item', 'company', 'price', 'gender']
    list_filter = ['gender', PriceRangeFilter, 'company']
    search_fields = ['name_item']


class ProductSizeAdmin(admin.ModelAdmin):
    list_filter = ['size']


class ReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewPhotosInline]
    list_filter = ['rating']


class PurchesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Покупатель', {'fields': ('user',)}),
        ('Адресс доставки', {'fields': ('city', 'street', 'postcode')}),
        ("Список товаров", {'fields': ('products', 'check_products', 'total_price')}),
        ("Время", {'fields': ('created_at',)}),
    ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductSize, ProductSizeAdmin)
admin.site.register(FavoriteList)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Purchase, PurchesAdmin)
# admin.site.register(ReviewPhotos)
