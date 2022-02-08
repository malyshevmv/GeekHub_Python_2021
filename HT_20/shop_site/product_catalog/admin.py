from django.contrib import admin
from .models import Product, Category, Status, ProductInstance


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Status)
admin.site.register(ProductInstance)
