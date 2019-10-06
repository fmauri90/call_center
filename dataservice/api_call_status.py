from flask import Blueprint, jsonify, make_response
from tabledef import Call, Company
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from tabledef import Call
import config

select_call_status = """
SELECT id_call, id_company, id_condominium, date_call, data_call, call_status, id_technician FROM calls WHERE call_status IS {};
"""

select_call_status_2_tech = """
SELECT id_call, id_company, id_condominium, date_call, data_call, call_status, id_technician FROM calls WHERE id_technician IS {} AND call_status IS 2;
"""


api_call_status = Blueprint('api_call_status', __name__)


@api_call_status.route('/companies/calls/<call_status_id>', methods=['GET'])
def status(call_status_id):
    """
            endpoint which is used to have the calls of a specific status for all companies
            :params call_status_id: call_status_id
            :return: return the calls of a specific status for all companies
    """

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_call_status.format(call_status_id))
    call_status = []
    for el in result:
        call_status.append(
            {
                config.CALL_ID: el[0],
                config.COMPANY_ID: el[1],
                config.BUILDING_ID: el[2],
                config.CALL_INFO: el[4]
            }
        )

    if call_status_id in config.CALL_STATUS_LABEL:
        response = {
            "call_status": config.CALL_STATUS_LABEL[call_status_id],
            'status': 'OK',
            "items": call_status
        }
        res_calls = make_response(jsonify(response), 200)
    else:
        response = {
            "call_status": "Status not valid",
            'status': 'ERROR'
        }

        res_calls = make_response(jsonify(response), 404)

    return res_calls


@api_call_status.route('/calls/<call_id>/update/<status>/<id_technician>', methods=['GET'])
def update_status(call_id, status, id_technician):

    """
            endpoint which is used to update the id call and assigns the call of a specific technician
            :params call_id: call_id, status: status, id_technician: id_technician
            :return: update the id call and assigns the call of a specific technician
    """

    if status in config.CALL_STATUS_LABEL:
        engine = create_engine('sqlite:///call_center.db', echo=True)
        conn = engine.connect()
        update_status = update(Call).where(Call.id_call == call_id).values(call_status=status, id_technician=id_technician)
        conn.execute(update_status)
        response = {
            "call_status": config.CALL_STATUS_LABEL[status],
            'status': 'OK'
        }
        res_status = make_response(jsonify(response), 200)
    else:
        response = {
            "call_status": "Status must be between 1 and 3",
            'status': 'ERROR'
        }
        res_status = make_response(jsonify(response), 404)

    return res_status


@api_call_status.route('/calls/active/tech/<tech_id>', methods=['GET'])
def call_by_tech(tech_id):

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_call_status_2_tech.format(tech_id))
    call_info = []
    for el in result:
        call_info.append(
            {
                config.CALL_ID: el[0],
                config.COMPANY_ID: el[1],
                config.BUILDING_ID: el[2],
                config.CALL_INFO: el[4]
            }
        )


    response = {
        'status': 'OK',
        "items": call_info
    }
    res_calls = make_response(jsonify(response), 200)

    return res_calls