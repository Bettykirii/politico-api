from flask import make_response, jsonify, Blueprint,request
from app.v1.models.office_model import offices
b_v1= Blueprint('v1', __name__, url_prefix='/app/v1')
import ast
import json

@b_v1.route('/politico', methods=['GET'])
def home():
   make_response(jsonify({
       "status": 200,
       "message": "Politico enables citizens give their mandate to the type of leaders they need "


   }), 200)

@b_v1.route("/offices",methods=['GET'])
def get_all_offices():
   return make_response(jsonify(offices), 200)


@b_v1.route("/offices/<officeID>",methods=['GET'])
## this is a method to get a specific office
def get_offices(officeID):
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
       return jsonify({"status": 400}, {"message": "You have entered invalid office ID"})




@b_v1.route("/offices", methods=['POST'])
def create_office():
   json_data = request.get_json(force=True)
   data=json.dumps(json_data)
   if (json_data['type'] is not "") and (json_data["name"] is not ""):
       datadict=ast.literal_eval(data)
       name=datadict['name']
       type=datadict['type']
       if isinstance(name,str) and isinstance(type,str):
           id = len(offices) + 1
           office_type = json_data["type"]
           office_name = json_data["name"]

           new_office = {
               "id": id,
               "type": office_type,
               "name": office_name

           }

           print(new_office)
           offices.append(new_office)

           return make_response(jsonify({
               "status": 201,
               "data": [new_office]
           }), 201)

       else:
           return jsonify({"status":404,"Message":"Enter valid data"})


   return make_response(jsonify({
       "status": 401,
       "message": "Missing required fields"
   }))







# @v1.route("/offices/<officeID>", methods=['DELETE'])
# def deleteOffice(officeID):
#    # print(offices)
#    # print(type(officeID))
#    for office in offices:
#        if office["id"] == int(officeID):
#            offices.remove(office)
#            return make_response(jsonify({
#                "status": 200,
#                "data": "the office has been deleted successfully"
#            }), 200)

#    return make_response(jsonify({
#        "status": 404,
#        "error": "could not find office with ID {}".format(officeID)
#    }),404)
# @v1.route('/offices/<officeID>',methods=['PATCH'])
# def party_update(officeID):
#     for office in offices:
#         if office['id'] == int(officeID):
#             data = request.get_json()
#             # new_name = data['name']
#             print(data)
#             office['name'] = data['name']
#             return make_response(jsonify({
#                 "status": 200,
#                 "data": "updated  the party with office ID {} ".format(officeID)
#             }), 200)
#         elif office in offices:
#             return "Office Already exist"
#         else:
#             update_office = {
#                 "name": office['name']
#
#             }
#             office.append(update_office)
#             return make_response(jsonify({
#                 "status": 200,
#                 "data": [update_office]
#             }), 200)



if __name__ == "__main__":
   b_v1.run(debug=True)