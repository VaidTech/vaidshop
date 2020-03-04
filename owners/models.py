from django.db import models
from django.contrib.auth import get_user_model 
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import Group, Permission

from accounts.models import User


# User = get_user_model()

class Owner(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo   = models.ImageField(upload_to='%d-%m-%y')
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username








