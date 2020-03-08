from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	is_owner	= models.BooleanField(default=False, null=True)
	is_employee = models.BooleanField(default=False, null=True)
