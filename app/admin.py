from django.contrib import admin
# Trong các file khác, chẳng hạn như admin.py hoặc views.py
from .models import user, Category, Product, Order, OrderDetail, AbstractUser

# Register your models here.


admin.site.register(user)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OrderDetail)
admin.site.register(Order)