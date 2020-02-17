from django.db import models

from core.models import StockType
from shops.models import Shop 


class Product(models.Model):
    title       = models.CharField(max_length=120)
    price       = models.FloatField()
    stock       = models.ForeignKey('Stock', on_delete=models.SET_NULL, null=True, related_name='products')
    shop        = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    image       = models.ImageField(upload_to="product/%d-%m-%Y")
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Stock(models.Model):
    stock_type      = models.ForeignKey(StockType, on_delete=models.SET_NULL,null=True, related_name='stocks')
    stock_quantity  = models.FloatField()
    updated_at      = models.DateTimeField(auto_now=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.stock_quantity} {self.stock_type.name}")








