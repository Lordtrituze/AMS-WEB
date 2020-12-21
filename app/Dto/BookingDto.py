
class RegisterBookingDto:
    flight_id: int
    passenger_id: int
    flight_class: str
    price: float
    booking_reference: str


class EditBookingDto:
    flight_id: int
    passenger_id: int
    flight_class: str
    price: float


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


