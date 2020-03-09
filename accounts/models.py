from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	is_owner	= models.BooleanField(blank=True, null=True)
	is_employee = models.BooleanField(blank=True, null=True)

	class Meta:
		db_table = 'accounts_user'
