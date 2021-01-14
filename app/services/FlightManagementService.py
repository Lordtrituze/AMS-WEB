from abc import ABCMeta, abstractmethod
from typing import List

from app.Dto.FlightDto import *
from app.Dto.SelectDto import SelectFlightDto
from app.repositories.FlightRepository import FlightRepository


class FlightManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register_flight(self, model: RegisterFlightDto):
        raise NotImplementedError

    @abstractmethod
    def edit_flight(self, flight_id: int, model: EditFlightDto):
        raise NotImplementedError

    @abstractmethod
    def list_flight(self) -> List[ListFlightDto]:
        raise NotImplementedError

    @abstractmethod
    def flight_details(self, flight_id: int) -> FlightDetailsDto:
        raise NotImplementedError

    @abstractmethod
    def get_flight_list(self) -> [SelectFlightDto]:
        raise NotImplementedError


class DefaultFlightManagementService(FlightManagementService):
    repository: FlightRepository

    def __init__(self, repository: FlightRepository):
        self.repository = repository

    def register_flight(self, model: RegisterFlightDto):
        return self.repository.register_flight(model)

    def edit_flight(self, flight_id: int, model: EditFlightDto):
        return self.repository.edit_flight(flight_id, model)

    def list_flight(self) -> List[ListFlightDto]:
        return self.repository.list_flight()

    def flight_details(self, flight_id: int) -> FlightDetailsDto:
        return self.repository.flight_details(flight_id)

    def delete_flight(self, flight_id: int):
        return self.repository.delete_flight(flight_id)

    def search_flight(self, takeoff_location, destination, departure_date):
        return self.repository.search_flight(takeoff_location, destination, departure_date)

    def get_flight_list(self) -> [SelectFlightDto]:
        return self.repository.get_flight_list()
