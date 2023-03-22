from django.contrib import admin
from .models import Company, Item, Inventory


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Название компании", {'fields': ['name_company']}),
        ("Страна", {'fields': ['country']}),
        ("Дата основания", {'fields': ['date_foundation']}),
    ]

    search_fields = ['name_company']
    list_display = ['name_company', 'date_foundation']

class InventoryItem(admin.StackedInline):
    model = Inventory

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name_item', 'category', 'gender']
    list_filter = ['category']
    inlines = [InventoryItem]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Item, ItemAdmin)
