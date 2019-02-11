from flask import Blueprint, jsonify, request
from app.v1.models.office_model import Office

b_v1= Blueprint("v1", __name__, url_prefix="/app/v1")

   

@b_v1.route('/offices', methods=['POST'])
def create_office():
    global Office
        if request.method == "POST":
             data = request.get_json(force=True)
             create_office = Office(officedata)
        if not(office) 
                return response = jsonify({
                "status": "400",
                "meesage": "enter valid office data"
            }), 400
        elif len(office) < 3:
        return response(jsonify({
            "message": "You should have three fields",
            "status": 400
        }), 400)
       
    response = create_office(officedata)
    return response(jsonify({
        'message': 'Office created successfully',
        'status': 201,
        'data': responses
    }), 201)

@b_v1.route('/offices', methods=['GET'])
def get_offices():
    '''
    method for getting all offices
    '''
    all_offices = Office()get_offices()
    return response(jsonify({
        'message': 'list of all offices',
        'status': 200,
        'data':all_offices
    }), 200)



@b_v1.route('/offices/<int:o_id>', methods=['GET'])
def specific_office(o_id):
    '''
    method for getting a specific political office
    '''
    specific_office = Office().get_specific_office(o_id)
    if specific_office:
        return response(jsonify({
            'message': 'office id successfully retrieved',
            'Status': 200,
            'offices': specific_office
        }), 200)
    return response(jsonify({
        'status': 404,
        'message': 'office not found'
    }), 404)   