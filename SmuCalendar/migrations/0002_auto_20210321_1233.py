# Generated by Django 3.1.5 on 2021-03-21 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('installer', '0005_cardproviderofconstructionandinstallationworks_note'),
        ('SmuCalendar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='montage',
            name='LBMBig',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='LBMLow',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='assemblyOfGreenhouses',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='assemblyOfMetalStructures',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='cargoFrom15To50Tons',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='cargoUpTo15tons',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='categoryLaw',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='circularSaw',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='cordlessScrewdriver',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='deliveryMaterialsTransport',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='drivingLicense',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='electricBump',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='electricDrill',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='fences3D',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='fencesProfiled',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='gasDrill',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='gasolineBump',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='generator',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='installationOfElectricSlidingGateDrives',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='installationOfElectricSwingGateDrives',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='installationOfSlidingGates',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='ladder',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='legalStatus',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='level',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='levelBuilder',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='note',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='organizationalStructure',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='passengerCar',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='passengerCarWithTowBar',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='passengerCarWithUpperTrunk',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='puncher',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='readinessToGoOnBusinessTrips',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='readyToLearn',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='setOfSpanners',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='stamp',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='stateTheNumber',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='supplierStatus',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='theTrailer',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='trailerL25mOrMore',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='trailerLFrom15To25m',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='trailerLUpTo15m',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='transportTheSpecifiedTool',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='weldingMachine',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='weldingWorks',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='workSchedule',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='workingForFormica',
        ),
        migrations.RemoveField(
            model_name='montage',
            name='workingWithCellularPolycarbonate',
        ),
        migrations.CreateModel(
            name='InstallationTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installationTask', models.CharField(max_length=50, verbose_name='задача на монтаж')),
                ('workingForFormica', models.BooleanField(default=False, verbose_name='работа в Формике')),
                ('fences3D', models.BooleanField(default=False, verbose_name='Заборы 3D')),
                ('fencesProfiled', models.BooleanField(default=False, verbose_name='Заборы прфлист')),
                ('assemblyOfGreenhouses', models.BooleanField(default=False, verbose_name='Сборщик теплиц')),
                ('installationOfSlidingGates', models.BooleanField(default=False, verbose_name='Установка откатных ворот')),
                ('installationOfElectricSlidingGateDrives', models.BooleanField(default=False, verbose_name='Установка электро приводов откатных ворот')),
                ('installationOfElectricSwingGateDrives', models.BooleanField(default=False, verbose_name='Установка электро приводов распашных ворот')),
                ('workingWithCellularPolycarbonate', models.BooleanField(default=False, verbose_name='Работа с Сотовым поликарбонатом')),
                ('assemblyOfMetalStructures', models.BooleanField(default=False, verbose_name='Сборка металлоконструкций')),
                ('weldingWorks', models.BooleanField(default=False, verbose_name='Сварочные работы')),
                ('cordlessScrewdriver', models.BooleanField(default=False, verbose_name='Шуроповёрт аккумуляторный')),
                ('electricDrill', models.BooleanField(default=False, verbose_name='Электрическая дрель')),
                ('circularSaw', models.BooleanField(default=False, verbose_name='Циркулярная пила')),
                ('LBMLow', models.BooleanField(default=False, verbose_name='УШМ малая')),
                ('LBMBig', models.BooleanField(default=False, verbose_name='УШМ большая')),
                ('levelBuilder', models.BooleanField(default=False, verbose_name='Строительный уровень')),
                ('gasDrill', models.BooleanField(default=False, verbose_name='Бензобур')),
                ('ladder', models.BooleanField(default=False, verbose_name='Лестница, стремянка')),
                ('setOfSpanners', models.BooleanField(default=False, verbose_name='Набор гаечных ключей')),
                ('weldingMachine', models.BooleanField(default=False, verbose_name='Сварочная аппарат')),
                ('extension', models.BooleanField(default=False, verbose_name='Удлинитель')),
                ('electricBump', models.BooleanField(default=False, verbose_name='Отбойник электрический')),
                ('gasolineBump', models.BooleanField(default=False, verbose_name='Отбойник бензиновый')),
                ('puncher', models.BooleanField(default=False, verbose_name='Перфоратор')),
                ('transportTheSpecifiedTool', models.BooleanField(default=False, verbose_name='Возможность перевозить  указанный инструмент на собственном автотранспорте')),
                ('deliveryMaterialsTransport', models.BooleanField(default=False, verbose_name='Доставка материалов на объект своим транспортном')),
                ('drivingLicense', models.BooleanField(default=False, verbose_name='Водительские права')),
                ('stamp', models.CharField(blank=True, max_length=50, null=True, verbose_name='Марка')),
                ('stateTheNumber', models.CharField(blank=True, max_length=12, null=True, verbose_name='гос. Номер')),
                ('passengerCarWithUpperTrunk', models.BooleanField(default=False, verbose_name='легковой с верхним багажником')),
                ('passengerCarWithTowBar', models.BooleanField(default=False, verbose_name='легковой с фаркопом')),
                ('cargoUpTo15tons', models.BooleanField(default=False, verbose_name='Грузовой До 1,5тн.')),
                ('cargoFrom15To50Tons', models.BooleanField(default=False, verbose_name='Грузовой От 1,5 до 5,0 тн.')),
                ('trailerLUpTo15m', models.BooleanField(default=False, verbose_name='Прицеп L = до 1,5м.')),
                ('trailerLFrom15To25m', models.BooleanField(default=False, verbose_name='Прицеп L= от 1,5 до 2,5м.')),
                ('trailerL25mOrMore', models.BooleanField(default=False, verbose_name='Прицеп L= 2,5м. и более.')),
                ('readinessToGoOnBusinessTrips', models.BooleanField(default=False, verbose_name='Готовность выезда в командировки')),
                ('readyToLearn', models.BooleanField(default=False, verbose_name='готовность к обучению')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Примечание')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.cargo', verbose_name='Грузовой')),
                ('categoryLaw', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.categorylaw', verbose_name='Категория прав')),
                ('generator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.generator', verbose_name='Генератор')),
                ('legalStatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.legalstatus', verbose_name='Юридический статус:')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.level', verbose_name='Нивелир')),
                ('organizationalStructure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.organizationalstructure', verbose_name='Организационный состав')),
                ('passengerCar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.passengercar', verbose_name='Автомобиль легковой')),
                ('supplierStatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.supplierstatus', verbose_name='Статус поставщика:')),
                ('theTrailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.thetrailer', verbose_name='Прицеп')),
                ('workSchedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='installer.workschedule', verbose_name='График работы')),
            ],
        ),
        migrations.AddField(
            model_name='montage',
            name='installationTask',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmuCalendar.installationtask', verbose_name='задача на монтаж'),
        ),
    ]
