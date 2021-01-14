from abc import ABCMeta, abstractmethod
from typing import List

from app.Dto.SelectDto import SelectAircraftDto
from app.models import Aircraft
from app.Dto.AircraftDto import *


class AircraftRepository(metaclass=ABCMeta):
    @abstractmethod
    def register_aircraft(self, model: RegisterAircraftDto):
        raise NotImplementedError

    @abstractmethod
    def edit_aircraft(self, aircraft_id: int, model: EditAircraftDto):
        raise NotImplementedError

    @abstractmethod
    def list_aircraft(self) -> List[ListAircraftDto]:
        """List Aircraft Object"""
        raise NotImplementedError

    @abstractmethod
    def aircraft_details(self, aircraft_id: int) -> AircraftDetailsDto:
        raise NotImplementedError

    @abstractmethod
    def delete_aircraft(self, aircraft_id: int):
        raise NotImplementedError

    @abstractmethod
    def get_aircraft_list(self) -> [SelectAircraftDto]:
        raise NotImplementedError


class DjangoORMAircraftRepository(AircraftRepository):
    def register_aircraft(self, model: RegisterAircraftDto):
        aircraft = Aircraft()
        aircraft.aircraft_name = model.aircraft_name
        aircraft.aircraft_type = model.aircraft_type
        aircraft.aircraft_capacity = model.aircraft_capacity
        aircraft.aircraft_no = model.aircraft_no
        aircraft.date_created = model.date_created
        aircraft.save()

    def edit_aircraft(self, aircraft_id: int, model: EditAircraftDto):
        try:
            aircraft = Aircraft.objects.get(id=aircraft_id)
            aircraft.aircraft_name = model.aircraft_name
            aircraft.aircraft_type = model.aircraft_type
            aircraft.aircraft_capacity = model.aircraft_capacity
            aircraft.date_updated = model.date_updated
            aircraft.save()
        except Aircraft.DoesNotExist as e:
            message = "Aircraft Does not exist"
            print(message)
            raise e

    def list_aircraft(self) -> List[ListAircraftDto]:
        aircraft = list(
            Aircraft.objects.values('aircraft_name', 'aircraft_type', 'aircraft_capacity', 'aircraft_no',
                                    'date_created', 'date_updated', 'id'))
        results: List[ListAircraftDto] = []
        for craft in aircraft:
            item = ListAircraftDto()
            item.aircraft_name = craft['aircraft_name']
            item.aircraft_type = craft['aircraft_type']
            item.aircraft_no = craft['aircraft_no']
            item.aircraft_capacity = craft['aircraft_capacity']
            item.date_created = craft['date_created']
            item.date_updated = craft['date_updated']
            item.id = craft['id']
            results.append(item)
        return results

    def aircraft_details(self, aircraft_id: int) -> AircraftDetailsDto:
        try:
            aircraft = Aircraft.objects.get(id=aircraft_id)
            result = AircraftDetailsDto()
            result.aircraft_name = aircraft.aircraft_name
            result.aircraft_type = aircraft.aircraft_type
            result.aircraft_capacity = aircraft.aircraft_capacity
            result.aircraft_no = aircraft.aircraft_no
            result.date_created = aircraft.date_created
            result.date_updated = aircraft.date_updated
            result.id = aircraft_id
            return result
        except Aircraft.DoesNotExist as e:
            raise e

    def delete_aircraft(self, aircraft_id: int):
        try:
            Aircraft.objects.get(id=aircraft_id).delete()
        except Aircraft.DoesNotExist as e:
            raise e

    def get_aircraft_list(self) -> [SelectAircraftDto]:
        aircrafts = list(Aircraft.objects.values('id', 'aircraft_name'))
        result: List[SelectAircraftDto] = []
        for aircraft in aircrafts:
            item = SelectAircraftDto()
            item.id = aircraft['id']
            item.aircraft_name = aircraft['aircraft_name']
            result.append(item)
        return result
