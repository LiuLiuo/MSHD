"""mshd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import *
from DataStorage.views import  *
from DisasterType.views import *
from index.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',index),
    url(r'^bolletinboard/',include('BolletinBoard.urls')),
    url(r'^upload/',include('upload.urls')),
    url(r'^disasterType/', disasterType),
    url(r'^DeathStatistics/', deathStatistics),
    url(r'^InjuredStatistics/', injuredStatistic),
    url(r'^MissingStatistics/', missingStatistic),
    url(r'^CivilStructure/', civilStructure),
    url(r'^BrickwoodStructure/', brickwoodStructure),
    url(r'^MasonryStructure/', masonryStructure),
    url(r'^FrameworkStructure/', frameworkStructure),
    url(r'^OtherStructure/', otherStructure),
    url(r'^CommDisaster/', commDisaster),
    url(r'^TrafficDisaster/', trafficDisaster),
    url(r'^WaterDisaster/', waterDisaster),
    url(r'^OilDisaster/', oilDisaster),
    url(r'^GasDisaster/', gasDisaster),
    url(r'^PowerDisaster/', powerDisaster),
    url(r'^IrrigationDisaster/', irrigationDisaster),
    url(r'^CollapseRecord/', collapseRecord),
    url(r'^LandslideRecord/', landslideRecord),
    url(r'^DebrisRecord/', debrisRecord),
    url(r'^KarstRecord/', karstRecord),
    url(r'^CrackRecord/', crackRecord),
    url(r'^SettlementRecord/', settlementRecord),
    url(r'^OtherRecord/', otherRecord),
    url(r'^DisasterInfo/', disasterInfo),
    url(r'^DisasterPrediction/', disasterPrediction),
    url(r'^DataStorage/$', getfromDB),
    url(r'^getDisasterType', getDisasterType),
    url(r'^DataStorage/336$', saveCommDisaster, name='CommDisaster'),
    url(r'^DataStorage/111$', saveDeathStatistics, name='DeathStatistics'),
    url(r'^DataStorage/221$', saveCivilStructure, name='CivilStructure'),
    url(r'^DataStorage/441$', saveCollapseRecord, name='CollapseRecord'),
    url(r'^DataStorage/552$', saveDisasterPrediction, name='DisasterPrediction'),
    #  url(r'^$', getfromDB),
    url(r'^DataStorage/refreshRequest/', changeRequeststatus),
    url(r'^DataStorage/showsentData/', showsentData),
    url(r'^DataStorage/shownotsendData/', shownotsendData),
    url(r'^search',search),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
