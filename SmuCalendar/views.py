from django.http import JsonResponse
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import TimeMontage, Montage
from counterparty.models import Counterparty
from installer.models import CardProviderOfConstructionAndInstallationWorks
from .forms import AddMomtageForm, ChangeMontageForm
import datetime


class List7Day(View):
    def get(self, request):
        nowtime = datetime.date.today()
        now7 = nowtime + datetime.timedelta(days=7)
        nowr = nowtime
        date = [nowtime]
        for i in range(6):
            nowr = nowr + datetime.timedelta(days=1)
            date.append(nowr)
        montage = Montage.objects.filter(dateMontage__range=[nowtime, now7])
        installed = []
        for i in montage.values('installer'):
            if i not in installed:
                installed.append(i['installer'])
        installer = CardProviderOfConstructionAndInstallationWorks.objects.filter(id__in=installed)
        tMontage = TimeMontage.objects.all()
        context = {
            'date': date,
            'montage': montage,
            'installer': installer,
            'timeMontage': tMontage,
        }
        return render(request, 'SmuCalendar/List7Day.html', context)


class ChangeMontage(View):
    def get(self, request, id):
        montage = get_object_or_404(Montage, id=id)
        montageForm = ChangeMontageForm(instance=montage)
        context = {
            "forms": montageForm
        }
        return render(request, "SmuCalendar/changeCalendar.html", context)
    def post(self, request, id):
        montage = get_object_or_404(Montage, id=id)
        change = ChangeMontageForm(request.POST or None, instance=montage)
        if change.is_valid():
            change.save()
        return redirect('list7day')


def timeMontage(request):
    installer = request.GET.get('installer')
    dateMontage = request.GET.get('dateMontage')
    montage = Montage.objects.filter(installer=int(installer)).filter(dateMontage=dateMontage)
    list_montage = list(montage)
    timemontage = TimeMontage.objects.all()
    for i in list_montage:
        timemontage = timemontage.exclude(time=i.timeMontage)
    context = {}
    for timeM in timemontage:
        context[timeM.id] = str(timeM.time)
    return JsonResponse(context)

def counterpartyView(request):
    counterparty = Counterparty.objects.all()
    context = {
        "counterparty": counterparty,

    }
    return JsonResponse(context)


class AddCalendar(View):
    def get(self, request):
        forms = AddMomtageForm(None)
        context = {
            "forms": forms
        }
        return render(request, "SmuCalendar/addCalendar.html", context)
    def post(self, request):
        addMontage = AddMomtageForm(request.POST or None)
        if addMontage.is_valid():
            addMont = addMontage.save(commit=False)
            addMont.save()
        return redirect('list7day')


class AddCalendarMontag(View):
    def get(self, request, id):
        conterparty = Counterparty.objects.get(pk=id)
        print(conterparty.adress)
        forms = AddMomtageForm(None)
        forms.fields['residentialAddress'].initial = conterparty.adress
        forms.fields['counterparty'].initial = conterparty

        context = {
            "forms": forms
        }
        return render(request, "SmuCalendar/addCalendar.html", context)
    def post(self, request, id):
        addMontage = AddMomtageForm(request.POST or None)
        if addMontage.is_valid():
            addMont = addMontage.save(commit=False)
            addMont.save()
        return redirect('list7day')


class Calendar(View):
    def get(self, request):
        # print(request.GET.get('date'))
        calendar = datetime.datetime.strptime(
            request.GET.get('date'),
            '%Y-%m-%d')
        montage = Montage.objects.filter(dateMontage=calendar)
        print(calendar)
        try:
            date = [montage[0].dateMontage]
        except IndexError:
            date = str(calendar.strftime('%Y-%m-%d'))
        installed = []
        for i in montage.values('installer'):
            if i not in installed:
                installed.append(i['installer'])
        installer = CardProviderOfConstructionAndInstallationWorks.objects.filter(
            id__in=installed)
        tMontage = TimeMontage.objects.all()
        context = {
            'date': date,
            'montage': montage,
            'installer': installer,
            'timeMontage': tMontage,
        }
        return render(request, 'SmuCalendar/calendar.html', context)
