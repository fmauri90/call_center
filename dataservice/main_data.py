from flask import Flask, request, jsonify, make_response
from datetime import datetime
from api_calls import api_calls
from api_condominium import api_condominium
from api_geo import api_geo
from api_condominium_company import api_condominium_company
from api_technical_company import api_technical_company
from api_companies import api_companies
from api_new import api_new
from api_call_status import api_call_status


app = Flask(__name__)

app.register_blueprint(api_calls)
app.register_blueprint(api_condominium)
app.register_blueprint(api_geo)
app.register_blueprint(api_condominium_company)
app.register_blueprint(api_technical_company)
app.register_blueprint(api_companies)
app.register_blueprint(api_new)
app.register_blueprint(api_call_status)

if __name__ == '__main__':
    app.run(port=5050)
