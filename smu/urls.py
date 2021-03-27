"""smu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LogoutView
from base.views import AccauntView, registration_view, login_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accaunt/', AccauntView.as_view(), name='accaunt'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('', include('index.urls'), name='index'),
    path('counterparty/', include('counterparty.urls'), name='counterparty'),
    # path('installer/', include('installer.urls'), name='installer'),
    path('', include('SmuCalendar.urls'), name='Calendar'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)