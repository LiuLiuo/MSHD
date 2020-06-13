from django.shortcuts import render
from receiveData.models import *


def disasterType(request):
    return render(request,'disasterType.html')

def deathStatistics(request):
    deathStatistics = DeathStatistics.objects.all()
    return render(request, 'deathStatistics.html', {'deathStatistics': deathStatistics})

def  civilStructure (request):
    civilStructures = CivilStructure.objects.all()
    return render(request, 'civilStructure.html', {'civilStructures': civilStructures})

def commDisaster (request):
    commDisasters = CommDisaster.objects.all()
    return render(request, 'commDisaster.html', {'commDisasters': commDisasters})

def collapseRecord (request):
    collapseRecords = CollapseRecord.objects.all()
    return render(request, 'collapseRecord.html', {'collapseRecords': collapseRecords})

def disasterPrediction (request):
    disasterPredictions = DisasterPrediction.objects.all()
    return render(request, 'disasterPrediction.html', {'disasterPredictions': disasterPredictions})

def injuredStatistic (request):
    injuredStatistics = InjuredStatistics.objects.all()
    return render(request, 'injuredStatistic.html', {'injuredStatistics': injuredStatistics})

def missingStatistic (request):
    missingStatistics = MissingStatistics.objects.all()
    return render(request, 'missingStatistic.html', {'missingStatistics': missingStatistics})

def brickwoodStructure (request):
    brickwoodStructures = BrickwoodStructure.objects.all()
    return render(request, 'brickwoodStructure.html', {'brickwoodStructures': brickwoodStructures})

def masonryStructure (request):
    masonryStructures = MasonryStructure.objects.all()
    return render(request, 'masonryStructure.html', {'masonryStructures': masonryStructures})

def frameworkStructure (request):
    frameworkStructures = FrameworkStructure.objects.all()
    return render(request, 'frameworkStructure.html', {'frameworkStructures': frameworkStructures})

def otherStructure (request):
    otherStructures = OtherStructure.objects.all()
    return render(request, 'otherStructure.html', {'otherStructures': otherStructures})

def trafficDisaster (request):
    trafficDisasters = TrafficDisaster.objects.all()
    return render(request, 'trafficDisaster.html', {'trafficDisasters': trafficDisasters})

def oilDisaster (request):
    oilDisasters = OilDisaster.objects.all()
    return render(request, 'oilDisaster.html', {'oilDisasters': oilDisasters})

def waterDisaster (request):
    waterDisasters = WaterDisaster.objects.all()
    return render(request, 'waterDisaster.html', {'waterDisasters': waterDisasters})

def gasDisaster (request):
    gasDisasters = GasDisaster.objects.all()
    return render(request, 'gasDisaster.html', {'gasDisasters': gasDisasters})

def powerDisaster (request):
    powerDisasters = PowerDisaster.objects.all()
    return render(request, 'powerDisaster.html', {'powerDisasters': powerDisasters})

def irrigationDisaster (request):
    irrigationDisasters = IrrigationDisaster.objects.all()
    return render(request, 'irrigationDisaster.html', {'irrigationDisasters': irrigationDisasters})

def landslideRecord (request):
    landslideRecords = LandslideRecord.objects.all()
    return render(request, 'landslideRecord.html', {'landslideRecords': landslideRecords})

def debrisRecord (request):
    debrisRecords = DebrisRecord.objects.all()
    return render(request, 'debrisRecord.html', {'debrisRecords': debrisRecords})

def karstRecord (request):
    karstRecords = KarstRecord.objects.all()
    return render(request, 'karstRecord.html', {'karstRecords': karstRecords})

def crackRecord (request):
    crackRecords = CrackRecord.objects.all()
    return render(request, 'crackRecord.html', {'crackRecords': crackRecords})

def settlementRecord (request):
    settlementRecords = SettlementRecord.objects.all()
    return render(request, 'settlementRecord.html', {'settlementRecords': settlementRecords})

def otherRecord (request):
    otherRecords = OtherRecord.objects.all()
    return render(request, 'otherRecord.html', {'otherRecords': otherRecords})

def disasterInfo (request):
    disasterInfos = DisasterInfo.objects.all()
    return render(request, 'disasterInfo.html', {'': disasterInfos})

def search (request):
    q = request.GET.get('keyword')

    if('死亡' in q):
        deathStatistics = DeathStatistics.objects.all()
        return render(request, 'deathStatistics.html', {'deathStatistics': deathStatistics})
    elif '失踪' in q:
        missingStatistics = MissingStatistics.objects.all()
        return render(request, 'missingStatistic.html', {'missingStatistics': missingStatistics})
    elif '受伤' in q:
        injuredStatistics = InjuredStatistics.objects.all()
        return render(request, 'injuredStatistic.html', {'injuredStatistics': injuredStatistics})
    elif '土木' in q:
        civilStructures = CivilStructure.objects.all()
        return render(request, 'civilStructure.html', {'civilStructures': civilStructures})
    elif '砖木' in q:
        brickwoodStructures = BrickwoodStructure.objects.all()
        return render(request, 'brickwoodStructure.html', {'brickwoodStructures': brickwoodStructures})
    elif '砖混' in q:
        masonryStructures = MasonryStructure.objects.all()
        return render(request, 'masonryStructure.html', {'masonryStructures': masonryStructures})
    elif '框架' in q:
        frameworkStructures = FrameworkStructure.objects.all()
        return render(request, 'frameworkStructure.html', {'frameworkStructures': frameworkStructures})
    elif '房屋破坏其他' in q:
        otherStructures = OtherStructure.objects.all()
        return render(request, 'otherStructure.html', {'otherStructures': otherStructures})
    elif '交通' in q:
        trafficDisasters = TrafficDisaster.objects.all()
        return render(request, 'trafficDisaster.html', {'trafficDisasters': trafficDisasters})
    elif '供水' in q:
        waterDisasters = WaterDisaster.objects.all()
        return render(request, 'waterDisaster.html', {'waterDisasters': waterDisasters})
    elif '输油' in q:
        oilDisasters = OilDisaster.objects.all()
        return render(request, 'oilDisaster.html', {'oilDisasters': oilDisasters})
    elif '燃气' in q:
        gasDisasters = GasDisaster.objects.all()
        return render(request, 'gasDisaster.html', {'gasDisasters': gasDisasters})
    elif '电力' in q:
        powerDisasters = PowerDisaster.objects.all()
        return render(request, 'powerDisaster.html', {'powerDisasters': powerDisasters})
    elif '通信' in q:
        commDisasters = CommDisaster.objects.all()
        return render(request, 'commDisaster.html', {'commDisasters': commDisasters})
    elif '水利' in q:
        irrigationDisasters = IrrigationDisaster.objects.all()
        return render(request, 'irrigationDisaster.html', {'irrigationDisasters': irrigationDisasters})
    elif '崩塌' in q:
        collapseRecords = CollapseRecord.objects.all()
        return render(request, 'collapseRecord.html', {'collapseRecords': collapseRecords})
    elif '滑坡' in q:
        landslideRecords = LandslideRecord.objects.all()
        return render(request, 'landslideRecord.html', {'landslideRecords': landslideRecords})
    elif '泥石流' in q:
        debrisRecords = DebrisRecord.objects.all()
        return render(request, 'debrisRecord.html', {'debrisRecords': debrisRecords})
    elif '岩溶塌陷' in q:
        karstRecords = KarstRecord.objects.all()
        return render(request, 'karstRecord.html', {'karstRecords': karstRecords})
    elif '地裂缝' in q:
        crackRecords = CrackRecord.objects.all()
        return render(request, 'crackRecord.html', {'crackRecords': crackRecords})
    elif '地面沉降' in q:
        settlementRecords = SettlementRecord.objects.all()
        return render(request, 'settlementRecord.html', {'settlementRecords': settlementRecords})
    elif '次生灾害其他' in q:
        otherRecords = OtherRecord.objects.all()
        return render(request, 'otherRecord.html', {'otherRecords': otherRecords})
    elif '基本震情' in q:
        disasterInfos = DisasterInfo.objects.all()
        return render(request, 'disasterInfo.html', {'': disasterInfos})
    elif '灾情预测' in q:
        disasterPredictions = DisasterPrediction.objects.all()
        return render(request, 'disasterPrediction.html', {'disasterPredictions': disasterPredictions})
    else:
        return render(request,'search_error.html')





# Create your views here.
