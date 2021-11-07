import xml.etree.ElementTree as ET
import requests
import db
from models import Details, Master
import flask
import xmltodict
engine = db.engine
conn = engine.connect
session = db.session


def geoname(username: str, postal_code: str) -> str:

    URL = 'http://api.geonames.org/postalCodeSearch?api.geonames.org/postalCodeSearch?'
    data = {'username': username, 'postalcode': postal_code}

    r = requests.post(URL, data=data)
    tree = ET.fromstring(r.content)
    print(r.status_code)
    city = ""
    for name in tree.iter('name'):
        city = name.text

    if city == "":
        return {'status': "400 BAD REQUEST", 
                'details': "Geoapi error, no city found, check username and postal code"},400
    try:  # Conexion con base de datos
        status = add_city(username, city, postal_code)
    except Exception as ex:

        return {'status': " 500 INTERNAL SERVER ERROR",
                'details': "error fetching the database."},500
    
    return status


def add_city(username, city, postal_code):
    user = Master(username)
    session.add(user)
    session.commit()
    session.refresh(user)
    detail = Details(id_master=user.id_search,
                     postal_code=postal_code, city=city)

    session.add(detail)
    session.commit()
    return {'status': "201 CREATED",
            'details': "Username "+username+ " with postal code "+postal_code+" and city "+city+" correctly created and added to the database"}, 201
