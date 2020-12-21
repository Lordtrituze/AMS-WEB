from datetime import date


class RegisterFlightDto:
    aircraft_id: int
    takeoff_location: str
    destination: str
    departure_date: date
    arrival_time: date
    flight_number: str
    price: float
    date_created: date


class EditFlightDto:
    aircraft_id: int
    takeoff_location: str
    destination: str
    departure_date: date
    arrival_time: date
    price: float


class ListFlightDto:
    aircraft_name: str
    takeoff_location: str
    destination: str
    departure_date: date
    arrival_time: date
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
    arrival_time: date
    flight_number: str
    price: float
    date_created: date
    date_updated: date
    id: int
