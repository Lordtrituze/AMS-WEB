from abc import ABCMeta, abstractmethod
from typing import List

from app.Dto.AircraftDto import *
from app.Dto.SelectDto import SelectAircraftDto
from app.repositories.AircraftRepository import AircraftRepository


class AircraftManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register_aircraft(self, model: RegisterAircraftDto):
        raise NotImplementedError

    @abstractmethod
    def edit_aircraft(self, aircraft_id: int, model: EditAircraftDto):
        raise NotImplementedError

    @abstractmethod
    def list_aircraft(self) -> List[ListAircraftDto]:
        raise NotImplementedError

    @abstractmethod
    def aircraft_details(self, aircraft_id: int) -> AircraftDetailsDto:
        raise NotImplementedError

    @abstractmethod
    def get_aircraft_list(self) -> [SelectAircraftDto]:
        raise NotImplementedError


class DefaultAircraftManagementService(AircraftManagementService):
    repository: AircraftRepository

    def __init__(self, repository: AircraftRepository):
        self.repository = repository

    def register_aircraft(self, model: RegisterAircraftDto):
        return self.repository.register_aircraft(model)

    def edit_aircraft(self, aircraft_id: int, model: EditAircraftDto):
        return self.repository.edit_aircraft(aircraft_id, model)

    def list_aircraft(self) -> List[ListAircraftDto]:
        return self.repository.list_aircraft()

    def aircraft_details(self, aircraft_id: int) -> AircraftDetailsDto:
        return self.repository.aircraft_details(aircraft_id)

    def delete_aircraft(self, aircraft_id: int):
        return  self.repository.delete_aircraft(aircraft_id)

    def get_aircraft_list(self) -> [SelectAircraftDto]:
        return  self.repository.get_aircraft_list()