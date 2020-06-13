import os

from django.shortcuts import render
from receiveData import models
from django.conf import settings
from django.db import connection
from django.http import JsonResponse
from django.http import FileResponse
#settings.configure()
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core import serializers
from django.forms.models import model_to_dict
import json,django
django.setup()

# Create your views here.
def getfromDB(request):

        if models.DisasterRequest.status == '0':
            models.DisasterRequest.objects.filter(status='0').update(status='未发送')
        if models.DisasterRequest.status == '1':
            models.DisasterRequest.objects.filter(status='0').update(status='已发送')
        datalist=models.DisasterRequest.objects.filter(status='未发送')
       #type = request.POST['disasterType']
        return render(request, 'dataStorage.html', {'data_list':datalist}) #显示数据库中的所有内容

def saveCommDisaster(request):
    datalist = models.CommDisaster.objects.all()
    json_data = serializers.serialize('json', datalist)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)

def saveDeathStatistics(request):
     datalist = models.DeathStatistics.objects.all()
     json_data = serializers.serialize('json', datalist)
     json_data = json.loads(json_data)
     return JsonResponse(json_data, safe=False)
def saveCivilStructure(request):
     datalist = models.CivilStructure.objects.all()
     json_data = serializers.serialize('json', datalist)
     json_data = json.loads(json_data)
     return JsonResponse(json_data, safe=False)
def saveCollapseRecord(request):
    datalist = models.CollapseRecord.objects.all()

    json_data = serializers.serialize('json', datalist)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)
def saveDisasterPrediction(request):
    datalist = models.DisasterPrediction.objects.all()
    json_data = serializers.serialize('json', datalist)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)
def getDisasterType(request,self):
    type = request.POST.get('disasterType')
    return render(request, 'dataStorage.html', {'type': type})

def changeRequeststatus(request):
    ROOT_DIR='47.93.86.172'

    requestlist = models.DisasterRequest.objects.filter(status="未发送")
    if request.method=="POST":
     disasterType=request.POST.get('disasterType')

     if(disasterType=='336'):
         requestData=models.CommDisaster.objects.all()
         models.DisasterRequest.objects.filter(status="未发送", disasterType="336").update(status="已发送")
         json_data = serializers.serialize('json', requestData)
         json_str = json.dumps(json_data) #将CommDisaster中的数据转化成json
         data_list = json.loads(json_str)  #将json数据转化成字符串，便于存储

         path=os.path.join(ROOT_DIR,'336')
         if not os.path.exists(path):
             os.makedirs(path)
         with  open(os.path.join(path,'CommonDisaster.json'), 'w') as f:
             json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '111'):
        requestData = models.DeathStatistics.objects.all()
        models.DisasterRequest.objects.filter(status="未发送", disasterType="111").update(status="已发送")
        json_data = serializers.serialize('json', requestData)
        json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
        data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
        path = os.path.join(ROOT_DIR, '111')
        if not os.path.exists(path):
            os.makedirs(path)
        with  open(os.path.join(path,'DeathStatistics.json'), 'w') as f:
            json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '221'):
            requestData = models.CivilStructure.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="221").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '221')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'CivilStructure.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '441'):
            requestData = models.CollapseRecord.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="441").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '441')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'CollapseRecord.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '552'):
            requestData = models.DisasterPrediction.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="552").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '552')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'DeathPrediction.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '112'):
            requestData = models.InjuredStatistics.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="112").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '112')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'InjuredStatistics.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '113'):
            requestData = models.MissingStatistics.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="113").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '113')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'MissingStatistics.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '222'):
            requestData = models.BrickwoodStructure.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="222").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '222')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'BrickwoodStructure.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '223'):
            requestData = models.MasonryStructure.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="223").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '223')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'MasonryStructure.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '224'):
            requestData = models.InjuredStatistics.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="224").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '224')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'InjuredStatistics.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '225'):
            requestData = models.OtherStructure.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="225").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '225')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'OtherStructure.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '331'):
            requestData = models.TrafficDisaster.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="331").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '331')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'TrafficDisaster.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '332'):
            requestData = models.WaterDisaster.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="332").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '332')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'WaterDisaster.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '333'):
            requestData = models.OilDisaster.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="333").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '333')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'OilDisaster.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '334'):
            requestData = models.GasDisaster.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="334").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '334')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'GasDisaster.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '335'):
         requestData = models.PowerDisaster.objects.all()
         models.DisasterRequest.objects.filter(status="未发送", disasterType="335").update(status="已发送")
         json_data = serializers.serialize('json', requestData)
         json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
         data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
         path = os.path.join(ROOT_DIR, '335')
         if not os.path.exists(path):
             os.makedirs(path)
         with  open(os.path.join(path, 'PowerDisaster.json'), 'w') as f:
             json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '337'):
         requestData = models.IrrigationDisaster.objects.all()
         models.DisasterRequest.objects.filter(status="未发送", disasterType="337").update(status="已发送")
         json_data = serializers.serialize('json', requestData)
         json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
         data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
         path = os.path.join(ROOT_DIR, '337')
         if not os.path.exists(path):
             os.makedirs(path)
         with  open(os.path.join(path, 'IrrigationDisaster.json'), 'w') as f:
             json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '442'):
            requestData = models.LandslideRecord.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="442").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '442')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'LandslideRecord.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '443'):
            requestData = models.DebrisRecord.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="443").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '443')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'DebrisRecord.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '444'):
            requestData = models.KarstRecord.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="444").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '444')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'KarstRecord.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '445'):
            requestData = models.CrackRecord.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="445").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '445')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'CrackRecord.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '446'):
            requestData = models.SettlementRecord.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="446").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '446')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'SettlementRecord.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '447'):
            requestData = models.OtherRecord.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="447").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '447')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'OtherRecord.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back
     if (disasterType == '551'):
            requestData = models.DisasterInfo.objects.all()
            models.DisasterRequest.objects.filter(status="未发送", disasterType="551").update(status="已发送")
            json_data = serializers.serialize('json', requestData)
            json_str = json.dumps(json_data)  # 将CommDisaster中的数据转化成json
            data_list = json.loads(json_str)  # 将json数据转化成字符串，便于存储
            path = os.path.join(ROOT_DIR, '551')
            if not os.path.exists(path):
                os.makedirs(path)
            with  open(os.path.join(path,'DisasterInfo.json'), 'w') as f:
                json.dump(data_list, f, ensure_ascii=False)  # Reading data back

     return render(request, 'dataStorage.html', {'data_list': requestlist})  # 显示数据库中的

def showsentData(request):#显示已经发送的数据

    models.DisasterRequest.objects.filter(status='1').update(status='已发送')

    if request.method == "GET":
        requestlist = models.DisasterRequest.objects.filter(status='已发送')

    return render(request, 'dataStorage.html', {'data_list': requestlist})  # 显示数据库中的


def shownotsendData(request):  # 显示已经发送的数据

    models.DisasterRequest.objects.filter(status = '0').update(status='未发送')

    if request.method == "GET":
        requestlist = models.DisasterRequest.objects.filter(status='未发送')
        return render(request, 'dataStorage.html', {'data_list': requestlist})  # 显示数据库中的






