from datetime import datetime
from flask_login import UserMixin

from .base import Model, Column


class User(UserMixin, Model):
    id = Column(str)
    username = Column(str)
    password = Column(str)


class Plane(Model):
    manufacturer = Column(str)
    model = Column(str)
    capacity = Column(int)


class Airline(Model):
    name = Column(str)


class PassengerBooking(Model):
    passenger_id = Column(str)
    flight_id = Column(str)


class Passenger(Model):
    id = Column(str)
    name = Column(str)
    bookings = Column(PassengerBooking, is_many=True)


class Location(Model):
    code = Column(str)
    city = Column(str)
    country = Column(str)


class Flight(Model):
    id = Column(str)
    airline = Column(Airline)
    plane = Column(Plane)
    passengers = Column(Passenger, is_many=True)
    departure_time = Column(datetime)
    departure = Column(Location)
    destination = Column(Location)
    ticket_cost = Column(float)
