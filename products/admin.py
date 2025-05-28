from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Products


# Register your models here.
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

# Register Products
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('categories', 'created_at')

# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)


