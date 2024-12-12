from django import forms
from structure.models import Basket


class BasketForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пожелания к заказу',
    }))

    class Meta:
        model = Basket
        fields = ('comment',)