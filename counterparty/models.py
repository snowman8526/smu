from django.db import models
#from installer.models import ModelInstaller
from django.urls import reverse


class Counterparty(models.Model):
    """ Партнёры """
    firstName = models.CharField(
        "Фамилия",
        max_length=25,
        null=True,
        blank=True)
    lastName = models.CharField("Имя",
                                max_length=25,
                                null=True,
                                blank=True)
    middleName = models.CharField(
        max_length=30,
        verbose_name="Отчество",
        null=True,
        blank=True)
    adress = models.CharField("Адресс", max_length=300, null=True, blank=True)
    telephone = models.CharField("Телефон",
                                 max_length=16,
                                 null=False,
                                 unique=True)
    email = models.EmailField(null=True, blank=True)


    photo = models.ImageField(upload_to='Counterparty', null=True, blank=True)

    def __str__(self):
        return self.firstName

    def get_absolute_url(self):
        return reverse('ChangeCounterparty', kwargs={'change': self.telephone})
