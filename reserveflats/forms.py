from django import forms
from .models import SuccessPaymentUser


class SuccessForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'field',
        'required placeholder': 'Ваше имя',
    }))
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'field',
        'required placeholder': 'Ваша фамилия',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'field',
        'required placeholder': 'Ваш Email',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'field',
        'required id': 'phone'
    }))

    class Meta:
        model = SuccessPaymentUser
        fields = ('name', 'surname', 'email', 'phone')
