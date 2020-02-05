from django.db import models

from owners.models import Owner



class Shop(models.Model):
    owner       = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name        = models.CharField(max_length=120)
    address     = models.TextField()
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name        = models.CharField(max_length=120)
    price       = models.IntegerField()
    stock       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class ProductAddToShop(models.Model):
    shop        = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.shop.name}s {self.product.name}")





