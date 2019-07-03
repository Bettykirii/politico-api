from flask import Blueprint, jsonify, request,make_response
from api.v1.models.party_model import Createparty,parties

import json

b= Blueprint("b1", __name__, url_prefix="/api/v1")

   

@b.route('/parties', methods=['POST'])
def create_party():
    '''
    method for creating all parties
    '''
    json_data = request.get_json(force=True)
    id = len(parties)+1
    if json_data:
        if (json_data['party_name'] is not "") and (json_data["hqAddress"] is not "") and (json_data["logoUrl"] is not ""):
          
            party_name = json_data["party_name"]
            hqAddress = json_data["hqAddress"]
            logoUrl=json_data["logoUrl"]
            if isinstance(party_name,str) and isinstance(hqAddress,str) and isinstance(logoUrl,str):
                for  party in parties:
                    if party['party_name'] !=party_name and party['logoUrl'] !=logoUrl:
                       continue
                    else:
                        return jsonify({
                        "error":"Party already exists",
                        "status":409
                    }),409



            new_party = {
                "id":id,
                "party_name":party_name,
                "hqAddress":hqAddress,
                "logoUrl":logoUrl,
            }

            parties.append(new_party)

            return make_response(jsonify({
                "status": 201,
                "data": [new_party]
            }), 201)
        else:
            return make_response(jsonify({
                            "status":401,
                            "message":"Input required fields"
                        }))

  
@b.route('/parties', methods=['GET'])
def get_all_parties():
    '''
    method for getting all parties
    '''

   
    return make_response(jsonify({
        'message': 'list of all parties',
        'status': 200,
        'data':parties
    }), 200)

@b.route("/parties/<p_id>",methods=['GET'])
def get_party(p_id):
    
        id=int(p_id)
        for party in parties:
            print(type(party["id"]))

            if party["id"] == id:

                return make_response(jsonify({

                    "data": party,
                    "status": 200
                }),200)

            else:
                    return make_response(jsonify({
                        "status": 404,
                        "message": "Could not find party with id {} kindly check if it exists".format(p_id)
                    }), 404)


        return jsonify({"status":400},{"message":"Invalid party ID"})
@b.route('parties/<p_id>',methods=['PATCH'])
def party_update(p_id):
    for party in parties:
        if party ['id']==int(p_id):

            data=request.get_json()
            new_name=data['party_name']
            party['party_name']=data['party_name']
            return make_response(jsonify({
                "status":200,
                 "data":"updated  the party with party ID {} ".format(p_id)
            }),200)
       
            party_update = {
                "party_name": party['party_name']

            }
            parties.append(update_party)
            return make_response(jsonify({
                "status": 200,
                "data": [update_party]
            }), 200)

@b.route("/parties/<p_id>", methods=['DELETE'])
def delete_party(p_id):
   
       for party in parties:
           if party["id"] == int(p_id):
               parties.remove(party)
               return make_response(jsonify({
                   "status": 200,
                   "data": "deleted successfully"
               }), 200)

           return make_response(jsonify({
               "status": 404,
               "msg": "could not find party with ID {}".format(p_id)
           }), 404)
   
       return jsonify({"status": 400}, {"message": "Please enter a valid party ID to delete"})

if __name__ =='__main__':
    b.route.run(debug=True)  