from django import forms
from webapp.models import Product, Review


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ["name", "phone", "address"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["feedback_text"]