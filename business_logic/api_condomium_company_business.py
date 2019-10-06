import requests
from flask import Blueprint, request, jsonify, make_response

import json
import config

api_condominium_company_business = Blueprint('api_condominium_company_business', __name__)


@api_condominium_company_business.route('/<id_company>/condominium', methods=['GET'])
def condominium_company_business(id_company):
    condominium_company_bus = requests.get('http://127.0.0.1:5050/{}/condominium'.format(id_company), headers={"Content-Type": "application/json"})
    data = json.loads(condominium_company_bus.text)
    print(data)
    if 'items' in data and data.get('status', '') == 'OK':
        condominium_company_list = [
                            {
                                config.BUILDING_ID: el[config.BUILDING_ID],
                                config.BUILDING_INFO: el[config.BUILDING_INFO]
                            }
                            for el in data['items']]

        response = {
            "message": "Condominium list",
            "items": condominium_company_list
        }
        res_condominium = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No condominium in database",
            "items": []
        }
        res_condominium = make_response(jsonify(response), 404)

    return res_condominium
