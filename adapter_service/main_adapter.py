import requests
from flask import Flask, request, jsonify, make_response
from api_geo_adapter import api_geo_adapter


app = Flask(__name__)
app.register_blueprint(api_geo_adapter)


if __name__ == '__main__':
    app.run(port=5090)
