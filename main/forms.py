from django import forms

from main.models import Category, Product


class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CategoryForm(forms.Form):
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[(category.id, category) for category in Category.objects.all()],
        required=False,
    )
    gender_choices = [
        ('W', 'Man'),
        ('M', 'Woman'),
        ('U', 'Unisex'),
    ]
    gender = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=gender_choices,
        required=False,
    )
    sort_choices = (
        ('price_asc', 'Цене (от меньшего к большему)'),
        ('price_desc', 'Цене (от большего к меньшему)'),
        ('release_asc', 'Дате выхода (от новых к старым)'),
        ('release_desc', 'Дате выхода (от старых к новым)'),
    )

    sort_by = forms.ChoiceField(choices=sort_choices, required=False,
                                widget=forms.RadioSelect())
