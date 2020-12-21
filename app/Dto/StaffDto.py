from datetime import date


class RegisterStaffDto:
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    username: str
    role: str
    department: str
    date_of_employment: date


class EditStaffDto:
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    role: str
    department: str


class ListStaffDto:
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    role: str
    department: str
    date_of_employment: date


class StaffDetailsDto:
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    role: str
    department: str
    date_of_employment: date