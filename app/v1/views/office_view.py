from flask import Blueprint, jsonify, request,make_response
from app.v1.models.office_model import Office,offices
import ast
import json

b_v1= Blueprint("v1", __name__, url_prefix="/app/v1")

   

@b_v1.route('/offices', methods=['POST'])
def create_office():
    '''
    method for getting all offices
    '''
    json_data=request.get_json(force=True)
    id=len(offices)+1
    if json_data:
        office_name=json_data['name']
        office_type=json_data['type']
        
    new_office = {
            "office_id": id,
            "office_name": office_name,
            "office_type": office_type,
            
        }

    offices.append(new_office)
    return make_response(jsonify({
            "status":201,
            "data":[new_office]
        }),201)
    

@b_v1.route('/offices', methods=['GET'])
def get_offices():
    '''
    method for getting all offices
    '''

    
    return make_response(jsonify({
        'message': 'list of all offices',
        'status': 200,
        'data':offices
    }), 200)


@b_v1.route('/offices/<officeID>',methods=['GET'])
def getOffice(officeID):
   try:
       for office in offices:
           print(type(office["id"]))
           if office["id"] == int(officeID):
               return make_response(jsonify(office), 200)

       return make_response(jsonify({
           "code": 404,
           "message": "Could not find office with id {} kindly check it again".format(officeID)
       }), 404)
   except:
       return jsonify({"status": 200}, {"message": "You have retrieved ID "})


if __name__ =='__main__':
    b.route.run(debug=True)   