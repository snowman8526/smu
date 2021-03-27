from django.db import models
#from smu.installer.models import Installer
#from smu.counterparty.models import Counterparty
from counterparty.models import Counterparty
from installer.models import CardProviderOfConstructionAndInstallationWorks
from django.urls import reverse

from installer.models import (
    WorkSchedule,
    OrganizationalStructure,
    LegalStatus,
    SupplierStatus,
    TheTrailer,
    PassengerCar,
    CategoryLaw,
    Generator,
    Level,
    Cargo)


class TimeMontage(models.Model):
    time = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.time

class Status(models.Model):
    status = models.CharField(max_length=50, verbose_name="Статусы работы")

    def __str__(self):
        return self.status


class InstallationTask(models.Model):
    installationTask = models.CharField(
        max_length=50,
        verbose_name='задача на монтаж')
    workingForFormica = models.BooleanField(
        verbose_name='работа в Формике',
        default=False)
    fences3D = models.BooleanField(
        verbose_name='Заборы 3D',
        default=False
    )
    fencesProfiled = models.BooleanField(
        verbose_name='Заборы прфлист',
        default=False
    )
    assemblyOfGreenhouses = models.BooleanField(
        verbose_name='Сборщик теплиц',
        default=False
    )
    installationOfSlidingGates = models.BooleanField(
        verbose_name='Установка откатных ворот',
        default=False
    )
    installationOfElectricSlidingGateDrives = models.BooleanField(
        verbose_name='Установка электро приводов откатных ворот',
        default=False
    )
    installationOfElectricSwingGateDrives = models.BooleanField(
        verbose_name='Установка электро приводов распашных ворот',
        default=False
    )
    workingWithCellularPolycarbonate = models.BooleanField(
        verbose_name='Работа с Сотовым поликарбонатом',
        default=False
    )
    assemblyOfMetalStructures = models.BooleanField(
        verbose_name='Сборка металлоконструкций',
        default=False
    )
    weldingWorks = models.BooleanField(
        verbose_name='Сварочные работы',
        default=False
    )
    cordlessScrewdriver = models.BooleanField(
        verbose_name='Шуроповёрт аккумуляторный',
        default=False
    )
    electricDrill = models.BooleanField(
        verbose_name='Электрическая дрель',
        default=False
    )
    circularSaw = models.BooleanField(
        verbose_name='Циркулярная пила',
        default=False
    )
    LBMLow = models.BooleanField(
        verbose_name='УШМ малая',
        default=False
    )
    LBMBig = models.BooleanField(
        verbose_name='УШМ большая',
        default=False
    )
    levelBuilder = models.BooleanField(
        verbose_name='Строительный уровень',
        default=False
    )
    level = models.ForeignKey(
        Level,
        verbose_name='Нивелир',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    gasDrill = models.BooleanField(
        verbose_name='Бензобур',
        default=False
    )
    generator = models.ForeignKey(
        Generator,
        on_delete=models.CASCADE,
        verbose_name='Генератор',
        null=True,
        blank=True
    )
    ladder = models.BooleanField(
        verbose_name='Лестница, стремянка',
        default=False,
    )
    setOfSpanners = models.BooleanField(
        verbose_name='Набор гаечных ключей',
        default=False
    )
    weldingMachine = models.BooleanField(
        verbose_name='Сварочная аппарат',
        default=False
    )
    extension = models.BooleanField(
        verbose_name='Удлинитель',
        default=False
    )
    electricBump = models.BooleanField(
        verbose_name='Отбойник электрический',
        default=False
    )
    gasolineBump = models.BooleanField(
        verbose_name='Отбойник бензиновый',
        default=False
    )
    puncher = models.BooleanField(
        verbose_name='Перфоратор',
        default=False
    )
    transportTheSpecifiedTool = models.BooleanField(
        verbose_name='Возможность перевозить  указанный инструмент на собственном автотранспорте',
        default=False
    )
    deliveryMaterialsTransport = models.BooleanField(
        verbose_name='Доставка материалов на объект своим транспортном',
        default=False
    )
    drivingLicense = models.BooleanField(
        verbose_name='Водительские права',
        default=False
    )
    categoryLaw = models.ForeignKey(
        CategoryLaw,
        verbose_name='Категория прав',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    stamp = models.CharField(
        max_length=50,
        verbose_name='Марка',
        null=True,
        blank=True
    )
    stateTheNumber = models.CharField(
        max_length=12,
        verbose_name='гос. Номер',
        null=True,
        blank=True
    )
    passengerCar = models.ForeignKey(
        PassengerCar,
        verbose_name='Автомобиль легковой',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    passengerCarWithUpperTrunk = models.BooleanField(
        verbose_name='легковой с верхним багажником',
        default=False
    )
    passengerCarWithTowBar = models.BooleanField(
        verbose_name='легковой с фаркопом',
        default=False
    )
    cargo = models.ForeignKey(
        Cargo,
        verbose_name='Грузовой',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    cargoUpTo15tons = models.BooleanField(
        verbose_name='Грузовой До 1,5тн.',
        default=False
    )
    cargoFrom15To50Tons = models.BooleanField(
        verbose_name='Грузовой От 1,5 до 5,0 тн.',
        default=False
    )
    theTrailer = models.ForeignKey(
        TheTrailer,
        verbose_name="Прицеп",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    trailerLUpTo15m = models.BooleanField(
        verbose_name='Прицеп L = до 1,5м.',
        default=False
    )
    trailerLFrom15To25m = models.BooleanField(
        verbose_name='Прицеп L= от 1,5 до 2,5м.',
        default=False
    )
    trailerL25mOrMore = models.BooleanField(
        verbose_name='Прицеп L= 2,5м. и более.',
        default=False
    )
    workSchedule = models.ForeignKey(
        WorkSchedule,
        verbose_name="График работы",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    readinessToGoOnBusinessTrips = models.BooleanField(
        verbose_name='Готовность выезда в командировки',
        default=False
    )
    readyToLearn = models.BooleanField(
        verbose_name='готовность к обучению',
        default=False
    )
    note = models.TextField(
        verbose_name='Примечание',
        null=True,
        blank=True
    )
    organizationalStructure = models.ForeignKey(
        OrganizationalStructure,
        verbose_name='Организационный состав',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    legalStatus = models.ForeignKey(
        LegalStatus,
        verbose_name='Юридический статус:',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    supplierStatus = models.ForeignKey(
        SupplierStatus,
        verbose_name='Статус поставщика:',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.installationTask}"

class Montage(models.Model):
    installer = models.ForeignKey(
        CardProviderOfConstructionAndInstallationWorks,
        verbose_name="установщики",
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    counterparty = models.ForeignKey(
        Counterparty,
        verbose_name="Заказчик",
        on_delete=models.CASCADE,
        null=False)
    installationTask = models.ForeignKey(
        InstallationTask,
        verbose_name='задача на монтаж',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    dateMontage = models.DateField(verbose_name="Дата монтожа", null=True)
    timeMontage = models.ForeignKey(
        TimeMontage,
        verbose_name="Время проведения установки",
        on_delete=models.CASCADE,
        null=True)
    status = models.ForeignKey(
        Status,
        verbose_name="Какой статус выполнения?",
        on_delete=models.CASCADE,
        null=False,
        default=True)
    residentialAddress = models.CharField(
        max_length=200,
        verbose_name='Адрес проживания')



    def __str__(self):
        return"{} {} {}".format(self.installer, self.dateMontage, self.timeMontage)
    
    def get_absolute_url(self):
        return "/changeMontag/{}".format(self.id)