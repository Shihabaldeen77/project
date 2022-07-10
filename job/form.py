from dataclasses import field
from pyexpat import model
from django import forms
from .models import Apply,Job

class Applayform(forms.ModelForm):
    class Meta:
        model=Apply
        fields =['name','email','vewsite','cv','jop']


class Addjob(forms.ModelForm):
    class Meta:
        model=Job
        fields = ['title','jop_type','salary','experiance','vecancy','description','image','categori']



        