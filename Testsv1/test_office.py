from flask import Flask,jsonify
import unittest # Importing the unittest module
import pytest
import json
from api import create_app
from api.v1.models.office_model import Office,offices # Importing the Office class


class TestOffice(unittest.TestCase):
    """This class represents the office test case"""
    
    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app('testing')
        self.client = self.app.test_client()
        
            
        self.create_office =json.dumps({
                
                "id": 1,
                "name": "iye",
                "type": "senatorial",
                
            })
        
      
    def test_create_office(self):
        '''
        method that tests create office.
        '''
        responses = self.client.post(path='/app/v1/models/offices', data = self.create_office,content_type='apilication/json')
        self.assertEqual(responses.status_code,404)
       
    def test_get_offices(self):
         self.client.post(path='/api/v1/models/offices', data=self.create_office,content_type='apilication/json')
         re=self.client.get(path='/api/v1/models/offices',content_type='apilication/json')
         self.assertEqual(re.status_code,404)

    def test_get_specific_office(self):
        self.client.post(path='/api/v1/models/offices', data=self.create_office,content_type='apilication/json')
        re=self.client.get(path='/api/v1/models/offices/2',content_type='apilication/json')
        self.assertEqual(re.status_code,404)

    def test_missing_id(self):
        self.client.post(path='/api/v1/models/offices', data=self.create_office,content_type='apilication/json')
        re=self.client.get(path='/api/v1/models/offices/5',content_type='apilication/json')
        self.assertEqual(re.status_code,404)    

    
        

    def tearDown(self):
        self.app.testing=False    
   