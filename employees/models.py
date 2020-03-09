from django.db import models
from owners.models import Owner
from django.contrib.auth import get_user_model 

User = get_user_model()


class Employee(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="employees", null=True)
    mobile_number = models.CharField(max_length=11, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    profile_photo = models.ImageField(upload_to='%d-%m-%y', null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user.username)
