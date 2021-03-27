from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .forms import PeopleForm
from django.views.generic import View


class AccauntView(View):
    def get(self, request):
        userForm = PeopleForm(None, instance=request.user)
        #userFormProfile = PeopleProfileForms(None, instance=request.user.userprofile)

        context= {
            "form" : userForm,
        #   "form2" : userFormProfile
        }
        return render(request, 'base/accaunt.html', context)
    def post(self, request):
        userForm = PeopleForm(request.POST, instance=request.user)
        #profileForm = PeopleProfileForms(request.POST, instance=request.user.userprofile)
        if userForm.is_valid():#and profileForm.is_valid():
            # print('ok')
            userForm.save()
            #profileForm.save()

        userForm = PeopleForm(None, instance=request.user)
        # userFormProfile = PeopleProfileForms(None, instance=request.user.userprofile)

        context = {
            "form": userForm,
            # "form2": userFormProfile
        }
        return render(request, 'base/accaunt.html', context)

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        new_user.username = username
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.email = email
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('index'))



    context = {
        'form': form,
    }
    return render(request, 'base/registration.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('index'))
    context = {
        'form': form,
    }
    return render(request, 'base/login.html', context)