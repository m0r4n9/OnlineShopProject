from django import forms

from main.models import Product

CHOICES = [('item1', 'item 1'),
           ('item2', 'item 2')]


class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.widgets.RadioSelect(attrs={
        'class': 'test'
    }))
