from flask import Blueprint, jsonify, request
from office_model import Office

app = Blueprint("v1", __name__, url_prefix="/app/v1")


@app.route('/offices/', methods=['POST', 'GET'])
def offices():
        if request.method == "POST":
            officedata = str(request.data.get('officedata', ''))
            if officedata:
                office = Office(officedata=officedata)
                office.save()
                response = jsonify({
                    'id': office.id,
                    'name': office.name,
                    'type': office.type,
                    
                })
                response.status_code = 201
                return response
        else:
            # GET
            offices = office.get_all()
            results = []

            for office in offices:
                obj = {
                    'id': office.id,
                    'name': office.name,
                    'type': office.type,
                    
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

            return app