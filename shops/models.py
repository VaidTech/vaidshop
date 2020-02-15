from django.db import models

from owners.models import Owner
from products.models import Product 


class Shop(models.Model):
    owner       = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='shops')
    name        = models.CharField(max_length=120)
    address     = models.TextField()
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.name)


class ShopProduct(models.Model):
    shop        = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_products')
    product     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_shops')
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.shop.name}s {self.product.name}")








