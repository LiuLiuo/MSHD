from django.test import TestCase
import pandas as pd
import numpy as np
from  receiveData.models import TotalData
from receiveData.views import savetheData
import json
class DataModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        json_data = open(r'D:\virtualpython\MSHD\receiveData\data.json', encoding='utf-8-sig').read()
        data = json.loads(json_data)  # 取出json中数据
        # 获取公共数据
        Common_data = pd.DataFrame(data)[['Code', 'Location', 'Date', 'ReportingUnit']]
        # 获取不同类型灾难的细节
        Detail_data = pd.DataFrame([detail['Detail'] for detail in data])
        #Common_data['Code'].astype(str)
        ID = np.array(Common_data.loc[0, ['Code']].values,dtype=np.str)
        TotalData_item = TotalData()
       # TotalData_item.ID = ID
        TotalData_item.ID = '1234564000010010001'
        TotalData_item.type='1'
        TotalData_item.save()

        save_items = TotalData.objects.all()
        first_save_item = save_items[0]
        self.assertEqual(first_save_item.ID,'1234564000010010001')
