import requests
from flask import Flask, request, jsonify, make_response
from datetime import datetime
from api_calls import api_calls_business
from api_condominium_business import api_condominium_business
from api_geo_business import api_geo_business
from api_condomium_company_business import api_condominium_company_business
from api_technical_company_business import api_technical_company_business
from api_companies_business import api_companies_business
from api_call_status import api_call_status


app = Flask(__name__)
app.register_blueprint(api_calls_business)
app.register_blueprint(api_condominium_business)
app.register_blueprint(api_geo_business)
app.register_blueprint(api_condominium_company_business)
app.register_blueprint(api_technical_company_business)
app.register_blueprint(api_companies_business )
app.register_blueprint(api_call_status)

if __name__ == '__main__':
    app.run(port=5080)
