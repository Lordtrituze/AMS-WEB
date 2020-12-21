from abc import ABCMeta, abstractmethod
from typing import List
from app.Dto.StaffDto import *
from app.repositories.StaffRepository import StaffRepository


class StaffManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register_staff(self, model: RegisterStaffDto):
        raise NotImplementedError

    @abstractmethod
    def edit_staff(self, staff_id: int, model: EditStaffDto):
        raise NotImplementedError

    @abstractmethod
    def list_staff(self) -> List[ListStaffDto]:
        raise NotImplementedError

    @abstractmethod
    def staff_details(self, staff_id: int) -> StaffDetailsDto:
        raise NotImplementedError


class DefaultStaffManagementService(StaffManagementService):
    repository: StaffRepository

    def __init__(self, repository: StaffRepository):
        self.repository = repository

    def register_staff(self, model: RegisterStaffDto):
        return self.repository.register_staff(model)

    def edit_staff(self, staff_id: int, model: EditStaffDto):
        return self.repository.edit_staff(staff_id, model)

    def list_staff(self) -> List[ListStaffDto]:
        return self.repository.list_staff()

    def staff_details(self, staff_id: int) -> StaffDetailsDto:
        return self.repository.staff_details(staff_id)

    def delete_staff(self, staff_id: int):
        return self.repository.delete_staff(staff_id)
