from mimetypes import knownfiles
from pyexpat import model
from django import forms
from django.db.models import fields
from .models import *

class postblogforms (forms.ModelForm):
    class Meta: 
        model = Blog
        fields = ("title",)

