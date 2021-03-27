from django.db import models
from django.urls import reverse


# class Installer (models.Model):
#     firstNameInstaller = models.CharField("Фамилия монтажника", max_length=20)
#     lastNameInstaller = models.CharField("Имя монтажника", max_length=20)
#     telephone = models.CharField("Телефон", max_length=15, unique=True, null=False)
#     perf = models.BooleanField(default=False, verbose_name="Перфоратор")# Перфоратор
#     welder = models.BooleanField(default=False, verbose_name="Сварочный автомат")# Сварочник
#     car = models.BooleanField(default=False, verbose_name="Машина")# Машина
#     assistant2 = models.BooleanField(default=False, verbose_name="2 помошника")
#
#
#     def __str__(self):
#         return self.firstNameInstaller + " " + self.lastNameInstaller
#     def get_absolute_url(self):
#         return reverse('ChangeInstaller', kwargs={'changeInstaller': self.telephone})


class WorkSchedule(models.Model):
    workSchedule = models.CharField(
        max_length=30,
        verbose_name="График работы",
        null=False)
    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'
    def __str__(self):
        return self.workSchedule

class LegalStatus(models.Model):
    legalStatus = models.CharField(
        max_length=30,
        verbose_name="Юридический статус",
        null=False)
    class Meta:
        verbose_name = 'Юридический статус'
        verbose_name_plural = 'Юридические статусы'
    def __str__(self):
        return self.legalStatus

class SupplierStatus(models.Model):
    supplierStatus = models.CharField(
        max_length=30,
        verbose_name="Статус поставщика",
        null=False)
    class Meta:
        verbose_name = 'Статус поставщика'
        verbose_name_plural = 'Статусы поставщиков'
    def __str__(self):
        return self.supplierStatus

class SupplierEvaluationCustomer(models.Model):
    supplierEvaluationCustomer = models.PositiveSmallIntegerField(
        verbose_name="Оценка поставщика заказчиком")
    class Meta:
        verbose_name = 'Оценка поставщика заказчиком'
        verbose_name_plural = 'Оценки поставщиков заказчиком'
    def __str__(self):
        return self.supplierEvaluationCustomer

class SupplierEvaluationCompany(models.Model):
    supplierEvaluationCompany = models.PositiveSmallIntegerField(
        verbose_name="Оценка поставщика компанией")
    class Meta:
        verbose_name = 'Оценка поставщика компании'
        verbose_name_plural = 'Оценкаи поставщиков компаний'
    def __str__(self):
        return self.supplierEvaluationCompany

class CardTransportProvider(models.Model):
    """Карточка поставщика транспорта"""

    lastName = models.CharField(
        max_length=30,
        verbose_name="Фамилия",
        null=False,
        blank=False)
    firstName = models.CharField(
        max_length=30,
        verbose_name="Имя",
        null=False, blank=False)
    middleName = models.CharField(
        max_length=30,
        verbose_name="Отчество",
        null=True,
        blank=True)
    email = models.EmailField(
        verbose_name="Почта",
        null=True,
        blank=True)
    photo = models.ImageField(
        verbose_name="Фотография человека",
        null=True,
        blank=True,
        upload_to="TransportProviderCard")
    tel1 = models.CharField(
        max_length=12,
        verbose_name="Телефоны",
        null=False,
        unique=True
    )
    # tel2 = models.CharField(
    #     max_length=9,
    #     verbose_name="Телефонные номера 2",
    #     null=False,
    #     unique=True)
    openTruckLength = models.PositiveSmallIntegerField(
        verbose_name="Открытый грузовик полезная длина м.",
        null=True,
        blank=True)
    openTruckWidth = models.PositiveSmallIntegerField(
        verbose_name="Открытый грузовик полезная ширена м.",
        null=True,
        blank=True)
    openTruckHeight = models.PositiveSmallIntegerField(
        verbose_name="Открытый грузовик полезная Высота м.",
        null=True,
        blank=True)
    openTruckCarrying = models.PositiveSmallIntegerField(
        verbose_name="Открытый грузовик грузоподьёмность тон",
        null=True,
        blank=True)
    openTruckSelf_loader = models.PositiveSmallIntegerField(
        verbose_name="Открытый грузовик самопогрузчик тон",
        null=True,
        blank=True)
    closeTruckLength = models.PositiveSmallIntegerField(
        verbose_name="Закрытый грузовик полезная длина м.",
        null=True,
        blank=True)
    closeTruckWidth = models.PositiveSmallIntegerField(
        verbose_name="Закрытый грузовик полезная ширена м.",
        null=True,
        blank=True)
    closeTruckHeight = models.PositiveSmallIntegerField(
        verbose_name="Закрытый грузовик полезная Высота м.",
        null=True,
        blank=True)
    closeTruckCarrying = models.PositiveSmallIntegerField(
        verbose_name="Закрытый грузовик грузоподьёмность тон",
        null=True,
        blank=True)
    closeTruckAwning = models.BooleanField(
        verbose_name="Тент",
        default=False)
    closeTruckMetal = models.BooleanField(
        verbose_name="Металл. Кунг",
        default=False)
    workSchedule = models.ForeignKey(
        WorkSchedule,
        verbose_name='График работы:',
        on_delete=models.CASCADE)
    legalStatus = models.ForeignKey(
        LegalStatus,
        verbose_name='Юридический статус:',
        on_delete=models.CASCADE)
    supplierStatus = models.ForeignKey(
        SupplierStatus,
        verbose_name='Статус поставщика:',
        on_delete=models.CASCADE)
    note = models.TextField(
        verbose_name='Примечание',
        null=True,
        blank=True
    )

    class Meta:
        # unique_together = ('tel1', 'tel2')
        verbose_name = 'Карточка поставщика транспорта'
        verbose_name_plural = 'Карточки поставщиков транспорта'
    def __str__(self):
        return f'{self.tel1} {self.firstName}'

class PassengerCar(models.Model):
    passengerCar = models.CharField(max_length=50,
                                    verbose_name='Автомобиль легковой')
    class Meta:
        verbose_name = 'Автомобиль легковой'
        verbose_name_plural = 'Автомобили легковые'
    def __str__(self):
        return self.passengerCar



class Level(models.Model):
    level = models.CharField(max_length=30, verbose_name='Нивелир')
    class Meta:
        verbose_name = 'Нивелир'
        verbose_name_plural = 'Нивелиры'
    def __str__(self):
        return self.level

class Generator(models.Model):
    generator = models.CharField(max_length=30, verbose_name='Генератор')
    class Meta:
        verbose_name = 'Генератор'
        verbose_name_plural = 'Генераторы'
    def __str__(self):
        return self.generator


class Cargo(models.Model):
    cargo = models.CharField(max_length=50,
                             verbose_name='Грузовой',)
    class Meta:
        verbose_name = 'Грузовой'
        verbose_name_plural = 'Грузовые'
    def __str__(self):
        return self.cargo


class TheTrailer(models.Model):
    theTrailer = models.CharField(max_length=50,
                                  verbose_name='Прицеп')
    class Meta:
        verbose_name = 'Прицеп'
        verbose_name_plural = 'Прицепы'
    def __str__(self):
        return self.theTrailer


class OrganizationalStructure(models.Model):
    organizationalStructure = models.CharField(
        max_length=50,
        verbose_name='Организационный состав')
    class Meta:
        verbose_name = 'Организационный состав'
        verbose_name_plural = 'Организационные составы'
    def __str__(self):
        return self.organizationalStructure


class CategoryLaw(models.Model):
    categoryLaw = models.CharField(
        max_length=50,
        verbose_name='Водительские права'
    )
    class Meta:
        verbose_name = 'Водительские права'
        verbose_name_plural = 'Водительские права'

    def __str__(self):
        return self.categoryLaw


class CardProviderOfConstructionAndInstallationWorks(models.Model):
    """Карточка  поставщика Строительно-монтажных работ"""

    lastName = models.CharField(
        max_length=30,
        verbose_name="Фамилия",
        null=False,
        blank=False)
    firstName = models.CharField(
        max_length=30,
        verbose_name="Имя",
        null=False, blank=False)
    middleName = models.CharField(
        max_length=30,
        verbose_name="Отчество",
        null=True,
        blank=True)
    email = models.EmailField(
        verbose_name="Почта",
        null=True,
        blank=True)
    photo = models.ImageField(
        verbose_name="Фотография человека",
        null=True,
        blank=True,
        upload_to="TransportProviderCard")
    tel1 = models.CharField(
        max_length=20,
        verbose_name="Телефоны",
        null=False,
        unique=True
    )
    # tel2 = models.CharField(
    #     max_length=20,
    #     verbose_name="Телефонные номера 2",
    #     null=True,
    #     unique=True)
    residentialAddress = models.CharField(
        max_length=200,
        verbose_name='Адрес проживания')
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
    class Meta:
        verbose_name = 'Карточка поставщика Строительно-монтажных работ'
        verbose_name_plural = 'Карточки поставщиков Строительно-монтажных работ'
    def __str__(self):
        return f'{self.lastName} {self.firstName} - {self.tel1}'

class CardSpecialEquipmentSupplier(models.Model):
    """Карточка  поставщика Спецтехника"""

    lastName = models.CharField(
        max_length=30,
        verbose_name="Фамилия",
        null=False,
        blank=False)
    firstName = models.CharField(
        max_length=30,
        verbose_name="Имя",
        null=False, blank=False)
    middleName = models.CharField(
        max_length=30,
        verbose_name="Отчество",
        null=True,
        blank=True)
    email = models.EmailField(
        verbose_name="Почта",
        null=True,
        blank=True)
    photo = models.ImageField(
        verbose_name="Фотография человека",
        null=True,
        blank=True,
        upload_to="TransportProviderCard")
    tel1 = models.CharField(
        max_length=12,
        verbose_name="Телефоны",
        null=False,
        unique=True
    )
    # tel2 = models.CharField(
    #     max_length=9,
    #     verbose_name="Телефонные номера 2",
    #     null=True,
    #     unique=True)
    autocraneBoomLength = models.PositiveSmallIntegerField(
        verbose_name="Автокран Длина стрелы, м.",
        null=True,
        blank=True
    )
    autocraneLoadCapacity = models.PositiveSmallIntegerField(
        verbose_name='Автокран грузоподъемность, тн.',
        null=True,
        blank=True
    )
    autocraneCarBrand = models.CharField(
        max_length=50,
        verbose_name='Автокран база, марка автомобиля',
        null=True,
        blank=True
    )
    autocraneWheelAxle = models.PositiveSmallIntegerField(
        verbose_name='Автокран колесных осей',
        null=True,
        blank=True
    )
    autocraneTheDriveAxis = models.PositiveSmallIntegerField(
        verbose_name='Автокран привод на оси',
        null=True,
        blank=True
    )
    autocraneTheAverageCostm_h = models.PositiveSmallIntegerField(
        verbose_name='Автокран средняя стоимость м/час',
        null=True,
        blank=True
    )
    autocraneTravelPlaceWork = models.PositiveSmallIntegerField(
        verbose_name='Автокран проезд к месту работ, руб.',
        null=True,
        blank=True
    )
    backhoeLoaderStamp = models.CharField(
        max_length=30,
        verbose_name='Экскаватор погрузчик марка',
        null=True,
        blank=True
    )
    backhoeLoaderUsefulWidth = models.PositiveSmallIntegerField(
        verbose_name='Экскаватор погрузчик полезная Ширина, м.',
        null=True,
        blank=True
    )
    backhoeLoaderSideHeight = models.PositiveSmallIntegerField(
        verbose_name='Экскаватор погрузчик высота борта, м.',
        null=True,
        blank=True
    )
    backhoeLoaderLoadCapacity = models.PositiveSmallIntegerField(
        verbose_name='Экскаватор погрузчик грузоподъемность, тн.',
        null=True,
        blank=True
    )
    backhoeLoaderTheAverageCost = models.PositiveSmallIntegerField(
        verbose_name='Экскаватор погрузчик средняя  стоимость м/час',
        null=True,
        blank=True
    )
    backhoeLoaderTravelPlaceWork = models.PositiveSmallIntegerField(
        verbose_name='Экскаватор погрузчик проезд к месту работ, руб.',
        null=True,
        blank=True
    )
    backhoeLoaderBucket0_4 = models.BooleanField(
        verbose_name='Экскаватор погрузчик ковш 0,4м.',
        default=False
    )
    backhoeLoaderBucket0_6 = models.BooleanField(
        verbose_name='Экскаватор погрузчик ковш 0,6м.',
        default=False
    )
    backhoeLoaderBoer200 = models.BooleanField(
        verbose_name='Экскаватор погрузчик бур Ф200мм',
        default=False
    )
    backhoeLoaderBoer250 = models.BooleanField(
        verbose_name='Экскаватор погрузчик бур Ф250мм',
        default=False
    )
    backhoeLoaderBoer300 = models.BooleanField(
        verbose_name='Экскаватор погрузчик бур Ф300мм',
        default=False
    )
    backhoeLoaderHammer = models.BooleanField(
        verbose_name='Экскаватор погрузчик молот',
        default=False
    )
    drillingDeviceStamp = models.CharField(
        max_length=50,
        verbose_name='Бурильная установка марка (база)',
        null=True,
        blank=True
    )
    drillingDeviceWheelAxle = models.PositiveSmallIntegerField(
        verbose_name='Бурильная установка колесных осей',
        null=True,
        blank=True
    )
    drillingDeviceTheDriveAxis = models.CharField(
        max_length=70,
        verbose_name='Бурильная установка привод на оси',
        null=True,
        blank=True
    )
    drillingDeviceTheAverageCostost = models.PositiveSmallIntegerField(
        verbose_name='Бурильная установка средняя  стоимость м/час',
        null=True,
        blank=True
    )
    drillingDeviceAverageCostPerMeter = models.PositiveSmallIntegerField(
        verbose_name='Бурильная установка средняя  стоимость пог.м.',
        null=True,
        blank=True
    )
    drillingDeviceTravelPlaceWork = models.PositiveSmallIntegerField(
        verbose_name='Бурильная установка проезд к месту работ, руб.',
        null=True,
        blank=True
    )
    drillingDeviceBoer200 = models.BooleanField(
        verbose_name='Бурильная установка экскаватор погрузчик бур Ф200мм',
        default=False
    )
    drillingDeviceBoer250 = models.BooleanField(
        verbose_name='Бурильная установка экскаватор погрузчик бур Ф250мм',
        default=False
    )
    drillingDeviceBoer300 = models.BooleanField(
        verbose_name='Бурильная установка экскаватор погрузчик бур Ф300мм',
        default=False
    )
    drillingDeviceAutotowerTo15 = models.BooleanField(
        verbose_name='Бурильная установка автовышка до 15м.',
        default=False
    )
    drillingDeviceAutotowerTo15_23 = models.BooleanField(
        verbose_name='Бурильная установка автовышка от 15 до 23м.',
        default=False
    )
    drillingDeviceAutotowerUp23 = models.BooleanField(
        verbose_name='Бурильная установка автовышка от 23м.',
        default=False
    )
    legalStatus = models.ForeignKey(
        LegalStatus,
        verbose_name='Юридический статус',
        on_delete=models.CASCADE
    )
    supplierStatus = models.ForeignKey(
        SupplierStatus,
        verbose_name='Статус поставщика:',
        on_delete=models.CASCADE
    )
    note = models.TextField(
        verbose_name='Примечание',
        null=True,
        blank=True
    )
    class Meta:
        verbose_name = 'Карточка поставщика Спецтехники'
        verbose_name_plural = 'Карточки поставщиков Спецтехники'
    def __str__(self):
        return f'{self.tel1} {self.firstName}'

