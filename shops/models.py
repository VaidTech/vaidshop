from django.db import models
from owners.models import Owner
from django.contrib.auth import get_user_model 

User = get_user_model()

class Shop(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='shops', null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=120, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="shop/%d-%m-%Y/", null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return str(self.name)