import requests
from flask import Blueprint, request, jsonify, make_response

import json
import config

api_technical_company_business = Blueprint('api_technical_company_business', __name__)


@api_technical_company_business.route('/<id_company>/technical', methods=['GET'])
def technical_company_business(id_company):
    technical_company = requests.get('http://127.0.0.1:5050/{}/technical'.format(id_company), headers={"Content-Type": "application/json"})
    data = json.loads(technical_company.text)
    print(data)
    if 'items' in data and data.get('status', '') == 'OK':
        technical_list = [
                            {
                                config.TECH_ID: el[config.TECH_ID],
                                config.TECH_INFO: el[config.TECH_INFO]
                            }
                            for el in data['items']]

        response = {
            "message": "Technicians list",
            "items": technical_list
        }
        res_technical = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No technicians in database",
            "items": []
        }
        res_technical = make_response(jsonify(response), 404)

    return res_technical


#@api_technical_company_business.route('/technician/<id_technician>/<chat_id>', methods=['GET'])
#def update_chat_id(id_technician, chat_id):
#    tech_status = requests.get('http://127.0.0.1:5050/technician/{}/{}'.format(id_technician, chat_id),
#                               headers={"Content-Type": "application/json"})

@api_technical_company_business.route('/technician/<id_technician>/add_chat_id/<chat_id>', methods=['GET'])
def update_chat_id(id_technician, chat_id):

    tech_res = requests.get('http://127.0.0.1:5050/technician_chat/{}/info'.format(chat_id),
                 headers={"Content-Type": "application/json"})
    tech_info = json.loads(tech_res.text)

    response = {
        'status': 'ERROR'
    }

    if 'info' in tech_info:
        if config.TECH_ID in tech_info['info']:
            if str(tech_info['info'][config.TECH_ID]) == id_technician:
                response = {
                    'status': 'OK',
                    'message': 'You are just logged in'
                }
            else:
                response = {
                    'status': 'OK',
                    'message': 'You are logged as a different tech. Use /logout command before /login'
                }
        else:
            tech_status = requests.get('http://127.0.0.1:5050/technician/{}/add_chat_id/{}'.format(id_technician, chat_id),
                               headers={"Content-Type": "application/json"})


            data = json.loads(tech_status.text)
            if 'status' in data:
                if data['status'] == 'OK':
                    response = {
                        'status': 'OK',
                        'message': 'You are logged in.'
                    }

    res_status = make_response(jsonify(response), 200)

    return res_status


@api_technical_company_business.route('/technician_chat/<chat_id>/logout', methods=['GET'])
def logout_chat_id(chat_id):
    tech_status = requests.get('http://127.0.0.1:5050/technician_chat/{}/logout'.format(chat_id),
                               headers={"Content-Type": "application/json"})
    response = {
        'status': 'ERROR',
        'message': 'ERROR'
    }

    data = json.loads(tech_status.text)
    if 'status' in data:
        if data['status'] == 'OK':
            response = {
                'status': 'OK',
                'message': 'You are logged out'
            }

    res_status = make_response(jsonify(response), 200)

    return res_status


@api_technical_company_business.route('/technician_chat/<chat_id>/update/<status>', methods=['GET'])
def tech_company_business(chat_id, status):
    tech_res = requests.get('http://127.0.0.1:5050/technician_chat/{}/info'.format(chat_id, status),
                            headers={"Content-Type": "application/json"})
    tech_info = json.loads(tech_res.text)
    response = {
        "message": "Retry",
    }

    if tech_info['info'][config.TECH_STATUS] == 2 and status == '0':
        calls_res = requests.get('http://127.0.0.1:5050/calls/active/tech/{}'.format(tech_info['info'][config.TECH_ID]),
                                 headers={"Content-Type": "application/json"})
        calls_json = json.loads(calls_res.text)
        calls = calls_json.get('items', [])

        if len(calls) > 0:
            response = {
                "message": "You have an active call.",
                "call_info": calls[0],
                "status": 'OK'
            }

            res_call = make_response(jsonify(response), 200)

            return res_call

    if tech_info['info'][config.TECH_STATUS] == 2 and status == '1':
        calls_res = requests.get('http://127.0.0.1:5050/calls/active/tech/{}'.format(tech_info['info'][config.TECH_ID]),
                                 headers={"Content-Type": "application/json"})
        calls_json = json.loads(calls_res.text)
        calls = calls_json.get('items', [])

        if len(calls) > 0:
            response = {
                "message": "You have an active call.",
                "call_info": calls[0],
                "status": 'OK'
            }

            res_call = make_response(jsonify(response), 200)

            return res_call

    if status == '0':
        tech_status = requests.get('http://127.0.0.1:5050/technician_chat/{}/update/{}'.format(chat_id, status),
                                   headers={"Content-Type": "application/json"})
        data = json.loads(tech_status.text)
        if 'tech_status' in data and data.get('status', '') == 'OK':
            response = {
                "message": "Good by.",
                "status": "OK"
            }

    if status == '1':

        calls_res = requests.get('http://127.0.0.1:5050/calls/{}/1'.format(tech_info['info'][config.COMPANY_ID]), headers={"Content-Type": "application/json"})
        calls_json = json.loads(calls_res.text)
        calls = calls_json.get('items', [])

        if len(calls) > 0:
            tech_status = requests.get('http://127.0.0.1:5050/technician_chat/{}/update/2'.format(chat_id),
                                       headers={"Content-Type": "application/json"})
            call_status = requests.get('http://127.0.0.1:5050/calls/{}/update/2/{}'.format(calls[0][config.CALL_ID], tech_info['info'][config.TECH_ID]),
                                       headers={"Content-Type": "application/json"})
            response = {
                "message": "Status tech",
                "status": '2',
                "call_info": calls[0]
            }
        else:
            tech_status = requests.get('http://127.0.0.1:5050/technician_chat/{}/update/1'.format(chat_id),
                                       headers={"Content-Type": "application/json"})
            response = {
                "message": "At the moment there aren't any calls, retry /active later",
                "status": "OK",
            }

    if status == '3':

        calls_res = requests.get('http://127.0.0.1:5050/calls/active/tech/{}'.format(tech_info['info'][config.TECH_ID]),
                                       headers={"Content-Type": "application/json"})

        calls_json = json.loads(calls_res.text)
        calls = calls_json.get('items', [])

        if len(calls) > 0:
            tech_status = requests.get('http://127.0.0.1:5050/technician_chat/{}/update/3'.format(chat_id),
                                       headers={"Content-Type": "application/json"})
            call_status = requests.get('http://127.0.0.1:5050/calls/{}/update/3/{}'.format(calls[0][config.CALL_ID],
                                                                                       tech_info['info'][
                                                                                           config.TECH_ID]),
                                   headers={"Content-Type": "application/json"})

            response = {
                "message": "Call ended. If you want new call use command /active.",
                "status": 'OK',
            }

    res_call = make_response(jsonify(response), 200)

    return res_call



"""
@api_technical_company_business.route('/technician_chat/<chat_id>/update/<status>', methods=['GET'])
def tech_company_business(chat_id, status):
    tech_status = requests.get('http://127.0.0.1:5050/technician_chat/{}/update/{}'.format(chat_id, status), headers={"Content-Type": "application/json"})
    data = json.loads(tech_status.text)
    if 'tech_status' in data and data.get('status', '') == 'OK':
        response = {
            "message": "Status tech",
            "status": data['tech_status']
        }

        if status == '1':
            tech_res = requests.get('http://127.0.0.1:5050/technician_chat/{}/info'.format(chat_id, status), headers={"Content-Type": "application/json"})
            tech_info = json.loads(tech_res.text)
            calls_res = requests.get('http://127.0.0.1:5050/calls/{}/1'.format(tech_info['info'][config.COMPANY_ID]), headers={"Content-Type": "application/json"})
            calls_json = json.loads(calls_res.text)
            calls = calls_json.get('items', [])

            if len(calls) > 0:
                tech_status = requests.get('http://127.0.0.1:5050/technician_chat/{}/update/2'.format(chat_id),
                                           headers={"Content-Type": "application/json"})
                call_status = requests.get('http://127.0.0.1:5050/calls/{}/update/2/{}'.format(calls[0][config.CALL_ID], tech_info['info'][config.TECH_ID]),
                                           headers={"Content-Type": "application/json"})
                response = {
                    "message": "Status tech",
                    "status": '2',
                    "call": calls[0]
                }

        if status == '3':
            tech_res = requests.get('http://127.0.0.1:5050/technician_chat/{}/info'.format(chat_id, status), headers={"Content-Type": "application/json"})
            tech_info = json.loads(tech_res.text)

            calls_res = requests.get('http://127.0.0.1:5050/calls/active/tech/{}'.format(tech_info['info'][config.TECH_ID]),
                                           headers={"Content-Type": "application/json"})

            calls_json = json.loads(calls_res.text)
            calls = calls_json.get('items', [])

            if len(calls) > 0:
                call_status = requests.get('http://127.0.0.1:5050/calls/{}/update/3/{}'.format(calls[0][config.CALL_ID],
                                                                                           tech_info['info'][
                                                                                               config.TECH_ID]),
                                       headers={"Content-Type": "application/json"})

                response = {
                    "message": "Call ended. If you want new call use command /active.",
                    "status": 'OK',
                }

        res_call = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No call in database",
            "items": []
        }
        res_call = make_response(jsonify(response), 404)

    return res_call
"""