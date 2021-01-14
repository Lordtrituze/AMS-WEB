from abc import ABCMeta, abstractmethod
from typing import List

from app.Dto.SelectDto import SelectFlightDto
from app.models import Flight
from app.Dto.FlightDto import *


class FlightRepository(metaclass=ABCMeta):
    @abstractmethod
    def register_flight(self, model: RegisterFlightDto):
        raise NotImplementedError

    @abstractmethod
    def edit_flight(self, flight_id: int, model: EditFlightDto):
        raise NotImplementedError

    @abstractmethod
    def list_flight(self) -> List[ListFlightDto]:
        """List Flight Object"""
        raise NotImplementedError

    @abstractmethod
    def flight_details(self, flight_id: int) -> FlightDetailsDto:
        raise NotImplementedError

    @abstractmethod
    def delete_flight(self, flight_id: int):
        raise NotImplementedError

    @abstractmethod
    def search_flight(self, takeoff_location, destination, departure_date):
        raise NotImplementedError

    @abstractmethod
    def get_flight_list(self) -> [SelectFlightDto]:
        raise NotImplementedError


class DjangoORMFlightRepository(FlightRepository):
    def register_flight(self, model: RegisterFlightDto):
        flight = Flight()
        flight.aircraft_id = model.aircraft_id
        flight.takeoff_location = model.takeoff_location
        flight.destination = model.destination
        flight.departure_date = model.departure_date
        flight.arrival_time = model.arrival_time
        flight.flight_number = model.flight_number
        flight.price = model.price
        flight.date_created = model.date_created
        flight.save()

    def edit_flight(self, flight_id: int, model: EditFlightDto):
        try:
            flight = Flight.objects.get(id=flight_id)
            flight.aircraft_id = model.aircraft_id
            flight.takeoff_location = model.takeoff_location
            flight.destination = model.destination
            flight.departure_date = model.departure_date
            flight.arrival_time = model.arrival_time
            flight.price = model.price
            flight.save()
        except Flight.DoesNotExist as e:
            message = "Flight Does not exist"
            print(message)
            raise e

    def list_flight(self) -> List[ListFlightDto]:
        flights = list(
            Flight.objects.values('aircraft__aircraft_name', 'takeoff_location', 'destination', 'id'))
        results: List[ListFlightDto] = []
        for flight in flights:
            item = ListFlightDto()
            item.aircraft_name = flight['aircraft__aircraft_name']
            item.takeoff_location = flight['takeoff_location']
            item.destination = flight['destination']
            item.id = flight['id']
            results.append(item)
        return results

    def flight_details(self, flight_id: int) -> FlightDetailsDto:
        try:
            flight = Flight.objects.get(id=flight_id)
            result = FlightDetailsDto()
            result.aircraft_name = flight.aircraft.aircraft_name
            result.takeoff_location = flight.takeoff_location
            result.destination = flight.destination
            result.departure_date = flight.departure_date
            result.arrival_time = flight.arrival_time
            result.flight_number = flight.flight_number
            result.date_created = flight.date_created
            result.date_updated = flight.date_updated
            result.price = flight.price
            result.id = flight.id
            return result
        except Flight.DoesNotExist as e:
            raise e

    def delete_flight(self, flight_id: int):
        try:
            Flight.objects.get(id=flight_id).delete()
        except Flight.DoesNotExist as e:
            raise e

    def search_flight(self, takeoff_location, destination, departure_date):
        if departure_date is '':
            flights = Flight.objects.filter(takeoff_location=takeoff_location, destination=destination)
        else:
            flights = Flight.objects.filter(takeoff_location=takeoff_location).filter(destination=destination).filter(
                departure_date=departure_date)
        results: List[SearchFlightDto] = []
        for flight in flights:
            item = SearchFlightDto()
            item.takeoff_location = flight.takeoff_location
            item.destination = flight.destination
            item.departure_date = flight.departure_date
            item.arrival_time = flight.arrival_time
            item.id = flight.id
            results.append(item)
        return results

    def get_flight_list(self) -> [SelectFlightDto]:
        flights = list(Flight.objects.values('id', 'flight_number'))
        result: List[SelectFlightDto] = []
        for flight in flights:
            item = SelectFlightDto()
            item.id = flight['id']
            item.aircraft_name = flight['flight_number']
            result.append(item)
        return result
