
from abc import ABCMeta, abstractmethod, ABC
from typing import List

from app.models import Booking
from app.Dto.BookingDto import *


class BookingRepository(metaclass=ABCMeta):
    @abstractmethod
    def register_booking(self, model: RegisterBookingDto):
        raise NotImplementedError

    @abstractmethod
    def edit_booking(self, booking_reference: int, model: EditBookingDto):
        raise NotImplementedError

    @abstractmethod
    def list_booking(self) -> List[ListBookingDto]:
        """List Booking Object"""
        raise NotImplementedError

    @abstractmethod
    def booking_details(self, booking_reference: int) -> BookingDetailsDto:
        raise NotImplementedError

    @abstractmethod
    def delete_booking(self, booking_reference: int):
        raise NotImplementedError


class DjangoORMBookingRepository(BookingRepository):
    def register_booking(self, model: RegisterBookingDto):
        booking = Booking()
        booking.flight_id = model.flight_id
        booking.passenger_id = model.passenger_id
        booking.flight_class = model.flight_class
        booking.price = model.price
        booking.booking_reference = model.booking_reference
        booking.save()

    def edit_booking(self, booking_reference: int, model: EditBookingDto):
        try:
            booking = Booking.objects.get(id=booking_reference)
            booking.flight_id = model.flight_id
            booking.passenger_id = model.passenger_id
            booking.flight_class = model.flight_class
            booking.price = model.price
            booking.save()
        except Booking.DoesNotExist as e:
            message = "Booking Does not exist"
            print(message)
            raise e

    def list_booking(self) -> List[ListBookingDto]:
        bookings = list(
            Booking.objects.values('passenger__users__first_name', 'flight__flight_number', 'flight_class'))
        results: List[ListBookingDto] = []
        for booking in bookings:
            item = ListBookingDto()
            item.passenger_name = booking['passenger__users__first_name']
            item.flight_number = booking['flight__flight_number']
            item.flight_class = booking['flight_class']
            results.append(item)
        return results

    def booking_details(self, booking_id: int) -> BookingDetailsDto:
        try:
            booking = Booking.objects.get(id=booking_id)
            result = BookingDetailsDto()
            result.flight_number = booking.flight.flight_number
            result.flight_class = booking.flight_class
            result.passenger_name = booking.passenger.users.first_name
            result.price = booking.price
            result.booking_reference = booking.booking_reference
            result.id = booking.id
            return result
        except Booking.DoesNotExist as e:
            raise e

    def delete_booking(self, booking_reference: int):
        try:
            Booking.objects.get(id=booking_reference).delete()
        except Booking.DoesNotExist as e:
            raise e
