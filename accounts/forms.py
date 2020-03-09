import re
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from owners.models import Owner
from employees.models import Employee
from accounts.models import User 


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserUpdateForm(forms.Form):
    username    = forms.CharField(required=True)
    email       = forms.EmailField(required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        regex_username = re.compile("[!@#$%^&*()+ ]")
        is_not_valid = regex_username.findall(username)
        if is_not_valid:
            raise forms.ValidationError("Enter a valid username.It only take [a-zA-Z0-9_]")
        return username 

    
class OwnerRegisterForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('profile_photo',)


class LoginForm(forms.Form):
    username        = forms.CharField()
    password        = forms.CharField(widget=forms.PasswordInput())