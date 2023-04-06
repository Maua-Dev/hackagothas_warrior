from typing import List
from abc import ABC, abstractmethod
from src.shared.domain.entities.criminal_record import CriminalRecord


class ICriminalRecordRepository(ABC):

    @abstractmethod
    def get_all_criminal_records(self) -> List[CriminalRecord]:
        pass

    @abstractmethod
    def get_criminal_record(self, criminal_record_id:int) -> CriminalRecord:
        pass

    @abstractmethod
    def get_criminal_record_by_villain(self, villain_id:int) -> List[CriminalRecord]:
        pass
    
    @abstractmethod
    def create_criminal_record(self, criminal_record:CriminalRecord) -> CriminalRecord:
        pass

    @abstractmethod
    def delete_criminal_record(self, criminal_record_id:int) -> CriminalRecord:
        pass

    @abstractmethod
    def update_criminal_record(self, new_criminal_record:CriminalRecord) -> CriminalRecord:
        pass