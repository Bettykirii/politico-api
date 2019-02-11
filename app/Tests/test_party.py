mport unittest # Importing the unittest module
import json
from app import create_app
from app.api.version1.models.party_models import Party, parties # Importing the Office class


class TestParty(unittest.TestCase):
    """This class represents the office test case"""
    def setUp(self):
         """Define test variables and initialize app."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
       
        
        self.office = {
            "name": "odm",
            "hqAddress": "nairobi",
            "logoUrl":"image"
        }
        
      
    
    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
        parties.clear() 


    def test_create_party(self):
        '''
        method that tests create party.
        '''
        responses = self.client.post('/app/v1/models/parties', json = self.office)
        data = responses.get_json()

        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Party added successfully')
        self.assertEqual(responses.status_code, 201)

    def test_get_parties(self):
        responses = self.client.post('/app/v1/models/parties', json = self.office)
        