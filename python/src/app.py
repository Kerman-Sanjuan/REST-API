from flask import Flask, request, render_template
from flask import jsonify
from flask_restful import Resource, Api
import db
from endpoint_geolocate import Geolocate

app = Flask(__name__)
db.Base.metadata.create_all(db.engine)
api = Api(app)

# Cada enpoint se define de esta manera. Con el correspondiente import.
api.add_resource(Geolocate, '/geolocate')


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(port=5000)
