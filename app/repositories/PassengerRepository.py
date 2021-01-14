
from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User

from app.models import Passenger
from app.Dto.PassengerDto import *


class PassengerRepository(metaclass=ABCMeta):
    @abstractmethod
    def register_passenger(self, model: RegisterPassengerDto):
        raise NotImplementedError

    @abstractmethod
    def edit_passenger(self, aircraft_id: int, model: EditPassengerDto):
        raise NotImplementedError

    @abstractmethod
    def list_passenger(self) -> List[ListPassengerDto]:
        """List Passenger Object"""
        raise NotImplementedError

    @abstractmethod
    def passenger_details(self, passenger_id: int) -> PassengerDetailsDto:
        raise NotImplementedError

    @abstractmethod
    def delete_passenger(self, passenger_id: int):
        raise NotImplementedError


class DjangoORMPassengerRepository(PassengerRepository):
    def register_passenger(self, model: RegisterPassengerDto):
        passenger = Passenger()
        passenger.phone = model.phone
        passenger.address = model.address
        passenger.reg_no = model.reg_no

        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()
        passenger.user = user

        passenger.save()

    def edit_passenger(self, passenger_id: int, model: EditPassengerDto):
        try:
            passenger = Passenger.objects.get(id=passenger_id)
            passenger.phone = model.phone
            passenger.address = model.address
            # passenger.save()
            # user_id = passenger.user_id
            # user = User.objects.get(id=user_id)
            # user.first_name = model.first_name
            # user.last_name = model.last_name
            # user.email = model.email
            # user.username = model.username
            # user.save()
            passenger.user.first_name = model.first_name
            passenger.user.last_name = model.last_name
            passenger.user.username = model.username
            passenger.user.email = model.email
            passenger.user.save()
            passenger.save()

        except Passenger.DoesNotExist as e:
            message = "Passenger Does not exist"
            print(message)
            raise e

    def list_passenger(self) -> List[ListPassengerDto]:
        passenger = list(
            Passenger.objects.values('id', 'user__first_name', 'user__last_name', 'user__email', 'phone'))
        results: List[ListPassengerDto] = []
        for person in passenger:
            item = ListPassengerDto()
            item.first_name = person['user__first_name']
            item.last_name = person['user__last_name']
            item.email = person['user__email']
            item.phone = person['phone']
            item.id = person['id']
            results.append(item)
        return results

    def passenger_details(self, passenger_id: int) -> PassengerDetailsDto:
        try:
            passenger = Passenger.objects.get(id=passenger_id)
            result = PassengerDetailsDto()
            result.first_name = passenger.user.first_name
            result.last_name = passenger.user.last_name
            result.username = passenger.user.username
            result.email = passenger.user.email
            result.phone = passenger.phone
            result.address = passenger.address
            result.reg_no = passenger.reg_no
            result.id = passenger.id
            return result
        except Passenger.DoesNotExist as e:
            raise e

    def delete_passenger(self, passenger_id: int):
        try:
            Passenger.objects.get(id=passenger_id).delete()
        except Passenger.DoesNotExist as e:
            raise e
