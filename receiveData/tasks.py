from __future__ import absolute_import,unicode_literals
from celery import task
from celery import shared_task
from celery import Celery
from celery.schedules import crontab
from django.shortcuts import render
import os,django

import pandas as pd
import numpy as np
from  receiveData.models import *  #导入模型
# Create your views here.
import json
import  time
import os

app = Celery('tasks', broker='pyamqp://guest@localhost//')

def sleeptime(hour,min,sec):  #设定时间
    return hour*3600+min*60+sec

def return_the_Location(ID_Code):
    ''' 根据从数据框中的数据转成string再截取前12位与地理位置匹配 返回字符串'''
    ID_str = to_str(ID_Code)
    ID_location_str = ID_str[0:12]    #得到前12位
   # print(ID_location_str,type(ID_location_str))
   # print(ID_location_series,type(ID_location_series))
    data = pd.read_csv(r'/root/mshd/receiveData/finallocation.csv')
    selectrow = data[data['编码'] == int(ID_location_str)]  # 匹配
    m = selectrow.具体地址
    #print(type(m))
    finallocation = to_str(m)
   # print(type(finallocation))
    return finallocation

def return_type_number(ID_Code):
    '''根据编码的第14，15位,返回类型的编码 类型；字符串'''
    #人员死亡统计表 DeathStatistics  11
    #土木结构房屋破坏统计表 CivilStructure 21
    #通信系统灾情统计表 CommDisaster  36
    #崩塌记录表 CollapseRecord 41
    #灾情预测 DisasterPrediction 52
    # ID_array = np.array(ID_Code.values)
    # ID_str = ''.join(ID_array)
    ID_str = to_str(ID_Code)
    ID_type_str = ID_str[13:15]  # 得到前12位
    return ID_type_str


def to_str(init):
    '''把数据框中数据转化为字符串形式'''
    init_array = np.array(init.values)
    init_str = ''.join('%s' %i for i in init_array)
    return init_str



#MSCode = '202' #测试用

def savetheData(MSCode):
    '''将Json中数据分类存储，并在总表中存储记录'''
    rootDir = r'/root/mshd/datafile'
    datarootDir = r'/root/mshd/datafile/data'
    logpath = os.path.join(rootDir)
    for lists in os.listdir(datarootDir):
        if(lists):
            filepath = os.path.join(datarootDir, lists)  # 扫描文件夹获取文件路径
            json_data = open(filepath, encoding='utf-8-sig').read()
            #得到文件的创建时间并转换时间信息格式
            format = '%Y-%m-%d %H:%M:%S'
            timevalue = time.localtime(os.path.getctime(filepath))
            dt = time.strftime(format, timevalue)
            # 将读取文件的信息写入log.txt
            logpath = os.path.join(rootDir, 'log.txt')
            logcontent = [
                'filename:' + lists,
                'time:' + dt,
                'size:' + str(os.path.getsize(filepath)),
                '文件中包含的灾情种类:\n'
            ]
            log = open(logpath, 'a+')
            log.writelines('\n'.join(logcontent))
            data = json.loads(json_data)  # 取出json中数据
            # 获取公共数据
            Common_data = pd.DataFrame(data)[['Code', 'Location', 'Date', 'Reporting_unit']]
            # 获取细节整体
            detail_total = pd.DataFrame(data)[['Detail']]
            # 获取不同类型灾难的细节
            Detail_data = pd.DataFrame([detail['Detail'] for detail in data])
            # 获取数据长度
            data_number = len(Common_data)

            # 循环读入
            for n in range(0, data_number):
                ID = Common_data.loc[n, ['Code']]
                ID_location_str = return_the_Location(ID)  # ID编码的字符串
                ID_type_str = return_type_number(ID)  # 类型的字符串
                detail_array = np.array(detail_total.iloc[n, [0]].values)
                detail_str = ''.join('%s' % i for i in detail_array)  # 细节字段总体的字符串

                def Type_11_save():
                    '''把人员伤亡信息保存人员伤亡表里'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    number_str = to_str(Detail_data.loc[n, ['Number']])
                    number_int = int(round(float(number_str)))
                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str

                    }

                    dic_11 = {  # 存储人员伤亡表数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'number': number_int,

                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    DeathStatistics.objects.create(**dic_11, ID=total)  # 保存在人员伤亡表

                    # print('1:',Death.ID.detail)  #通过属性访问总表模型
                    # print(Death.ID_id)        #其实就是加了隐藏得属性ID_id
                    log.writelines("人员死亡信息已保存\n")

                def Type_12_save():
                    '''把人员受伤信息保存人员伤亡表里'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    number_str = to_str(Detail_data.loc[n, ['Number']])
                    number_int = int(round(float(number_str)))
                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str

                    }

                    dic_12 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'number': number_int,

                    }
                    total = TotalData.objects.create(**dic_total)
                    InjuredStatistics.objects.create(**dic_12, ID=total)

                    log.writelines("人员受伤信息已保存\n")


                def Type_13_save():
                    '''把人员死亡信息保存人员伤亡表里'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    number_str = to_str(Detail_data.loc[n, ['Number']])
                    number_int = int(round(float(number_str)))
                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str

                    }

                    dic_13 = {  # 存储人员伤亡表数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'number': number_int,

                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    MissingStatistics.objects.create(**dic_13, ID=total)  # 保存在人员伤亡表

                    log.writelines("人员失踪信息已保存\n")

                def Type_21_save():
                    '''把土木结构房屋破坏信息信息保存在CivilStructure表里'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    basically_intact_square = to_str(Detail_data.loc[n, ['Basically_intact_square']])
                    damaged_square = to_str(Detail_data.loc[n, ['Damaged_square']])
                    destroyed_square = to_str(Detail_data.loc[n, ['Destroyed_square']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_21 = {  # 存储土木结构房屋破坏表数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'basically_intact_square': basically_intact_square,
                        'damaged_square': damaged_square,
                        'destroyed_square': destroyed_square,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    CivilStructure.objects.create(**dic_21, ID=total)  # 保存土木房屋破坏表中
                    log.writelines("土木结构房屋破坏信息保存\n")


                def Type_22_save():
                    '''砖木结构房屋破坏信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    basically_intact_square = to_str(Detail_data.loc[n, ['Basically_intact_square']])
                    damaged_square = to_str(Detail_data.loc[n, ['Damaged_square']])
                    destroyed_square = to_str(Detail_data.loc[n, ['Destroyed_square']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_22 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'basically_intact_square': basically_intact_square,
                        'damaged_square': damaged_square,
                        'destroyed_square': destroyed_square,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  #
                    BrickwoodStructure.objects.create(**dic_22, ID=total)  #
                    log.writelines("砖木结构房屋破坏信息保存\n")

                def Type_23_save():
                    '''砖混结构房屋破坏信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    basically_intact_square = to_str(Detail_data.loc[n, ['Basically_intact_square']])
                    slight_damaged_square = to_str(Detail_data.loc[n, ['Slight_damaged_square']])
                    moderate_damaged_square = to_str(Detail_data.loc[n, ['Moderate_damaged_square']])
                    serious_damaged_square = to_str(Detail_data.loc[n, ['Serious_damaged_square']])
                    destroyed_square = to_str(Detail_data.loc[n, ['Destroyed_square']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_23 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'basically_intact_square': basically_intact_square,
                        'slight_damaged_square': slight_damaged_square,
                        'moderate_damaged_square': moderate_damaged_square,
                        'serious_damaged_square': serious_damaged_square,
                        'destroyed_square': destroyed_square,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  #
                    MasonryStructure.objects.create(**dic_23, ID=total)  #
                    log.writelines("砖混结构房屋破坏信息保存\n")

                def Type_24_save():
                    '''框架结构房屋破坏信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    basically_intact_square = to_str(Detail_data.loc[n, ['Basically_intact_square']])
                    slight_damaged_square = to_str(Detail_data.loc[n, ['Slight_damaged_square']])
                    moderate_damaged_square = to_str(Detail_data.loc[n, ['Moderate_damaged_square']])
                    serious_damaged_square = to_str(Detail_data.loc[n, ['Serious_damaged_square']])
                    destroyed_square = to_str(Detail_data.loc[n, ['Destroyed_square']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_24 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'basically_intact_square': basically_intact_square,
                        'slight_damaged_square': slight_damaged_square,
                        'moderate_damaged_square': moderate_damaged_square,
                        'serious_damaged_square': serious_damaged_square,
                        'destroyed_square': destroyed_square,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  #
                    FrameworkStructure.objects.create(**dic_24, ID=total)  #
                    log.writelines("框架结构房屋破坏信息保存\n")

                def Type_25_save():
                    '''其他结构房屋破坏信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    basically_intact_square = to_str(Detail_data.loc[n, ['Basically_intact_square']])
                    slight_damaged_square = to_str(Detail_data.loc[n, ['Slight_damaged_square']])
                    moderate_damaged_square = to_str(Detail_data.loc[n, ['Moderate_damaged_square']])
                    serious_damaged_square = to_str(Detail_data.loc[n, ['Serious_damaged_square']])
                    destroyed_square = to_str(Detail_data.loc[n, ['Destroyed_square']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_25 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'basically_intact_square': basically_intact_square,
                        'slight_damaged_square': slight_damaged_square,
                        'moderate_damaged_square': moderate_damaged_square,
                        'serious_damaged_square': serious_damaged_square,
                        'destroyed_square': destroyed_square,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  #
                    OtherStructure.objects.create(**dic_25, ID=total)  #
                    log.writelines("其他结构房屋破坏信息保存\n")

                def Type_31_save():
                    '''交通系统灾情信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    grade = to_str(Detail_data.loc[n, ['Grade']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_31 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'grade': grade,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    TrafficDisaster.objects.create(**dic_31, ID=total)  #
                    log.writelines("交通系统灾情信息已保存\n")

                def Type_32_save():
                    '''供水系统灾情信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    grade = to_str(Detail_data.loc[n, ['Grade']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_32 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'grade': grade,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    WaterDisaster.objects.create(**dic_32, ID=total)  #
                    log.writelines("供水系统灾情信息已保存\n")

                def Type_33_save():
                    '''系统灾情信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    grade = to_str(Detail_data.loc[n, ['Grade']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_33 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'grade': grade,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    OilDisaster.objects.create(**dic_33, ID=total)  #
                    log.writelines("输油系统灾情信息已保存\n")

                def Type_34_save():
                    '''系统灾情信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    grade = to_str(Detail_data.loc[n, ['Grade']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_34 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'grade': grade,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    GasDisaster.objects.create(**dic_34, ID=total)  #
                    log.writelines("燃气系统灾情信息已保存\n")

                def Type_35_save():
                    '''系统灾情信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    grade = to_str(Detail_data.loc[n, ['Grade']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_35 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'grade': grade,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    PowerDisaster.objects.create(**dic_35, ID=total)  #
                    log.writelines("电力系统灾情信息已保存\n")

                def Type_36_save():
                    '''把通信系统灾情信息信息保存在CommDisaster表里'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    grade = to_str(Detail_data.loc[n, ['Grade']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_36 = {  # 存储通信系统灾情破坏表数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'grade': grade,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    CommDisaster.objects.create(**dic_36, ID=total)  # 保存通信系统灾情表
                    log.writelines("通信系统灾情信息已保存\n")

                def Type_37_save():
                    '''系统灾情信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    grade = to_str(Detail_data.loc[n, ['Grade']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_37 = {
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'grade': grade,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    IrrigationDisaster.objects.create(**dic_37, ID=total)  #
                    log.writelines("水利系统灾情信息已保存\n")

                def Type_41_save():
                    '''把崩塌记录信息信息保存在CollapseRecord表里'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    status = to_str(Detail_data.loc[n, ['Status']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_41 = {  # 存储崩塌记录数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'status': status,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    CollapseRecord.objects.create(**dic_41, ID=total)  # 保存
                    log.writelines("崩塌记录信息已保存\n")

                def Type_42_save():
                    '''记录信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    status = to_str(Detail_data.loc[n, ['Status']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_42 = {  # 存储崩塌记录数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'status': status,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    LandslideRecord.objects.create(**dic_42, ID=total)  # 保存表
                    log.writelines("滑坡记录信息已保存\n")

                def Type_43_save():
                    '''记录信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    status = to_str(Detail_data.loc[n, ['Status']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_43 = {  # 存储崩塌记录数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'status': status,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    DebrisRecord.objects.create(**dic_43, ID=total)  # 保存表
                    log.writelines("泥石流记录信息已保存\n")

                def Type_44_save():
                    '''记录信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    status = to_str(Detail_data.loc[n, ['Status']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_44 = {  # 存储崩塌记录数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'status': status,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    KarstRecord.objects.create(**dic_44, ID=total)  # 保存表
                    log.writelines("岩溶塌陷记录信息已保存\n")

                def Type_45_save():
                    '''记录信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    status = to_str(Detail_data.loc[n, ['Status']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_45 = {  # 存储崩塌记录数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'status': status,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    CrackRecord.objects.create(**dic_45, ID=total)  # 保存表
                    log.writelines("地裂缝记录信息已保存\n")

                def Type_46_save():
                    '''记录信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    status = to_str(Detail_data.loc[n, ['Status']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_46 = {  # 存储崩塌记录数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'status': status,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    SettlementRecord.objects.create(**dic_46, ID=total)  # 保存表
                    log.writelines("地面沉降记录信息已保存\n")

                def Type_47_save():
                    '''记录信息信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_47 = {  # 存储崩塌记录数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'type': type,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    OtherRecord.objects.create(**dic_47, ID=total)  # 保存表
                    log.writelines("其他次生灾害记录信息已保\n")

                def Type_51_save():
                    '''基本震情信息'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    longitude = to_str(Detail_data.loc[n, ['Longitude']])
                    latitude = to_str(Detail_data.loc[n, ['Latitude']])
                    depth = to_str(Detail_data.loc[n, ['Depth']])
                    magnitude = to_str(Detail_data.loc[n, ['Magnitude']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_51 = {  # 存储灾情预测表数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'longitude': float(longitude),
                        'latitude': float(latitude),
                        'depth': float(depth),
                        'magnitude': float(magnitude),
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    DisasterPrediction.objects.create(**dic_51, ID=total)  # 保存表
                    log.writelines("基本震情信息已保存\n")

                def Type_52_save():
                    '''把灾情预测信息信息保存在DisasterPrediction表里'''
                    ID_str = to_str(Common_data.loc[n, ['Code']])
                    location_str = ID_location_str
                    date_str = to_str(Common_data.loc[n, ['Date']])
                    ru_str = MSCode + to_str(Common_data.loc[n, ['Reporting_unit']])
                    longitude = to_str(Detail_data.loc[n, ['Longitude']])
                    latitude = to_str(Detail_data.loc[n, ['Latitude']])
                    depth = to_str(Detail_data.loc[n, ['Depth']])
                    magnitude = to_str(Detail_data.loc[n, ['Magnitude']])
                    intensity = to_str(Detail_data.loc[n, ['Intensity']])
                    picture = to_str(Detail_data.loc[n, ['Picture']])
                    type = to_str(Detail_data.loc[n, ['Type']])
                    note = to_str(Detail_data.loc[n, ['Note']])

                    dic_total = {  # 存储总表数据
                        'ID': ID_str,
                        'type': ID_type_str,
                        'detail': detail_str
                    }

                    dic_52 = {  # 存储灾情预测表数据
                        'location': location_str,
                        'date': date_str,
                        'reporting_unit': ru_str,
                        'longitude': float(longitude),
                        'latitude': float(latitude),
                        'depth': float(depth),
                        'magnitude': float(magnitude),
                        'intensity': intensity,
                        'type': type,
                        'picture': picture,
                        'note': note,
                    }
                    total = TotalData.objects.create(**dic_total)  # 先把数据在总表保存
                    DisasterPrediction.objects.create(**dic_52, ID=total)  # 保存表
                    log.writelines("灾情预测信息已保存\n")

                def default():
                    log.writelines("don't have this type\n")

                switch = {  # 根据编码中的灾情种类编码分别存储
                    '11': Type_11_save,
                    '12': Type_12_save,
                    '13': Type_13_save,
                    '21': Type_21_save,
                    '22': Type_22_save,
                    '23': Type_23_save,
                    '24': Type_24_save,
                    '25': Type_25_save,
                    '31': Type_31_save,
                    '32': Type_32_save,
                    '33': Type_33_save,
                    '34': Type_34_save,
                    '35': Type_35_save,
                    '36': Type_36_save,
                    '37': Type_37_save,
                    '41': Type_41_save,
                    '42': Type_42_save,
                    '43': Type_43_save,
                    '44': Type_44_save,
                    '45': Type_45_save,
                    '46': Type_46_save,
                    '47': Type_47_save,
                    '51': Type_51_save,
                    '52': Type_52_save,
                }
                switch.get(ID_type_str)()

            log.writelines("所有数据存储完成\n--------------------------------------------\n")
            log.close()
            os.remove(filepath)
        else:
            break
    return

@shared_task
def main(MSCode):
    #MSCode = '202'
    os.system(r'python /root/mshd/manage.py dumpdata --format=xml receiveData> /root/mshd/datafile/back_up.xml')  # 运行命令行，将数据库文件备份到指定路径
    savetheData(MSCode)#读取文件进行存储
    return

