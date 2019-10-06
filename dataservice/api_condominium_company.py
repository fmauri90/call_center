from flask import Blueprint, request, jsonify, make_response
from tabledef import Condominium
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config


select_condominium = """
SELECT id_condominium, id_company, data_condominium FROM condominiums WHERE id_company is {};
"""

api_condominium_company = Blueprint('api_condominium_company', __name__)


@api_condominium_company.route('/<id_company>/condominium', methods=['GET'])
def condominium_company_id(id_company):
    """
    endpoint which is used add a new call to database
    :param id_company: id_company
    :return: add a new call to database and return the id of the call that has been added
    """

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_condominium.format(id_company))
    condominium = []
    for el in result:
        condominium.append(
            {
                config.BUILDING_ID: el[0],
                config.BUILDING_INFO: el[2]
            }
        )

    if result:
        response = {
            "message": "Condominiums:",
            'status': 'OK',
            "items": condominium
        }
        res_condominium = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No condominium in database",
            'status': 'ERROR',
            "items": []
        }
        res_condominium = make_response(jsonify(response), 404)
    return res_condominium
