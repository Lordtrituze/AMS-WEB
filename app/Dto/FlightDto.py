from datetime import date, time


class RegisterFlightDto:
    aircraft_id: int
    takeoff_location: str
    destination: str
    departure_date: date
    arrival_time: time
    flight_number: str
    price: float
    date_created: date


class EditFlightDto:
    aircraft_id: int
    takeoff_location: str
    destination: str
    departure_date: date
    arrival_time: time
    price: float
    date_created: date
    date_updated: date


class ListFlightDto:
    aircraft_name: str
    takeoff_location: str
    destination: str
    departure_date: date
    arrival_time: time
    flight_number: str
    price: float
    date_created: date
    date_updated: date
    id: int


class FlightDetailsDto:
    aircraft_name: str
    takeoff_location: str
    destination: str
    departure_date: date
    arrival_time: time
    flight_number: str
    price: float
    date_created: date
    date_updated: date
    id: int


class SearchFlightDto:
    takeoff_location: str
    destination: str
    departure_date: date
    arrival_time: time
    id: int
