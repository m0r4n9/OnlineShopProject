from django import forms

from main.models import Product, ProductSize
from bootstrap4.widgets import RadioSelectButtonGroup, RadioSelect


class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    # sizes = forms.ModelMultipleChoiceField(queryset=ProductSize.objects.all(), widget=forms.CheckboxSelectMultiple)

    # class Meta:
    #     model = ProductSize
    #     fields = ['sizes']

    # def __init__(self, pk, *args, **kwargs):
    #     super(CartAddProductForm, self).__init__(*args, **kwargs)
    #     sizes = ProductSize.objects.filter()
    #     print(sizes[0].size)
    #     sizes_list = []
    #     for item in sizes:
    #         sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # for item in sizes:
    #     sizes_list.append((item, item.size))
    # self.fields['sizes'] = forms.ChoiceField(required=True, choices=sizes_list, widget=forms.RadioSelect(attrs={
    #     'class': 'test',
    # }))
