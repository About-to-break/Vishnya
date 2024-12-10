from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Россия, Москва, ул. Мира, дом 6',
    }))

    class Meta:
        model = Order
        fields = ('address',)
