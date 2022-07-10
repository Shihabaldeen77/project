from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Profile

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']





class Usermodel(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name']


class Profilemodel(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['phone_numper','city','image']

