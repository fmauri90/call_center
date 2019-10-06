import requests
from flask import Blueprint

api_geo_business = Blueprint('api_geo', __name__)


@api_geo_business.route('/geo_condominium_business', methods=['GET'])
def api_geo():
    geo_condominium = requests.get('http://127.0.0.1:5090/geo_condominium_adapter', json={"address": "Via 4 Novembre, 122 Gardolo"}, headers={"Content-Type": "application/json"})
    content_geo_condominium = geo_condominium.content
    return content_geo_condominium

