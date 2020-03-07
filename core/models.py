from django.db import models


class StockType(models.Model):
    name = models.CharField(max_length=120, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)