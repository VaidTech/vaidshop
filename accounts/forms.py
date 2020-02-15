from django import forms 
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm

import re

from owners.models import Owner
from employees.models import Employee

User = get_user_model()


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

        widgets = {
            'username': forms.TextInput(attrs={
                                    'placeholder': 'Username',
                                    'id': 'username',
                                }
                            ),
            'email': forms.EmailInput(attrs={
                                    'placeholder': 'Email-Address',
                                    'id': 'email',
                                }
                            )
        }


class UserUpdateForm(forms.Form):
    username    = forms.CharField(required=True, max_length=120, widget=forms.TextInput(attrs={
                                                                    'placeholder': 'Username', 
                                                                    'id': 'username'
                                                                }
                                                            )
                                                        )
    email       = forms.EmailField(required=False, widget=forms.TextInput(attrs={
                                                                    'placeholder': 'Email Address', 
                                                                    'id': 'email'
                                                                }
                                                            )
                                                        )

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
        fields = [
            'profile_photo'
        ]

        widgets = {
            'profile_photo': forms.FileInput(attrs={
                                    'id': 'image'
                                }
                            )
        }


class LoginForm(forms.Form):
    username        = forms.CharField(widget=forms.TextInput(
                                                attrs={
                                                    'placeholder': 'Username',
                                                    'id': 'username'
                                                }
                                            )
                                        )
    password        = forms.CharField(widget=forms.PasswordInput(
                                                attrs={
                                                    'placeholder': 'Password',
                                                    'id': 'login-password'
                                                }
                                            )
                                        )









