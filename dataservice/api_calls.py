from flask import Blueprint, request, jsonify, make_response
from tabledef import Call, Company
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date, timedelta

import config


select_calls = """
SELECT id_call, id_company, id_condominium, date_call, data_call FROM calls WHERE date_call between date('{data1}') and date('{data2}');
"""

select_calls_company = """
SELECT id_call, id_company, id_condominium, date_call, data_call FROM calls WHERE id_company IS {} AND date_call between date('{data1}') and date('{data2}');
"""

select_call_from_status = """
SELECT id_call, id_company, id_condominium, date_call, data_call, call_status FROM calls WHERE call_status is {} AND id_company is {};
"""

api_calls = Blueprint('api_calls', __name__)


@api_calls.route('/companies/calls/<year>/<month>/<day>', methods=['GET'])
def day_call(year, month, day):

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_calls.format(data1=date(int(year), int(month), int(day)) - timedelta(days=1), data2=date(int(year), int(month), int(day)) + timedelta(days=1)))
    calls = []
    for el in result:
        calls.append(
            {
                config.CALL_ID: el[0],
                config.COMPANY_ID: el[1],
                config.BUILDING_ID: el[2],
                config.CALL_INFO: el[4]
            }
        )

    if result:
        response = {
            "message": "calls",
            'status': 'OK',
            "items": calls
        }
        res_calls = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "ERROR: No calls in database",
            'status': 'ERROR',
            "items": []
        }
        res_calls = make_response(jsonify(response), 404)

    return res_calls


@api_calls.route('/<id_company>/calls/<year>/<month>/<day>', methods=['GET'])
def day_call_company(id_company, year, month, day):
    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_calls_company.format(id_company, data1=date(int(year), int(month), int(day)) - timedelta(days=1), data2=date(int(year), int(month), int(day)) + timedelta(days=1)))
    calls_company = []
    for el in result:
        calls_company.append(
            {
                config.CALL_ID: el[0],
                config.BUILDING_ID: el[2],
                config.CALL_INFO: el[4]
            }
        )
    if result:
        response = {
            "message": "calls".format(config.COMPANY_ID),
            'status': 'OK',
            "items": calls_company
        }
        res_calls_company = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No calls in database",
            'status': 'ERROR',
            "items": []
        }
        res_calls_company = make_response(jsonify(response), 404)

    return res_calls_company


@api_calls.route('/calls/<company_id>/<status>', methods=['GET'])
def calls_company_by_status(company_id, status):
    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    calls_res = conn.execute(select_call_from_status.format(status, company_id))
    calls = []
    for el in calls_res:
        calls.append(
            {
                config.CALL_ID: el[0],
                config.COMPANY_ID: el[1],
                config.BUILDING_ID: el[2],
                config.CALL_DATE: el[3],
                config.CALL_INFO: el[4],
                config.CALL_STATUS: el[5]
            }
        )

    response = {
        "message": "Calls",
        'status': 'OK',
        "items": calls
    }
    res_calls = make_response(jsonify(response), 200)


    return res_calls












"""
@api_calls.route('/calls/<id_call>', methods=['GET'])
def day_call_company(id_call):
    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_calls.format(id_call))
    calls_company = []
    for el in result:
        calls_company.append(
            {
                config.CALL_ID: el[0],
                config.BUILDING_ID: el[2],
                config.CALL_INFO: el[4]
            }
        )
    if result:
        response = {
            "message": "calls".format(config.COMPANY_ID),
            'status': 'OK',
            "items": calls_company
        }
        res_calls_company = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No calls in database",
            'status': 'ERROR',
            "items": []
        }
        res_calls_company = make_response(jsonify(response), 404)

    return res_calls_company

"""