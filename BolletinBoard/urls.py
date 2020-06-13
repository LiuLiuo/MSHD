from django.conf.urls import url
from BolletinBoard import views
urlpatterns = [
    url(r'',views.bolletinboard,name='bolletinboard'),
]