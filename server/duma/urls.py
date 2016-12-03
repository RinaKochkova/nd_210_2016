"""GosDuma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^factions/$', views.factions_index, name='factions_index'),
    url(r'^deputy/([0-9]+)/$', views.deputy_details, name='deputy_page'),  # номер будет передан как аргумент-строка
    url(r'^factions/([0-9]{1})/$', views.faction_details, name='faction_page'),
    url(r'^stats/$', views.stats, name='statistics'),
]
