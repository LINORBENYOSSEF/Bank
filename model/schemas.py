import uuid

from marshmallow import Schema, fields, post_load

from model.models import Flight
from app_db import db


class AirlineSchema(Schema):
    name = fields.Str(required=True)


class LocationSchema(Schema):
    code = fields.Str(required=True)
    city = fields.Str(required=True)
    country = fields.Str(required=True)


class FlightSchema(Schema):
    id = fields.Str(dump_only=True)
    airline = fields.Nested(AirlineSchema, required=True)
    departure_time = fields.DateTime(required=True)
    departure = fields.Nested(LocationSchema, required=True)
    destination = fields.Nested(LocationSchema, required=True)
    ticket_cost = fields.Float(required=True)

    @post_load
    def create_flight(self, data, **kwargs):
        flight = Flight(**data)
        flight.id = str(uuid.uuid4())
        flight.passengers = []

        db.add(flight)

        return flight
