from django import forms
import django_filters

from main.models import Category, Review, Product, GENDER_ID


class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class ReviewFormImages(ReviewForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())

    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ['images']


class ProductFilterSet(django_filters.FilterSet):
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
                                                        widget=forms.CheckboxSelectMultiple)
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    order_by = django_filters.OrderingFilter(
        choices=(
            ('price', 'По возрастанию'),
            ('-price', 'По убыванию'),
            ('-release', 'От новых к старым'),
            ('release', 'От старых к новым'),
        ),
        fields=(
            ('price', 'price'),
            ('release', 'release'),
        ),
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'gender']

class ReviewFilterSet(django_filters.FilterSet):
    order_by = django_filters.OrderingFilter(
        choices=(
            ('rating', 'Сначала отрицательные отзывы'),
            ('-rating', 'Сначала положительные отзыва'),
            ('-created_at', 'Сначало новые'),
            ('created_at', 'Сначала старые'),
        ),
        fields=(
            ('rating', 'rating'),
            ('created_at', 'created_at')
        )
    )
