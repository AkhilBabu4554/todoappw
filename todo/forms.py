from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
class UsercreateForm(UserCreationForm):
    username=forms.CharField(max_length=50,
                            help_text="Enter a unique username.",
                            
                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1=forms.CharField(
          widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),
          label="Password",
        help_text="Password must contain at least 8 characters."
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}),
        label="Confirm Password",
        help_text="Conform your Password"
    )
    class Meta:
        model=User
        fields=["username","password1","password2"]
        