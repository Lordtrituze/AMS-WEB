
class RegisterPassengerDto:
    first_name: str
    last_name: str
    username: str
    email: str
    phone: int
    address: str
    reg_no: str
    password: str
    confirm_password: str


class EditPassengerDto:
    first_name: str
    last_name: str
    username: str
    email: str
    phone: int
    address: str


class ListPassengerDto:
    first_name: str
    last_name: str
    email: str
    phone: int
    address: str
    reg_no: str
    id: int


class PassengerDetailsDto:
    first_name: str
    last_name: str
    username: str
    email: str
    phone: int
    address: str
    reg_no: str
    id: int


