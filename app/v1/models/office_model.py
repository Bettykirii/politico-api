import time



class Office():
    """This class represents the class office."""

    def __init__(self, partydata):
        self.partydata = partydata
def get_offices(self):
        return self.all_offices

    def create_office(self, office_type, office_name):
        '''
         Args:
            name: New office name.
            type : New office type.
        '''
        
        new_office = {
            "office_id": len(self.all_offices)+1,
            "office_name": office_name,
            "office_type": office_type
        }

        self.all_offices.append(new_office)
        return self.all_offices

    def get_specific_office(self, office_id):
        '''
            Args:
            office_id: specific id of a office.
            
        '''
        if self.all_offices:
            for spec_office in self.all_offices:
                if spec_office.get('office_id') == office_id:

                    return spec_office
