
from django.db import models

# Create your models here.
# class TotalData(models.Model):
#     class Meta:
#         db_table = 'TotalData'
#
#     ID = models.CharField(primary_key=True, max_length=19, default='')
#     type = models.CharField(max_length=4, null=False, default='')
#     detail = models.CharField(max_length=200,null=False,default='')
#
# class CommDissaster(models.Model):
#     class Meta:
#         db_table = 'CommDissaster'
#
#     ID = models.ForeignKey('TotalData', on_delete=models.CASCADE,default='')
#     date = models.CharField(max_length=12,null=False,default='')
#     location = models.CharField(max_length=100,null=False,default='')
#     type = models.CharField(max_length=4, null=False, default='')
#     grade = models.CharField(max_length=4, null=False, default='')
#     picture = models.ImageField(default='')
#     note = models.TextField(max_length=200, default='')
#     reporting_unit = models.TextField(max_length=50, default='202')
#
# class CollapseRecord(models.Model):
#     class Meta:
#         db_table = 'CollapseRecord'
#
#     ID = models.ForeignKey('TotalData', on_delete=models.CASCADE,default='')
#     date = models.CharField(max_length=12, null=False, default='')
#     location = models.CharField(max_length=100, null=False, default='')
#     type = models.CharField(max_length=10, null=False, default='')
#     status = models.CharField(max_length=10, null=False, default='')
#     picture = models.ImageField(default='')
#     note = models.TextField(max_length=200, default='')
#     reporting_unit = models.TextField(max_length=50, default='202')
#
# class DeathStatistics(models.Model):
#     class Meta:
#         db_table = 'DeathStatistics'
#
#     ID = models.ForeignKey('TotalData', on_delete=models.CASCADE,default='')
#     location = models.CharField(max_length=100,null=False)
#     date = models.CharField(max_length=12,null=False)
#     number = models.IntegerField(null=False)
#     reporting_unit = models.TextField(max_length=20,null=False)
#
#
#
# class CivilStructure(models.Model):
#     class Meta:
#         db_table = 'CivilStructure'
#
#     ID = models.ForeignKey('TotalData', on_delete=models.CASCADE,default='')
#     date = models.CharField(max_length=12, null=False)
#     location = models.CharField(max_length=100, null=False)
#     basically_intact_square = models.CharField(max_length=6,null=False)
#     damaged_square = models.CharField(max_length=6,null=False)
#     destroyed_square = models.CharField(max_length=6,null=False)
#     note = models.CharField(max_length=200,null=False)
#     reporting_unit = models.TextField(max_length=20, null=False)
#
#
#
# class DisasterPrediction(models.Model):
#     class Meta:
#        db_table='DisasterPrediction'
#
#     ID = models.ForeignKey('TotalData', on_delete=models.CASCADE,default='')
#     date = models.CharField(max_length=48, null=False, default='')
#     location = models.CharField(max_length=100, null=False, default='')
#     longitude=models.FloatField(max_length=100,default='')
#     latitude = models.FloatField(max_length=100, default='')
#     depth=models.FloatField(default='')
#     magnitude=models.FloatField(default='')
#     intensity=models.CharField(max_length=6, default='')
#     type=models.CharField(max_length=2,default='')
#     picture = models.ImageField(default='')
#     note = models.TextField(max_length=200, default='')
#     reporting_unit = models.TextField(max_length=50, default='')
# class DisasterRequest(models.Model):
#     class Meta:
#        db_table='DisasterRequest'
#
#     ID = models.ForeignKey('TotalData', on_delete=models.CASCADE,default='')
#     date= models.CharField(max_length=12, null=False, default='')
#     disasterType= models.CharField(max_length=3, null=False, default='')
#     status= models.CharField(max_length=1,null=False, default='')
#     o_URL= models.CharField(max_length=200,null=False, default='')
#     requesting= models.CharField(max_length=50,null=False, default='')



