from flask import Blueprint, request, jsonify, make_response
from tabledef import Condominium
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config


select_condominium = """
SELECT id_condominium, id_company, data_condominium FROM condominiums;
"""

select_condominium_company = """
SELECT id_condominium, id_company, data_condominium FROM condominiums WHERE id_company is {};
"""

select_condominium_by_id = """
SELECT id_condominium, id_company, data_condominium FROM condominiums WHERE id_condominium is {};
"""

api_condominium = Blueprint('api_condominium', __name__)


@api_condominium.route('/<id_company>/number_condominium', methods=['GET'])
def number_condominium_company_id(id_company):

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_condominium_company.format(id_company))
    n_condominium = []
    for el in result:
        n_condominium.append(
            {
                config.BUILDING_ID: el[0],
                config.BUILDING_INFO: el[2]
            }
        )

    response = {
        "message": "Number condominiums:",
        'status': 'OK',
        "counter": len(n_condominium)
    }
    res_condominium = make_response(jsonify(response), 200)
    return res_condominium


@api_condominium.route('/number_condominium', methods=['GET'])
def number_condominium():
    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_condominium)
    n_condominium = []
    for el in result:
        n_condominium.append(
            {
                config.BUILDING_ID: el[0],
                config.COMPANY_ID: el[1],
                config.BUILDING_INFO: el[2]
            }
        )
    if result:
        response = {
            "message": "Number condominiums:",
            'status': 'OK',
            "counter": len(n_condominium)
        }
        res_condominium = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "ERROR: No condominium in database!!!",
            'status': 'ERROR',
            "items": []
        }
        res_condominium = make_response(jsonify(response), 404)

    return res_condominium


@api_condominium.route('/condominium/<build_id>', methods=['GET'])
def condominium_by_id(build_id):

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_condominium_by_id.format(build_id))
    condominium = []
    for el in result:
        condominium.append(
            {
                config.BUILDING_ID: el[0],
                config.COMPANY_ID: el[1],
                config.BUILDING_INFO: el[2]
            }
        )

    response = {
        'status': 'OK',
        'items': condominium
    }

    res_condominium = make_response(jsonify(response), 200)
    return res_condominium

