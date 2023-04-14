from django import forms

from main.models import Category, Review, ReviewPhotos, Product


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


class ReviewForm(forms.ModelForm):
    photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Review
        fields = ['product', 'comment', 'rating']

    def save(self, commit=True, user=None):
        review = super().save(commit=False)
        review.user = user
        if commit:
            review.save()
        photos = self.cleaned_data.get('photos')
        if photos:
            for photo in photos:
                ReviewPhotos.objects.create(review=review, photo=photo)
        return review
