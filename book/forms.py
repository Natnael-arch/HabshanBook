from django import forms
from .models import Purchase


class PurchaseForm(forms.Form):
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    phone = forms.IntegerField()
