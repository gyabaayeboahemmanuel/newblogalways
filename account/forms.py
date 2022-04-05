from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            # "password2",
            "first_name",
            "last_name",
            "email",
        )

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("profile_picture",)

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )