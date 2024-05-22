from django.contrib import admin
# Trong các file khác, chẳng hạn như admin.py hoặc views.py
from .models import user, Category, Product, Order, OrderDetail, AbstractUser

# Register your models here.
class ProductOptimize(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)

class OrderOptimize(admin.ModelAdmin):
    list_display = ('get_product_name', 'quantity', 'price')

    def get_product_name(self, obj):
        return obj.product.name

admin.site.register(user)
admin.site.register(Product, ProductOptimize)
admin.site.register(Category)
admin.site.register(OrderDetail, OrderOptimize)
admin.site.register(Order)