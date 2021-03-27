from django.db import models

# Create your models here.
from counterparty.models import Counterparty
from installer.models import Installer



class rab(models.Model):
    conterpaty = models.ForeignKey(Counterparty)
    groupInstaller = models.ForeignKey(Installer)
    dateInstaller = models.DateTimeField(null=False)
    dateCreate = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.dateInstaller


