from flask import Blueprint, request, jsonify, make_response
import json
import requests

api_geo_adapter = Blueprint('api_geo_adapter', __name__)


@api_geo_adapter.route('/geo_condominium_adapter', methods=['GET'])
def geo_coder():
    if request.is_json:

        req_json = request.get_json()
        print(req_json)
        if "address" not in req_json:
            res = make_response(jsonify({"message": "Field `address` is required", "status": 1}), 404)
            return res
        try:
            req_geo = requests.get(
                'https://nominatim.openstreetmap.org/search?q={address}&format=json&polygon=0&addressdetails=1'.format(
                    address=req_json.get('address')))

            if req_geo.json:
                response = {
                    "message": "",
                    "status": 0,
                    "items": req_geo.json()
                }

                res = make_response(jsonify(response), 200)

                return res
            else:
                res = make_response(jsonify({"message": "Geocoder API ERROR", "status": 4}), 404)
                return res
        except:
            res = make_response(jsonify({"message": "Geocoder API ERROR", "status": 4}), 404)
            return res
    else:
        res = make_response(jsonify({"message": "No JSON received", "status": 1}), 404)

        return res
