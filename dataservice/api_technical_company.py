from flask import Blueprint, request, jsonify, make_response
from tabledef import Technician
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from tabledef import Technician, Call

import config


# create a query that extracts the information of the table "technician" for a specific company
select_technicians = """
SELECT id_technician, id_company, data_technician, chat_id, status, message FROM technicians WHERE id_company is {};
"""

select_technician_company = """
SELECT id_company FROM technicians WHERE chat_id is {};
"""

select_technician_info_by_chat_id = """
SELECT id_technician, id_company, data_technician, chat_id, status FROM technicians WHERE chat_id is {};
"""

select_technician_info_by_tech_id = """
SELECT id_technician, id_company, data_technician, chat_id, status FROM technicians WHERE id_technician is {};
"""

#'''
# Call
select_call_from_status = """
SELECT id_call, id_company, id_condominium, date_call, data_call, call_status FROM calls WHERE call_status is {} AND id_company is {};
"""
#'''

# allows main_data to recall the underlying endpoint
api_technical_company = Blueprint('api_technical_company', __name__)


@api_technical_company.route('/<id_company>/technical', methods=['GET'])
def technician_company_id(id_company):
    """
    endpoint which is used to find the technicians of a given company in the database
    :param id_company: company_id
    :return: return the technician referred to the id_company
    """

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_technicians.format(id_company))
    technicians = []
    for el in result:
        technicians.append(
            {
                config.TECH_ID: el[0],
                config.TECH_INFO: el[2]
                }
            )

    if result:

        response = {
                "message": "technicians:",
                'status': 'OK',
                "items": technicians
            }

        res_technicians = make_response(jsonify(response), 200)

    else:
        response = {
            "message": "ERROR: No technicians in database",
            'status': 'ERROR',
            "items": []
        }
        res_technicians = make_response(jsonify(response), 404)

    return res_technicians


#@api_technical_company.route('/technician/<id_technician>/<chat_id>', methods=['GET'])
@api_technical_company.route('/technician/<id_technician>/add_chat_id/<chat_id>', methods=['GET'])
def update_chat_id(id_technician, chat_id):
    """
    endpoint which is used to login the technician
    :param id_technician: id_technician, chat_id: chat_id
    :return: insert in the database the chat_id referred to the id_technician
    """

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    update_chat_id = update(Technician).where(Technician.id_technician == id_technician).values(chat_id=chat_id)
    conn.execute(update_chat_id)
    response = {
        'status': 'OK'
    }
    res_status = make_response(jsonify(response), 200)

    return res_status

@api_technical_company.route('/technician_chat/<chat_id>/logout', methods=['GET'])
def logout_chat_id(chat_id):
    """
    endpoint which is used to logout the technician
    :param chat_id: chat_id
    :return: when technician logout cancel the chat_id referred to the technician with the same chat_id
    """


    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    update_chat_id = update(Technician).where(Technician.chat_id == chat_id).values(chat_id='', status='0')
    conn.execute(update_chat_id)
    response = {
        'status': 'OK'
    }
    res_status = make_response(jsonify(response), 200)

    return res_status

@api_technical_company.route('/technician_chat/<chat_id>/update/<status>', methods=['GET'])
def update_status_tech_by_chat_id(chat_id, status):
    """
    endpoint which is used to update the status of technician referred to chat_id
    :param chat_id: chat_id, status: status
    :return: update the status of technician referred to chat_id
    """


    if status in config.TECH_STATUS_LABEL:
        engine = create_engine('sqlite:///call_center.db', echo=True)
        conn = engine.connect()
        update_status = update(Technician).where(Technician.chat_id == chat_id).values(status=status)
        conn.execute(update_status)

        response = {
            "tech_status": config.TECH_STATUS_LABEL[status],
            'status': 'OK'
        }

        if status == '1':
            comp = conn.execute(select_technician_company.format(chat_id))
            free_calls = conn.execute(select_call_from_status.format(1, next(comp)[0]))
            calls = []
            for el in free_calls:
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
            #Call(input_data[config.COMPANY_ID], input_data[config.BUILDING_ID], datetime.now(), {config.CALL_MESSAGE: input_data[config.CALL_MESSAGE]}, call_status)
            response = {
                "tech_status": config.TECH_STATUS_LABEL[status],
                'status': 'OK',
                "free_calls": calls
            }

        res_status = make_response(jsonify(response), 200)
    else:
        response = {
            "tech_status": "Status must be between 0 and 4",
            'status': 'ERROR'
        }
        res_status = make_response(jsonify(response), 404)

    return res_status


@api_technical_company.route('/technician/<tech_id>/update/<status>', methods=['GET'])
def update_status_tech_by_tech_id(tech_id, status):
    """
    endpoint which is used to update the status of technician referred to tech_id
    :param tech_id: tech_id, status: status
    :return: update the status of technician referred to tech_id
    """

    if status in config.TECH_STATUS_LABEL:
        engine = create_engine('sqlite:///call_center.db', echo=True)
        conn = engine.connect()
        update_status = update(Technician).where(Technician.id_technician == tech_id).values(status=status)
        conn.execute(update_status)
        response = {
            "tech_status": config.TECH_STATUS_LABEL[status],
            'status': 'OK'
        }
        res_status = make_response(jsonify(response), 200)
    else:
        response = {
            "tech_status": "Status must be between 0 and 4",
            'status': 'ERROR'
        }
        res_status = make_response(jsonify(response), 404)

    return res_status

##### select_technician_info_by_chat_id
@api_technical_company.route('/technician_chat/<chat_id>/info', methods=['GET'])
def get_tech_info_by_chat_id(chat_id):
    """
    endpoint which is used to select the information of technician by chat id
    :param chat_id: chat_id
    :return: return the information of technician by chat id
    """
    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result =conn.execute(select_technician_info_by_chat_id.format(chat_id))
    info = {}
    for el in result:
        info = {
            config.TECH_ID: el[0],
            config.COMPANY_ID: el[1],
            config.TECH_INFO: el[2],
            config.TECH_CHAT: el[3],
            config.TECH_STATUS: el[4]
        }
    response = {
        "info": info,
        'status': 'OK'
    }
    res_status = make_response(jsonify(response), 200)

    return res_status


@api_technical_company.route('/technician/<tech_id>/info', methods=['GET'])
def get_tech_info_by_tech_id(tech_id):
    """
    endpoint which is used to select the information of technician by chat id
    :param tech_id: chat_id
    :return: return the information of technician by chat id
    """
    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result =conn.execute(select_technician_info_by_tech_id.format(tech_id))
    for el in result:
        info = {
            config.TECH_ID: el[0],
            config.COMPANY_ID: el[1],
            config.TECH_INFO: el[2],
            config.TECH_CHAT: el[3],
            config.TECH_STATUS: el[4]
        }
    response = {
        "info": info,
        'status': 'OK'
    }
    res_status = make_response(jsonify(response), 200)

    return res_status