from abc import ABCMeta, abstractmethod
from typing import List

from app.Dto.BookingDto import *
from app.repositories.BookingRepository import BookingRepository


class BookingManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register_booking(self, model: RegisterBookingDto):
        raise NotImplementedError

    @abstractmethod
    def edit_booking(self, booking_id: int, model: EditBookingDto):
        raise NotImplementedError

    @abstractmethod
    def list_booking(self) -> List[ListBookingDto]:
        raise NotImplementedError

    @abstractmethod
    def booking_details(self, booking_id: int) -> BookingDetailsDto:
        raise NotImplementedError


class DefaultBookingManagementService(BookingManagementService):
    repository: BookingRepository

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def register_booking(self, model: RegisterBookingDto):
        return self.repository.register_booking(model)

    def edit_booking(self, booking_id: int, model: EditBookingDto):
        return self.repository.edit_booking(booking_id, model)

    def list_booking(self) -> List[ListBookingDto]:
        return self.repository.list_booking()

    def booking_details(self, booking_id: int) -> BookingDetailsDto:
        return self.repository.booking_details(booking_id)

    def delete_booking(self, booking_id: int):
        return self.repository.delete_booking(booking_id)