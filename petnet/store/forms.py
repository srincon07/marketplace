from django import forms

from .models import Product, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "first_name",
            "last_name",
            "address",
            "zipcode",
            "city",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
            "address": forms.TextInput(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
            "zipcode": forms.TextInput(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
            "city": forms.TextInput(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "category",
            "title",
            "description",
            "price",
            "image",
        )
        widgets = {
            "category": forms.Select(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
            "title": forms.TextInput(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
            "description": forms.Textarea(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
            "image": forms.FileInput(
                attrs={"class": "p-2 w-full border border-gray-200 rounded-xl"}
            ),
        }
