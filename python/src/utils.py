import xml.etree.ElementTree as ET
import requests
import db
from models import Details, Master
import xmltodict
engine = db.engine
conn = engine.connect
session = db.session


def geoname(username: str, postal_code: str) -> str:

    URL = 'http://api.geonames.org/postalCodeSearch?api.geonames.org/postalCodeSearch?'
    data = {'username': username, 'postalcode': postal_code}

    r = requests.post(URL, data=data)
    tree = ET.fromstring(r.content)

    city = ""
    for name in tree.iter('name'):
        city = name.text
     
    if city == "":
        return {'error': "Error with GEONAMES API",'details': "user account has not been confirmed. Check your email for the confirmation email"}
    try: # Conexion con base de datos
        user = Master(username)
        session.add(user)
        session.commit()
        session.refresh(user)
        detail = Details(id_master=user.id_search,postal_code=postal_code, city=city)
        
        session.add(detail)
        session.commit()
    except Exception as ex:
        return {'error': "Error fetching database",'details': str(ex)}
        

    return str(r.status_code)
