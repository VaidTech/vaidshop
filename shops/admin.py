from django.contrib import admin

from .models import Shop, Product, ProductAddToShop


admin.site.register(Shop)

admin.site.register(Product)

admin.site.register(ProductAddToShop)

