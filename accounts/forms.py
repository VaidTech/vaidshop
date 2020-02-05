from django import forms 
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm

from owners.models import Owner



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








