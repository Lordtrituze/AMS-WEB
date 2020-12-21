from datetime import date


class RegisterAircraftDto:
    aircraft_name: str
    aircraft_type: str
    aircraft_capacity: int
    aircraft_no: str
    date_created: date


class EditAircraftDto:
    aircraft_name: str
    aircraft_type: str
    aircraft_capacity: int
    aircraft_no: str
    date_updated: date


class ListAircraftDto:
    aircraft_name: str
    aircraft_type: str
    aircraft_capacity: int
    aircraft_no: str
    date_created: date
    date_updated: date
    id: int


class AircraftDetailsDto:
    aircraft_name: str
    aircraft_type: str
    aircraft_capacity: int
    aircraft_no: str
    date_created: date
    date_updated: date
    id: int


