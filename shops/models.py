from django.db import models

from owners.models import Owner
from accounts.models import User 


class Shop(models.Model):
    owner       = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='shops')
    creator		= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name        = models.CharField(max_length=50)
    address     = models.CharField(max_length=120)
    description = models.TextField()
    image       = models.ImageField(upload_to="shop/%d-%m-%Y/")
    updated_at  = models.DateTimeField(auto_now=True)
    created_at  = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.name)









