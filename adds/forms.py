from django.forms import ModelForm
from .models import Advertising, Comments
from django.db import models
from django import forms
from django.middleware.csrf import CsrfViewMiddleware
import datetime


class Add_addsForm(forms.ModelForm):
    class Meta():
        model=Advertising
        ordering = ['Advertising_price']
        fields=['Advertising_header',
                'Advertising_text',
                'Advertising_price',
                'Advertising_picture']

class Commentform(ModelForm):
    class Meta():
        model = Comments
        fields=['comments_text']
