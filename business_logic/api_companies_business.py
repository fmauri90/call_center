import requests
from flask import Blueprint, request, jsonify, make_response

import json

api_companies_business = Blueprint('api_companies_business', __name__)


@api_companies_business.route('/companies', methods=['GET'])
def company_business():

    """
        endpoint which is used to have the name of all companies
        :params
        :return: return the name of all companies
    """

    companies = requests.get('http://127.0.0.1:5050/companies', headers={"Content-Type": "application/json"})
    data = json.loads(companies.text)
    if 'items' in data and data.get('status', '') == 'OK':
        companies_list = [el['name_company'] for el in data['items']]

        response = {
            "message": "Companies list",
            "items": companies_list,
            "counter": len(companies_list)
        }
        res_companies = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No companies in database",
            "items": [],
            "counter": 0
        }
        res_companies = make_response(jsonify(response), 404)

    return res_companies

