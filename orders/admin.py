from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status',  'total_amount', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username', 'id')
    inlines = [OrderItemInline]  # Show OrderItems inline in Order

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'get_cost')
    list_filter = ('product',)
    search_fields = ('order__id', 'product__name')

    def get_cost(self, obj):
        return obj.get_cost()
    get_cost.short_description = 'Total Cost'


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

