from django.contrib import admin
from .models import Status, TimeMontage, Montage, InstallationTask

admin.site.register(Status)
admin.site.register(TimeMontage)
admin.site.register(Montage)
admin.site.register(InstallationTask)


