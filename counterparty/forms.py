# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone
#from django.contrib.auth.models import User
from .models import Counterparty

class AddCounterpartyForm(forms.ModelForm):
    class Meta:
        model = Counterparty
        fields = '__all__'


class ChangeCounterpartyForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    adress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    photo = forms.ImageField()

    class Meta:
        model = Counterparty
        fields = [
            'firstName',
            'lastName',
            'adress',
            'telephone',
            'email',
            'photo',
        ]
