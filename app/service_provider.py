from typing import Callable

from dependency_injector import containers, providers

from app.repositories.FlightRepository import FlightRepository, DjangoORMFlightRepository
from app.repositories.AircraftRepository import AircraftRepository, DjangoORMAircraftRepository
from app.services.AircraftManagementService import AircraftManagementService, DefaultAircraftManagementService
from app.services.FlightManagementService import FlightManagementService, DefaultFlightManagementService
from app.services.PassengerManagementService import PassengerManagementService, DefaultPassengerManagementService
from app.repositories.PassengerRepository import PassengerRepository, DjangoORMPassengerRepository
from app.repositories.StaffRepository import DjangoORMStaffRepository, StaffRepository
from app.services.StaffManagementService import StaffManagementService, DefaultStaffManagementService


class Container(containers.DeclarativeContainer):
    aircraft_repository: Callable[[], AircraftRepository] = providers.Factory(
        DjangoORMAircraftRepository
    )
    aircraft_management_service: Callable[[], AircraftManagementService] = providers.Factory(
        DefaultAircraftManagementService,
        repository=aircraft_repository
    )

    passenger_repository: Callable[[], PassengerRepository] = providers.Factory(
        DjangoORMPassengerRepository
    )
    passenger_management_service: Callable[[], PassengerManagementService] = providers.Factory(
        DefaultPassengerManagementService,
        repository=passenger_repository
    )
    flight_repository: Callable[[], FlightRepository] = providers.Factory(DjangoORMFlightRepository)
    flight_management_service: Callable[[], FlightManagementService] = providers.Factory(
        DefaultFlightManagementService, repository=flight_repository
    )

    staff_repository: Callable[[], StaffRepository] = providers.Factory(
        DjangoORMStaffRepository
    )
    staff_management_service: Callable[[], StaffManagementService] = providers.Factory(
        DefaultStaffManagementService,
        repository=staff_repository
    )


app_service_provider = Container()

