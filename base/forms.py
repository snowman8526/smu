# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_check',
            'first_name',
            'last_name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['password'].help_text = 'Придумайте пароль'
        self.fields['password_check'].label = 'Повторите пароль'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'адрес электронной почты'
        self.fields['email'].help_text = 'Пожайлуста указывайте реальный адрес'

    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     password_check = self.cleaned_data['password_check']
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('Пользователь с данным пользователем уже зарегестрирован')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Пользователь с данной почтой уже зарегестрирован')
    #     if password != password_check:
    #         raise forms.ValidationError('Ваши пароли не совпадают! Попробуйте снова!')

    #Подсвечиваются поля
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        email = self.cleaned_data['email']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError({
                    'username': 'Пожалуйста выберите другое имя пользователя, т.к. пользователь с таким логином уже зарегистрирован в системе!'},
                code='user exists')

        if password != password_check:
            raise forms.ValidationError({
                'password': '',
                'password_check': 'Вы ошиблись при вводе паролей, они не совпадают, введите повторно!'},
                code='passwords do not match', )
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError({'email': 'Пользователь с таким email уже зарегистрирован!'},
                                        code='email exists')


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError({
                    'username': 'Пользователь с таким логином не зарегистрирован в системе!'},
                code='user exists')
        user =User.objects.get(username=username)
        if user and not user.check_password(password):
            raise forms.ValidationError({
                'password': 'Не верный пароль!'},
                code='user exists')


class PeopleForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    is_active = forms.BooleanField(required=False)
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'last_login',
        ]

    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'адрес электронной почты'
        self.fields['email'].help_text = 'Пожайлуста указывайте реальный адрес'
        self.fields['is_active'].label = 'Активен ли пользователь'
        self.fields['last_login'].label = 'последнй вход'




