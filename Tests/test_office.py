# import unittest # Importing the unittest module
# import json
# import pytest

# from app import create_app
# from app.v1.models.office_model import Office


# class TestOffice(unittest.TestCase):
#     """This class represents the office test case"""
# def setUp(self):
#        # """Define test variables and initialize app."""
#     self.app = create_app('testing')
#     self.client = self.app.test_client()
    
    
#     self.office = {
#         "type": "country",
#         "name": "presidential",
#         "id": "78",
#     }


# def test_create_office(self):
#     '''
#     method that tests create office.
#     '''
#     responses = self.client.post('/app/v1/models/Office', json = self.office)
#     data = responses.get_json()

#     self.assertEqual(data['status'], 201)
#     self.assertEqual(data['message'], 'Office added successfully')
#     self.assertEqual(responses.status_code, 201)


# def test_get_offices(self):
#     responses = self.client.post('/app/v1/model/Office', json = self.office)
    
    
#     # def tearDown(self):
#     # #"""teardown all initialized variables."""
#     # with self.app.app_context():
#     # offices.clear() 
