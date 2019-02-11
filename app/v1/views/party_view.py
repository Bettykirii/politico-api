from flask import Blueprint, jsonify, request
from app.v1.models.party_model import Createparty

b_party= Blueprint("v1", __name__, url_prefix="/app/v1")

   

@b_party.route('/parties', methods=['POST'])
def create_party():
    global Createparty
        if request.method == "POST":
             data = request.get_json(force=True)
             create_party = Createparty(partydata)
        if not(partydata) 
                return response = jsonify({
                "status": "400",
                "error": "enter valid party data"
            }), 400
        elif len(party) < 4:
        return response(jsonify({
            "error": "You should have four fields",
            "status": 400
        }), 400)
       
    response = create_party(partydata)
    return response(jsonify({
        'message': 'Party created successfully',
        'status': 201,
        'data': responses
    }), 201)

@b_party.route('/parties', methods=['GET'])
def get_parties():
    '''
    method for getting all parties
    '''
    party_all = Createparty().get_parties()
    return response(jsonify({
        'message': 'list of all parties',
        'status': 200,
        'data':all_parties
    }), 200)

@b_party.route('/parties/<int:p_id>/',, methods=['FETCH'])
def edit_party(id):
    '''
    method for editing a party
    '''
    party_data=request.get_json()
    if 'id' not in party_data :
        return make_response(jsonify({
            'message': ' invalid request',
            'status': 400
            }), 400)
    elif id(party_data)
        return response(jsonify({
            "message": "updated party details",
            "status": 202
        }), 202)
@b_party.route('/parties/<int:p_id>/', methods=['DELETE'])
def delete_party(p_id):
    '''
    method for deleting party by id
    '''
    Createparty().delete_party(p_id)
    return response(jsonify({
        'status': 'OK',
        'message': 'successfully deleted'
    }), 202)

@b_party.route('/parties/<int:p_id>', methods=['GET'])
def specific_party(p_id):
    '''
    method for getting a specific party
    '''
    specific_party = Createparty().get_specific_party(p_id)
    if specific_party:
        return response(jsonify({
            'message': 'party id successfully retrieved',
            'Status': 200,
            'parties': specific_party
        }), 200)
    return response(jsonify({
        'status': 404,
        'message': 'party not found'
    }), 404)   