# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone
from .models import TimeMontage, Montage, InstallationTask
from installer.models import CardProviderOfConstructionAndInstallationWorks

class AddMomtageForm(forms.ModelForm):
    class Meta:
        model = Montage
        fields = '__all__'
        widgets = {
            'dateMontage': forms.DateInput(attrs={'type': 'date'})
            }

def installer_kwargs(kw):
    installer = []
    print(kw)
    for i in kw['instance']:
        if i:
            installer.append(i)
    return installer

def add_installer(kwargs):
    card = CardProviderOfConstructionAndInstallationWorks.objects.all()
    if not kwargs['instance'].installationTask is None:
        task = InstallationTask.objects.filter(
            installationTask=kwargs['instance'].installationTask)
        if task[0].fences3D == True:
            card = card.filter(fences3D=True)
        if task[0].fencesProfiled == True:
            card = card.filter(fencesProfiled=True)
        if task[0].workingForFormica == True:
            card = card.filter(
                workingForFormica=True)
        if task[0].assemblyOfGreenhouses == True:
            card = card.filter(
                assemblyOfGreenhouses=True)
        if task[0].installationOfSlidingGates == True:
            card = card.filter(installationOfSlidingGates=True)
        if task[0].installationOfElectricSlidingGateDrives == True:
            card = card.filter(installationOfElectricSlidingGateDrives=True)
        if task[0].installationOfElectricSwingGateDrives == True:
            card = card.filter(installationOfElectricSwingGateDrives=True)
        if task[0].workingWithCellularPolycarbonate == True:
            card = card.filter(workingWithCellularPolycarbonate=True)
        if task[0].assemblyOfMetalStructures == True:
            card = card.filter(assemblyOfMetalStructures=True)
        if task[0].weldingWorks == True:
            card = card.filter(weldingWorks=True)
        if task[0].cordlessScrewdriver == True:
            card = card.filter(cordlessScrewdriver=True)
        if task[0].electricDrill == True:
            card = card.filter(electricDrill=True)
        if task[0].circularSaw == True:
            card = card.filter(circularSaw=True)
        if task[0].LBMLow == True:
            card = card.filter(LBMLow=True)
        if task[0].LBMBig == True:
            card = card.filter(LBMBig=True)
        if task[0].levelBuilder == True:
            card = card.filter(levelBuilder=True)
        if task[0].gasDrill == True:
            card = card.filter(gasDrill=True)
        if task[0].ladder == True:
            card = card.filter(ladder=True)
        if task[0].setOfSpanners == True:
            card = card.filter(setOfSpanners=True)
        if task[0].weldingMachine == True:
            card = card.filter(weldingMachine=True)
        if task[0].extension == True:
            card = card.filter(extension=True)
        if task[0].electricBump == True:
            card = card.filter(electricBump=True)
        if task[0].gasolineBump == True:
            card = card.filter(gasolineBump=True)
        if task[0].puncher == True:
            card = card.filter(puncher=True)
        if task[0].transportTheSpecifiedTool == True:
            card = card.filter(transportTheSpecifiedTool=True)
        if task[0].deliveryMaterialsTransport == True:
            card = card.filter(deliveryMaterialsTransport=True)
        if task[0].drivingLicense == True:
            card = card.filter(drivingLicense=True)
        if task[0].passengerCarWithUpperTrunk == True:
            card = card.filter(passengerCarWithUpperTrunk=True)
        if task[0].passengerCarWithTowBar == True:
            card = card.filter(passengerCarWithTowBar=True)
        if task[0].cargoUpTo15tons == True:
            card = card.filter(cargoUpTo15tons=True)
        if task[0].cargoFrom15To50Tons == True:
            card = card.filter(cargoFrom15To50Tons=True)
        if task[0].trailerLUpTo15m == True:
            card = card.filter(trailerLUpTo15m=True)
        if task[0].trailerLFrom15To25m == True:
            card = card.filter(trailerLFrom15To25m=True)
        if task[0].trailerL25mOrMore == True:
            card = card.filter(trailerL25mOrMore=True)
        if task[0].readinessToGoOnBusinessTrips == True:
            card = card.filter(readinessToGoOnBusinessTrips=True)
        if task[0].readyToLearn == True:
            card = card.filter(readyToLearn=True)
    card.order_by('lastName')
    return card

class ChangeMontageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChangeMontageForm, self).__init__(*args, **kwargs)

        self.fields['installer'].queryset = add_installer(kwargs)
    dateMontage = forms.CharField()


    class Meta:
        model = Montage
        fields = '__all__'
        widgets = {
            'dateMontage': forms.DateInput(attrs={'type': 'date'})
            }
