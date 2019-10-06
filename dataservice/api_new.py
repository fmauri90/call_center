from flask import Blueprint, request, jsonify, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from tabledef import Call, Condominium, Company, Technician
import requests
import config

api_new = Blueprint('api_new', __name__)



def get_company_id_by_name(name):
    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute("SELECT id, name_company FROM companies WHERE name_company IS {}".format(name))
    ids = []
    for i in result:
        ids.append(i[0])

    return ids[0]


@api_new.route('/add_new_condominium', methods=['POST'])
def add_new_condominium():
    """
    endpoint which is used add a new condominium to database
    :param
    :return: add a new condominium to database and return the id of the condominium that has been added
    """

    if request.is_json:
        input_data = request.get_json()
        required = [config.COMPANY_ID, config.BUILDING_NAME, config.BUILDING_ADDRESS]
        for field in required:
            if field not in input_data:
                res = make_response(jsonify({"message": "Field {} is required".format(field), "status": 1}), 404)
                return res

        engine = create_engine('sqlite:///call_center.db', echo=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        condominium = Condominium(input_data[config.COMPANY_ID], {config.BUILDING_ADDRESS: input_data[config.BUILDING_ADDRESS], config.BUILDING_NAME: input_data[config.BUILDING_NAME]})
        session.add(condominium)

        session.commit()
        session.refresh(condominium)
        session.close()

        response = {
            "message": "condominium:",
            'status': 'OK',
            "items": condominium.id_condominium

        }
        res = make_response(jsonify(response), 200)

        return res
    else:
        response = {
            "message": "call: The call cannot be added",
            'status': 'ERROR'
        }

    res = make_response(jsonify(response), 404)

    return res


@api_new.route('/add_new_call', methods=['POST'])
def add_new_call():
    """
    endpoint which is used add a new call to database
    :param
    :return: add a new call to database and return the id of the call that has been added
    """

    if request.is_json:
        input_data = request.get_json()
        required = [config.COMPANY_ID, config.CALL_MESSAGE, config.BUILDING_ID]
        for field in required:
            if field not in input_data:
                res = make_response(jsonify({"message": "Field `{}` is required".format(field)}), 404)
                return res

        engine = create_engine('sqlite:///call_center.db', echo=True)
        if config.CALL_STATUS in input_data:
            call_status = input_data[config.CALL_STATUS]
        else:
            call_status = '1'
        Session = sessionmaker(bind=engine)
        session = Session()
        call = Call(input_data[config.COMPANY_ID], input_data[config.BUILDING_ID], datetime.now(), {config.CALL_MESSAGE: input_data[config.CALL_MESSAGE]}, call_status)
        session.add(call)

        session.commit()
        session.refresh(call)
        session.close()

        response = {
            "message": "call:",
            'status': 'OK',
            "items": call.id_call
        }
        res = make_response(jsonify(response), 200)

        return res
    else:
        response = {
            "message": "call: The call cannot be added",
            'status': 'ERROR'
        }
        res = make_response(jsonify(response), 404)

        return res




