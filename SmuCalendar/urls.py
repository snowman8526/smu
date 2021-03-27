"""neroGrib2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from .views import (AddCalendar,
                    AddCalendarMontag,
                    timeMontage,
                    List7Day,
                    ChangeMontage,
                    counterpartyView,
                    Calendar)


urlpatterns = [
    path('', List7Day.as_view(), name='list7day'),
    # path('', Calendar.as_view(), name='calendar'),
    re_path(r'add/$', AddCalendar.as_view(), name='addCalendar'),
    re_path(r'add/(?P<id>[-\w]+)/$',
            AddCalendarMontag.as_view(),
            name='addCalendarMontag'),
    re_path(r'timeMontage', timeMontage, name='timeMontage'),
    # re_path(r'changeGroup/(?P<changeGroup>[-\w]+)/$', ChangeGroupInstaller.as_view(), name='ChangeGroupInstaller'),
    re_path(r'changeMontag/(?P<id>[-\w]+)/$',
            ChangeMontage.as_view(),
            name='MontageUrl'),
    re_path(r'con/$', counterpartyView, name='counterpartyView'),
    re_path(r'calendar/$', Calendar.as_view(), name='calendar')

]
