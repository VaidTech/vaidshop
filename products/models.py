from django.db import models

from core.models import StockType


class Product(models.Model):
    name        = models.CharField(max_length=120)
    price       = models.IntegerField()
    stock       = models.ForeignKey('Stock', on_delete=models.SET_NULL, null=True, related_name='products')
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Stock(models.Model):
    stock_type      = models.ForeignKey(StockType, on_delete=models.SET_NULL,null=True, related_name='stocks')
    measure         = models.FloatField(default=0)
    updated_at      = models.DateTimeField(auto_now=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.stock_type.name)
