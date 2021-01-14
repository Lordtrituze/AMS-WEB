from datetime import date


class RegisterBookingDto:
    flight_id: int
    passenger_id: int
    flight_class: str
    price: float
    booking_reference: str
    date_created: date


class EditBookingDto:
    flight_id: int
    passenger_id: int
    flight_class: str
    price: float
    id: int


class ListBookingDto:
    flight_number: str
    passenger_name: str
    flight_class: str
    price: float
    booking_reference: str
    id: int


class BookingDetailsDto:
    flight_number: str
    passenger_name: str
    flight_class: str
    price: float
    booking_reference: str
    id: int
    date_created: date
    date_updated: date


