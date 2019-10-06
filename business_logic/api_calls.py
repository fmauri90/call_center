import requests
from flask import Blueprint, request, jsonify, make_response

import json
import config

api_calls_business = Blueprint('api_calls', __name__)


@api_calls_business.route('/companies/calls/<year>/<month>/<day>', methods=['GET'])
def day_call_business(year, month, day):

    """
        endpoint which is used to have the call of a specif day for all companies
        :params year: year,  month: month, day: day
        :return: return the call of a specif day for all companies
    """

    day_call = requests.get('http://127.0.0.1:5050/companies/calls/{}/{}/{}'.format(year, month, day), headers={"Content-Type": "application/json"})
    data = json.loads(day_call.text)
    if 'items' in data and data.get('status', '') == 'OK':
        day_call_list = [
            {
                config.CALL_ID: el[config.CALL_ID],
                config.COMPANY_ID: el[config.COMPANY_ID],
                config.BUILDING_ID: el[config.BUILDING_ID],
                config.CALL_INFO: el[config.CALL_INFO]
            }
            for el in data['items']]

        response = {
            "message": "Call list",
            "items": day_call_list
        }
        res_call = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No call in database",
            "items": []
        }
        res_call = make_response(jsonify(response), 404)

    return res_call


@api_calls_business.route('/<id_company>/calls/<year>/<month>/<day>', methods=['GET'])
def day_call_company_business(id_company, year, month, day):

    """
        endpoint which is used to have the call of a specif day for a specific company
        :params id_company: id_company, year: year,  month: month, day: day
        :return: return the call of a specif day for a specific company
    """

    day_call_company = requests.get('http://127.0.0.1:5050/{}/calls/{}/{}/{}'.format(id_company, year, month, day), headers={"Content-Type": "application/json"})
    data = json.loads(day_call_company.text)
    if 'items' in data and data.get('status', '') == 'OK':
        day_call_list = [
            {
                config.CALL_ID: el[config.CALL_ID],
                config.BUILDING_ID: el[config.BUILDING_ID],
                config.CALL_INFO: el[config.CALL_INFO]
            }
            for el in data['items']]

        response = {
            "message": "Call list",
            "items": day_call_list
        }
        res_call = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No call in database",
            "items": []
        }
        res_call = make_response(jsonify(response), 404)

    return res_call



