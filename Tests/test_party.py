from flask import Flask,jsonify
import unittest # Importing the unittest module
import pytest
import json
from app import create_app
from app.v1.models.party_model import Createparty # Importing the Office class


class TestCreateparty(unittest.TestCase):
    """This class represents the office test case"""
    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app('testing')
        self.client = self.app.test_client()
        
            
        self.create_party =json.dumps({
                
                "id": 1,
                "name": "odm",
                "hqAddress": "nairobi",
                "logoUrl":"image"
            })
        
      
    
   

    def test_create_party(self):
        '''
        method that tests create party.
        '''
        responses = self.client.post(path='/app/v1/models/parties', data = self.create_party,content_type='application/json')
        self.assertEqual(responses.status_code,404)
       
    def test_get_parties(self):
         self.client.post(path='/app/v1/models/parties', data=self.create_party,content_type='application/json')
         re=self.client.get(path='/app/v1/models/parties',content_type='application/json')
         self.assertEqual(re.status_code,404)
        

    def tearDown(self):
        self.app.testing=False    
    # def tearDown(self):
    #     """teardown all initialized variables."""
    #     with self.app.app_context():
    #     parties.clear() 
    