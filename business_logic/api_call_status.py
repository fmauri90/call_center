import requests
from flask import Blueprint, request, jsonify, make_response

import json
import config

api_call_status = Blueprint('api_call_status', __name__)


@api_call_status.route('/companies/calls/<status>', methods=['GET'])
def day_call_business(status):

    """
        endpoint which is used to have the call of all companies for a specific status
        :params status: status
        :return: return the call of all companies for a specific status
    """

    status_call = requests.get('http://127.0.0.1:5050/companies/calls/{}'.format(status), headers={"Content-Type": "application/json"})
    data = json.loads(status_call.text)
    if 'items' in data and data.get('status', '') == 'OK':
        status_call_list = [
            {
                config.CALL_ID: el[config.CALL_ID],
                config.COMPANY_ID: el[config.COMPANY_ID],
                config.BUILDING_ID: el[config.BUILDING_ID],
                config.CALL_INFO: el[config.CALL_INFO]
            }
            for el in data['items']]

        response = {
            "message": "Call list",
            "items": status_call_list
        }
        res_call = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No call in database",
            "items": []
        }
        res_call = make_response(jsonify(response), 404)

    return res_call


@api_call_status.route('/calls/<call_id>/update/<status>/<id_technician>', methods=['GET'])
def day_call_company_business(call_id, status, id_technician):

    """
            endpoint which is used to update the id call and assigns the call of a specific technician
            :params call_id: call_id, status: status, id_technician: id_technician
            :return: update the id call and assigns the call of a specific technician
    """
    day_call_company = requests.get('http://127.0.0.1:5050/calls/{}/update/{}/{}'.format(call_id, status, id_technician), headers={"Content-Type": "application/json"})
    data = json.loads(day_call_company.text)
    if 'call_status' in data and 'id_technician' in data and data.get('status', '') == 'OK':

        response = {
            "message": "Call list",
            "status": config.CALL_STATUS_LABEL[data['call_status']],
            "id_technician": id_technician
        }
        res_call = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No call in database",
            "items": []
        }
        res_call = make_response(jsonify(response), 404)

    return res_call


