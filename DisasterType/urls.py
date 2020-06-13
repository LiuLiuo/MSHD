from django.conf.urls import url
from DisasterType import views
urlpatterns = [
    url(r'^disasterType/',views.disasterType),
    url(r'^DeathStatistics/',views.deathStatistics),
    url(r'^CivilStructure/',views.civilStructure),
    url(r'^CommDisaster/',views.commDissaster),
    url(r'^CollapseRecord/',views.collapseRecord),
    url(r'^DisasterPrediction/',views.disasterPrediction),
]