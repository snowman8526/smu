from django.shortcuts import render
from django.views.generic import View
# from .models import Installer
from .forms import AddInstallerForm, ChangeInstallerForm

# class InstallerList(View):
#     def get(self, request):
#         installer = Installer.objects.all()
#         context = {
#             "installer": installer,
#         }
#         return render(request, "installer/List.html", context)


# class InstallerGroupList(View):
#     def get(self, request):
#         groups = GroupInstaller.objects.all()
#         context = {
#             "groups": groups,
#         }
#         return render(request, "installer/ListGroup.html", context)



# class AddInstaller(View):
#     def get(self, request):
#         form = AddInstallerForm(None)
#         # print("1 ", form)
#         context ={
#             'form': form
#         }
#
#         return render(request, 'installer/addInstaller.html', context)
#     def post(self, request):
#         addInstaller = AddInstallerForm(request.POST, request.FILES or None)
#         if addInstaller.is_valid():
#             #print(counterparty.cleaned_data)
#             if "photo" in request.FILES:
#                 addInstaller.photo = request.FILES['photo']
#             addInstaller.save(commit=True)
#             return render(request, 'counterparty/List.html', {"counterparty": ""})
#         return render(request, 'counterparty/List.html', {"counterparty": ""})



# class AddGroupInstaller(View):
#     def get(self, request):
#         form = AddGroupInstallerForm(None)
#         # print("1 ", form)
#         context = {
#             'form': form
#         }
#
#         return render(request, 'installer/addGroup.html', context)
#
#     def post(self, request):
#         print(request.FILES)
#         addInstaller = AddGroupInstallerForm(request.POST, request.FILES or None)
#         if addInstaller.is_valid():
#             # print(counterparty.cleaned_data)
#             if "photo" in request.FILES:
#                 addInstaller.photo = request.FILES['photo']
#             addInstaller.save(commit=True)
#             return render(request, 'installer/List.html', {"installer": ""})
#         return render(request, 'installer/List.html', {"installer": ""})
#

# class ChangeGroupInstaller(View):
#     def get(self, request, changeGroup):
#         installGroup = GroupInstaller.objects.get(NameGroupInstaller=changeGroup)
#         form = ChangeGroupInstallerForm(instance=installGroup)
#         context = {
#             "form": form
#         }
#         return render(request, "installer/changeGroup.html", context)



#
# class ChangeInstaller(View):
#     def get(self, request, changeInstaller):
#         print(changeInstaller)
#         install = Installer.objects.get(telephone=changeInstaller)
#         form = ChangeInstallerForm(instance=install)
#         context = {
#             "form": form
#         }
#         return render(request, "installer/changeInstaller.html", context)