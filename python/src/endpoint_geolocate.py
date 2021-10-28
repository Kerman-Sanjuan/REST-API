from flask import request
from flask_restful import Resource
import xml.etree.ElementTree as ET
import db
from utils import geoname


class Geolocate(Resource):
    engine = db.engine
    conn = engine.connect
    session = db.session

    def post(self):
        """ Con el protocolo POST anadimos un nuevo usuario"""
        
        username = request.json['username']
        postal_code = request.json['postal_code']
        status_code = geoname(username, postal_code)

        return status_code
