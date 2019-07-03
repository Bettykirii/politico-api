from flask import Blueprint, jsonify, request,make_response
from api.v1.models.office_model import Office,offices
import ast
import json

b_v1= Blueprint("v1", __name__, url_prefix="/app/v1")

   

@b_v1.route('/offices', methods=['POST'])
def create_office():
    '''
    method for getting all offices
    '''
    json_data = request.get_json(force=True)
    data=json.dumps(json_data)
    if (json_data['office_type'] is not "") and (json_data["office_name"] is not ""):
        datadict=ast.literal_eval(data)
        name=datadict['office_name']
        type=datadict['office_type']
        id = len(offices) + 1
        office_type = json_data["office_type"]
        office_name = json_data["office_name"]
        if isinstance(name,str) and isinstance(type,str):
            for office in offices:
                if office['name'] !=name and office['type'] !=type:
                    continue
                else:
                    return jsonify({
                        "error":"Office already exist",
                        "status":409
                    }),409

        new_office = {
            "id": id,
            "name": office_name,
            "type": office_type,
        }    
        print(new_office)
        offices.append(new_office)

        return make_response(jsonify({
                "status": 201,
                "data": [new_office]
            }), 201)

        # else:
        #     return jsonify({"status":404,"Message":"Enter valid data"})


    return make_response(jsonify({
        "status": 401,
        "message": "Missing required fields"
    }))

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
   
        for office in offices:
            print(type(office["id"]))
            if office["id"] == int(officeID):
                return make_response(jsonify(office), 200)

        return make_response(jsonify({
            "code": 404,
            "message": "Could not find office with id {} kindly check it again".format(officeID)
        }), 404)
  
        return jsonify({"status": 400}, {"message": "You have entered invalid office ID"})

if __name__ =='__main__':
    b.route.run(debug=True)   