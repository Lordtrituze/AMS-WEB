from abc import ABCMeta, abstractmethod
from typing import List

from app.models import Aircraft
from app.Dto.PassengerDto import *
from app.repositories.PassengerRepository import PassengerRepository


class PassengerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register_passenger(self, model: RegisterPassengerDto):
        raise NotImplementedError

    @abstractmethod
    def edit_passenger(self, passenger_id: int, model: EditPassengerDto):
        raise NotImplementedError

    @abstractmethod
    def list_passenger(self) -> List[ListPassengerDto]:
        raise NotImplementedError

    @abstractmethod
    def passenger_details(self, passenger_id: int) -> PassengerDetailsDto:
        raise NotImplementedError


class DefaultPassengerManagementService(PassengerManagementService):
    repository: PassengerRepository

    def __init__(self, repository: PassengerRepository):
        self.repository = repository

    def register_passenger(self, model: RegisterPassengerDto):
        return self.repository.register_passenger(model)

    def edit_passenger(self, passenger_id: int, model: EditPassengerDto):
        return self.repository.edit_passenger(passenger_id, model)

    def list_passenger(self) -> List[ListPassengerDto]:
        return self.repository.list_passenger()

    def passenger_details(self, passenger_id: int) -> PassengerDetailsDto:
        return self.repository.passenger_details(passenger_id)

    def delete_passenger(self, passenger_id: int):
        return  self.repository.delete_passenger(passenger_id)
