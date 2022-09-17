from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_login import login_required

from app_db import db
from model.models import Flight
from model.schemas import FlightSchema

flights_api = Blueprint('flights_api', __name__)


@flights_api.route('/', methods=["GET"])
@flights_api.route('/<flight_id>/', methods=["GET"])
def get_flights(flight_id=None):
    if flight_id:
        flight = db.find_one(Flight, 'id', flight_id)
        if flight is None:
            return 'No such flight', HTTPStatus.NOT_FOUND

        schema = FlightSchema().dump(flight)
        return jsonify(schema), HTTPStatus.OK

    limit = request.args.get('limit')
    offset = request.args.get('offset')

    limit = int(limit) if limit is not None else None
    offset = int(offset) if offset is not None else None

    flights = db.get_all(Flight, limit=limit, offset=offset)
    schema = FlightSchema(many=True).dump(flights)
    return jsonify(schema), HTTPStatus.OK


@flights_api.route('/', methods=["POST"])
@login_required
def create_flight():
    data = request.get_json()

    schema = FlightSchema()
    flight = schema.load(data)

    return jsonify(schema.dump(flight)), HTTPStatus.CREATED