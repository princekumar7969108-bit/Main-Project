from django.contrib import admin
from .models import  Cart,Order_items,Order
# Register your models here.
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Order_items)
