import requests
from flask import Blueprint, request, jsonify, make_response
import json
import config


api_condominium_business = Blueprint('api_condominium_business', __name__)


@api_condominium_business.route('/<id_company>/number_condominium', methods=['GET'])
def number_condominium_company_business(id_company):

    """
        endpoint which is used to have the number of condominium of a specific company
        :params id_company: id_company
        :return: return the number of condominium of a specific company
    """

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

    """
        endpoint which is used to have the number of condominium of a specific technician
        :params id_company: id_company
        :return: return the number of condominium of a specific technician
    """

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

@api_condominium_business.route('/condominium/<build_id>', methods=['GET'])
def condominium_by_id(build_id):
    """
            endpoint which is used to have the condominium of a specific id
            :params id_company: id_company
            :return: return the number of condominium of a specific company
    """

    number_condominium_company_bus = requests.get('http://127.0.0.1:5050/condominium/{}'.format(build_id), headers={"Content-Type": "application/json"})
    data = json.loads(number_condominium_company_bus.text)
    if 'items' in data and data.get('status', '') == 'OK':
        response = {
            "status": "OK",
            "items": data['items']
        }
        res_condominium = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No condominiums in database",
            "status": 'Error'
        }
        res_condominium = make_response(jsonify(response), 404)

    return res_condominium