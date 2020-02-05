from django import forms 

from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'mobile_number',
            'date_of_birth',
            'gender',
            'profile_photo'
        ]



