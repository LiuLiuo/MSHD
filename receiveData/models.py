from django.db import models


# Create your models here.
class TotalData(models.Model):
    class Meta:
        db_table = 'TotalData'

    ID = models.CharField(primary_key=True, max_length=19, default='')
    type = models.CharField(max_length=4, null=False, default='')
    detail = models.CharField(max_length=200, null=False, default='')
    MSCode = models.CharField(max_length=4, null=False, default='')


class CommDisaster(models.Model): #336 通信
    class Meta:
        db_table = 'CommDisaster'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=4, null=False, default='')
    grade = models.CharField(max_length=4, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')


class CollapseRecord(models.Model): #441 崩塌
    class Meta:
        db_table = 'CollapseRecord'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=10, null=False, default='')
    status = models.CharField(max_length=10, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')


class DeathStatistics(models.Model):#111 死亡
    class Meta:
        db_table = 'DeathStatistics'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    location = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=20, null=False)
    number = models.IntegerField(null=False)
    reporting_unit = models.TextField(max_length=20, null=False)


class CivilStructure(models.Model): #221 土木
    class Meta:
        db_table = 'CivilStructure'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=100, null=False)
    basically_intact_square = models.CharField(max_length=6, null=False)
    damaged_square = models.CharField(max_length=6, null=False)
    destroyed_square = models.CharField(max_length=6, null=False)
    note = models.CharField(max_length=200, null=False)
    reporting_unit = models.TextField(max_length=20, null=False)


class DisasterPrediction(models.Model):#552
    class Meta:
        db_table = 'DisasterPrediction'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    longitude = models.FloatField(max_length=100, default='')
    latitude = models.FloatField(max_length=100, default='')
    depth = models.FloatField(default='')
    magnitude = models.FloatField(default='')
    intensity = models.CharField(max_length=6, default='')
    type = models.CharField(max_length=2, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='')

class InjuredStatistics(models.Model):#112
    class Meta:
        db_table = 'InjuredStatistics'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    location = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=20, null=False)
    number = models.IntegerField(null=False)
    reporting_unit = models.TextField(max_length=20, null=False)

class MissingStatistics(models.Model):#113 失踪
    class Meta:
        db_table = 'MissingStatistics'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    location = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=20, null=False)
    number = models.IntegerField(null=False)
    reporting_unit = models.TextField(max_length=20, null=False)

class BrickwoodStructure(models.Model):#222 砖木
    class Meta:
        db_table = 'BrickwoodStructure'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=100, null=False)
    basically_intact_square = models.CharField(max_length=6, null=False)
    damaged_square = models.CharField(max_length=6, null=False)
    destroyed_square = models.CharField(max_length=6, null=False)
    note = models.CharField(max_length=200, null=False)
    reporting_unit = models.TextField(max_length=20, null=False)

class MasonryStructure(models.Model):#223 砖混
    class Meta:
        db_table = 'MasonryStructure'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=100, null=False)
    basically_intact_square = models.CharField(max_length=6, null=False)
    slight_damaged_square=models.CharField(max_length=6, null=False)
    moderate_damaged_square = models.CharField(max_length=6, null=False)
    serious_damaged_square = models.CharField(max_length=6, null=False)
    destroyed_square = models.CharField(max_length=6, null=False)
    note = models.CharField(max_length=200, null=False)
    reporting_unit = models.TextField(max_length=20, null=False)

class FrameworkStructure(models.Model):#224 框架
    class Meta:
        db_table = 'FrameworkStructure'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=100, null=False)
    basically_intact_square = models.CharField(max_length=6, null=False)
    slight_damaged_square = models.CharField(max_length=6, null=False)
    moderate_damaged_square = models.CharField(max_length=6, null=False)
    serious_damaged_square = models.CharField(max_length=6, null=False)
    destroyed_square = models.CharField(max_length=6, null=False)
    note = models.CharField(max_length=200, null=False)
    reporting_unit = models.TextField(max_length=20, null=False)
class OtherStructure(models.Model):#225 其他
    class Meta:
        db_table = 'OtherStructure'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=100, null=False)
    basically_intact_square = models.CharField(max_length=6, null=False)
    slight_damaged_square = models.CharField(max_length=6, null=False)
    moderate_damaged_square = models.CharField(max_length=6, null=False)
    serious_damaged_square = models.CharField(max_length=6, null=False)
    destroyed_square = models.CharField(max_length=6, null=False)
    note = models.CharField(max_length=200, null=False)
    reporting_unit = models.TextField(max_length=20, null=False)
class TrafficDisaster(models.Model):#331 交通
    class Meta:
        db_table = 'TrafficDisaster'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=4, null=False, default='')
    grade = models.CharField(max_length=4, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class WaterDisaster(models.Model):#332 供水
    class Meta:
        db_table = 'WaterDisaster'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=4, null=False, default='')
    grade = models.CharField(max_length=4, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class OilDisaster(models.Model):#333 输油
    class Meta:
        db_table = 'OilDisaster'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=4, null=False, default='')
    grade = models.CharField(max_length=4, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class GasDisaster(models.Model):#334 燃气
    class Meta:
        db_table = 'GasDisaster'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=4, null=False, default='')
    grade = models.CharField(max_length=4, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class PowerDisaster(models.Model):#335 电力
    class Meta:
        db_table = 'PowerDisaster'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=4, null=False, default='')
    grade = models.CharField(max_length=4, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')


class IrrigationDisaster(models.Model):#337 水利
    class Meta:
        db_table = 'IrrigationDisaster'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=4, null=False, default='')
    grade = models.CharField(max_length=4, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')


class LandslideRecord(models.Model):#442 滑坡
    class Meta:
        db_table = 'LandslideRecord'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=10, null=False, default='')
    status = models.CharField(max_length=10, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class DebrisRecord(models.Model):#443 泥石流
    class Meta:
        db_table = 'DebrisRecord'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=10, null=False, default='')
    status = models.CharField(max_length=10, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class KarstRecord(models.Model):#444 岩溶塌陷
    class Meta:
        db_table = 'KarstRecord'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=10, null=False, default='')
    status = models.CharField(max_length=10, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class CrackRecord(models.Model):#445 地裂缝
    class Meta:
        db_table = 'CrackRecord'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=10, null=False, default='')
    status = models.CharField(max_length=10, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class SettlementRecord(models.Model):#446 地面沉降
    class Meta:
        db_table = 'SettlementRecord'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=10, null=False, default='')
    status = models.CharField(max_length=10, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')

class OtherRecord(models.Model):#447 其他此生灾害
    class Meta:
        db_table = 'OtherRecord'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=10, null=False, default='')
    picture = models.ImageField(default='')
    note = models.TextField(max_length=200, default='')
    reporting_unit = models.TextField(max_length=50, default='202')



class DisasterInfo(models.Model): #551
    class Meta:
        db_table = 'DisasterInfo'

    ID = models.ForeignKey('TotalData', on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=20, null=False, default='')
    location = models.CharField(max_length=100, null=False, default='')
    longitude = models.FloatField(max_length=100, default='')
    latitude = models.FloatField(max_length=100, default='')
    depth = models.FloatField(default='')
    magnitude = models.FloatField(default='')
    picture = models.ImageField(default='')
    reporting_unit = models.TextField(max_length=50, default='')

class DisasterRequest(models.Model):
    class Meta:
            db_table = 'DisasterRequest'

    date = models.CharField(max_length=20, null=False, default='')
    disasterType = models.CharField(max_length=3, null=False, default='')
    status = models.CharField(max_length=10, null=False, default='')
    o_URL = models.CharField(max_length=200, null=False, default='')
    requesting = models.CharField(max_length=50, null=False, default='')

