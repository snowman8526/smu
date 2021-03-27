# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone
#from django.contrib.auth.models import User
from .models import Installer#, GroupInstaller

class AddInstallerForm(forms.ModelForm):
    class Meta:
        model = Installer
        fields = [
            'firstNameInstaller',
            'lastNameInstaller',
            'telephone',
            #'groupInstaller',
        ]


class ChangeInstallerForm(forms.ModelForm):
    firstNameInstaller = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    lastNameInstaller = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    class Meta:
        model = Installer
        fields = [
            'firstNameInstaller',
            'lastNameInstaller',
            'telephone',
            # 'groupInstaller',
        ]


# class AddGroupInstallerForm(forms.ModelForm):
#     class Meta:
#         model = GroupInstaller
#         fields = [
#             'NameGroupInstaller',
#         ]
#
#
# class ChangeGroupInstallerForm(forms.ModelForm):
#     NameGroupInstaller = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
#
#     class Meta:
#         model = GroupInstaller
#         fields = [
#             'NameGroupInstaller',
#         ]


