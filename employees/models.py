from django.db import models
from django.contrib.auth import get_user_model


from owners.models import Owner

User = get_user_model()

class Employee(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    owner           = models.ForeignKey(Owner, on_delete=models.CASCADE)
    mobile_number   = models.CharField(max_length=11)
    date_of_birth   = models.DateField()
    gender          = models.CharField(max_length=10, choices=GENDER)
    profile_photo   = models.ImageField(upload_to='%d-%m-%y', blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username








