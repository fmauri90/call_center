import requests
from flask import Blueprint, request, jsonify, make_response
import json
import config


api_condominium_business = Blueprint('api_condominium_business', __name__)


@api_condominium_business.route('/<id_company>/number_condominium', methods=['GET'])
def number_condominium_company_business(id_company):
    number_condominium_company_bus = requests.get('http://127.0.0.1:5050/{}/number_condominium'.format(id_company), headers={"Content-Type": "application/json"})
    data = json.loads(number_condominium_company_bus.text)
    if 'counter' in data and data.get('status', '') == 'OK':
        response = {
            "message": "Condominium list",
            "counter": data['counter']
        }
        res_condominium = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No condominiums in database",
            "counter": '0'
        }
        res_condominium = make_response(jsonify(response), 404)

    return res_condominium


@api_condominium_business.route('/number_condominium', methods=['GET'])
def number_condominium_all_business():
    number_condominium_bus = requests.get('http://127.0.0.1:5050/number_condominium', headers={"Content-Type": "application/json"})
    data = json.loads(number_condominium_bus.text)
    if 'counter' in data and data.get('status', '') == 'OK':
        response = {
            "message": "Condominium list",
            "counter": data['counter']
        }
        res_condominium = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No condominiums in database",
            "counter": '0'
        }
        res_condominium = make_response(jsonify(response), 404)

    return res_condominium

