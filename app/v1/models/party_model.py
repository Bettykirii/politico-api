parties=[]
import time


class Createparty():
    """This class represents the createparty table."""

    def __init__(self,id):
        id=len(parties)+1
        self.party_name=party_name
        self.hqAddress=hqAddress
        self.logoUrl=logoUrl

    def create_party(self):
         '''
         Args:
            name: New party name.
            hqAddress : New party hqAddress.
            logoUrl: New party logoUrl
        '''
         new_party = {
            "id": self.id,
            "name": self.party_name,
            "hqAddress":self.hqAddress,
            "logoUrl": self.logoUrl,
        }
         return parties.append(new_party)
        
    
    def get_parties(self):
        return self.all_parties

    def create_party(self,id, name, hqAddress, logoUrl):
       

       

        self.all_parties.append(new_party)
        return self.all_parties

    def get_specific_party(self, id):
        '''
         Args:
            party_id: specific id of a party.
            
        '''
        if self.all_parties:
            for spec_party in self.all_parties:
                if spec_party.get('party_id') == id:

                    return spec_party
    def delete_party(self,id):
        for party in parties:
            if party['id'] == id:
                parties.remove(party)
   