from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpUserForm(UserCreationForm):
    """User registration form"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'John'}),
            'email': forms.EmailInput(attrs={'placeholder': 'JohnWick23@gmail.com'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Your password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Repeat your password'})
        }


class LoginUserForm(AuthenticationForm):
    """User login form"""
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'John'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))

