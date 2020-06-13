from django.shortcuts import render
from receiveData.models import TotalData


def bolletinboard(request):
    totalDatas = TotalData.objects.all()
    return render(request,'bolletinboard.html',{'totalDatas':totalDatas})
# Create your views here.
