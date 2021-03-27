from django.contrib import admin
from .models import (CardTransportProvider,
                     SupplierStatus,
                     SupplierEvaluationCompany,
                     SupplierEvaluationCustomer,
                     LegalStatus,
                     WorkSchedule,
                     CardSpecialEquipmentSupplier,
                     CardProviderOfConstructionAndInstallationWorks,
                     Generator,
                     Level,
                     Cargo,
                     OrganizationalStructure,
                     PassengerCar,
                     TheTrailer,
                     CategoryLaw)


class CardProviderAdmin(admin.ModelAdmin):
    search_fields = [
        'lastName',
        'email',
        'tel1',
        'note',
    ]
    list_filter = (
        'cordlessScrewdriver',
        'electricDrill',
        'circularSaw',
        'LBMLow',
        'LBMBig',
        'levelBuilder',
        'level',
        'gasDrill',
        'generator',
        'ladder',
        'setOfSpanners',
        'weldingMachine',
        'extension',
        'electricBump',
        'gasolineBump',
        'puncher',
        'legalStatus',
        'supplierStatus',
        'organizationalStructure',
        'workSchedule',
        'workingForFormica',
        'fences3D',
        'fencesProfiled',
        'assemblyOfGreenhouses',
        'installationOfSlidingGates',
        'installationOfElectricSlidingGateDrives',
        'installationOfElectricSwingGateDrives',
        'workingWithCellularPolycarbonate',
        'assemblyOfMetalStructures',
        'weldingWorks',
        'transportTheSpecifiedTool',
        'deliveryMaterialsTransport',
        'drivingLicense',
        'categoryLaw',
        'stamp',
        'passengerCar',
        'passengerCarWithUpperTrunk',
        'passengerCarWithTowBar',
        'cargo',
        'cargoUpTo15tons',
        'cargoFrom15To50Tons',
        'theTrailer',
        'trailerLUpTo15m',
        'trailerLFrom15To25m',
        'trailerL25mOrMore',
        'readinessToGoOnBusinessTrips',
        'readyToLearn',

    )


class CardTransportProviderAdmin(admin.ModelAdmin):
    search_fields = [
        'lastName',
        'email',
        'tel1',
        'note',
    ]

class CardSpecialEquipmentSupplierAdmin(admin.ModelAdmin):
    search_fields = [
        'lastName',
        'email',
        'tel1',
        'note',
    ]



admin.site.register(SupplierStatus)
admin.site.register(SupplierEvaluationCompany)
admin.site.register(SupplierEvaluationCustomer)
admin.site.register(LegalStatus)
admin.site.register(WorkSchedule)
admin.site.register(Generator)
admin.site.register(Level)
admin.site.register(CardTransportProvider, CardTransportProviderAdmin)
admin.site.register(
    CardProviderOfConstructionAndInstallationWorks,
    CardProviderAdmin)
admin.site.register(
    CardSpecialEquipmentSupplier,
    CardSpecialEquipmentSupplierAdmin)
admin.site.register(Cargo)
admin.site.register(CategoryLaw)
admin.site.register(OrganizationalStructure)
admin.site.register(PassengerCar)
admin.site.register(TheTrailer)
