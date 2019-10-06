from flask import Blueprint, request, jsonify, make_response
from tabledef import Company
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

select_companyes = """
SELECT id, name_company, date_entered, date_change, date_cancel, data_company FROM company;
"""


api_companies = Blueprint('api_companies', __name__)


@api_companies.route('/companies', methods=['GET'])
def companies():
    """
            endpoint which is used to have the informations of all the companies in the database
            :param
            :return: return the informations of all the companies in the database
    """

    engine = create_engine('sqlite:///call_center.db', echo=True)
    conn = engine.connect()
    result = conn.execute(select_companyes)
    companies = []
    for el in result:
        companies.append(
            {
                config.COMPANY_ID: el[0],
                config.COMPANY_NAME: el[1],
                config.COMPANY_ENTER_DATA: el[2],
                config.COMPANY_CHANGE_DATA: el[3],
                config.COMPANY_DELETE_DATA: el[4],
                config.COMPANY_INFO: el[5],
            }
        )
    if result:
        response = {
            "message": "companies",
            'status': 'OK',
            "items": companies
        }
        res_companies = make_response(jsonify(response), 200)
    else:
        response = {
            "message": "No companies in database",
            'status': 'ERROR',
            "items": []
        }
        res_companies = make_response(jsonify(response), 404)

    return res_companies
