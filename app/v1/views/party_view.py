from flask import Blueprint, jsonify, request,make_response
from app.v1.models.party_model import Createparty,parties

import json

b= Blueprint("b1", __name__, url_prefix="/app/v1")

   

@b.route('/parties', methods=['POST'])
def create_party():
    '''
    method for creating all parties
    '''
    json_data=request.get_json(force=True)
    id=len(parties)+1
    if json_data:
        party_name=json_data['name']
        hqAddress=json_data['hqAddress']
        logoUrl=json_data['logoUrl']
        
     
        new_party = {
            "party_id": id,
            "party_name": party_name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl,
        }

        parties.append(new_party)
        return make_response(jsonify({
            "status":201,
            "data":[new_party]
        }),201)
    

  

@b.route('/parties', methods=['GET'])
def get_parties():
    '''
    method for getting all parties
    '''

   
    return make_response(jsonify({
        'message': 'list of all parties',
        'status': 200,
        'data':parties
    }), 200)

@b.route('/parties/<partyID>',methods=['GET'])
def get_specific_party(partyID):
     
    # '''
    # method for getting a specific party by ID 

    # '''
   try:
       for party in parties:
           print(type(party["id"]))
           if party["id"] == int(partyID):
               return make_response(jsonify(party), 200)

       return make_response(jsonify({
           "code": 404,
           "message": "Could not find office with id {} kindly check it again".format(partyID)
       }), 404)
   except:
       return jsonify({"status": 200}, {"message": "You have retrieved party ID "})

@b.route('/parties/<partyID>',methods=['PATCH'])
def edit_specific_party(partyID):
    # '''
    # method for editing a specific party
    # '''
   try:
       for party in parties:
           print(type(party["id"]))
           if party["id"] == int(partyID):
               return make_response(jsonify(party), 200)

       return make_response(jsonify({
           "code": 404,
           "message": "Could not find office with id {} kindly check it again".format(partyID)
       }), 404)
   except:
       return jsonify({"status": 200}, {"message": "You have updated succesfully party with id "})


    
@b.route('/parties/<partyID>',methods=['DELETE'])
def delete_specific_party(partyID):
   try:
       for party in parties:
           print(type(party["id"]))
           if party["id"] == int(partyID):
               return make_response(jsonify(party), 200)

       return make_response(jsonify({
           "code": 404,
           "message": "Could not delete office with id {} kindly check it again".format(partyID)
       }), 404)
   except:
       return jsonify({"status": 200}, {"message": "You have deleted succesfully party with id "})

if __name__ =='__main__':
    b.route.run(debug=True)  