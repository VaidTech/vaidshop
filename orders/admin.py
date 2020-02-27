from django.contrib import admin

from .models import Order, Customer, OrderProduct


admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(OrderProduct)


