from django.test import TestCase, Client
import unittest

class ExploreTest(unittest.TestCase):
    def SetUp(self):
        self.client = Client()

    def test_details(self):
        response1 = self.client.get('http://127.0.0.1:8000/disasterType/')
        self.assertEqual(response1.status_code, 200)

        #错误url测试
        response2 = self.client.get('http://127.0.0.1:8000/DeathStatistics123/')
        self.assertEqual(response2.status_code, 200)

        response3 = self.client.get('http://127.0.0.1:8000/CivilStructure/')
        self.assertEqual(response3.status_code, 200)

        response4 = self.client.get('http://127.0.0.1:8000/disasterType/')
        self.assertEqual(response4.status_code, 200)

        response5 = self.client.get('http://127.0.0.1:8000/disasterType/')
        self.assertEqual(response5.status_code, 200)

        response6 = self.client.get('http://127.0.0.1:8000/disasterType/')
        self.assertEqual(response6.status_code, 200)




# Create your tests here.
