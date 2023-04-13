from typing import List
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.entities.villain import Villain
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.genre_enum import GENRE_ENUM
from src.shared.domain.enums.powers_type_enum import POWERS_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class CriminalRecordRepositoryMock(ICriminalRecordRepository):

    criminal_records_list = []

    villain_01 = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
    villain_02 = Villain(villain_id=2, name="Bane", description="Viagra Foda", genre=GENRE_ENUM.MALE, region=REGION_ENUM.EAST, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)
    villain_03 = Villain(villain_id=3, name="Arlequina", description="Margot Robbie", genre=GENRE_ENUM.FEMALE, region=REGION_ENUM.SOUTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)
    criminalRecord = CriminalRecord(criminal_record_id=1, villain=villain_01, crimes=[Crime(crime_type=CRIME_TYPE.MURDER, region=REGION_ENUM.NORTH)])

    def __init__(self):
        self.criminal_records_list = [
            CriminalRecord(1, self.villain_01, [Crime(crime_type=CRIME_TYPE.CATCHED_A_ROBIN, region=REGION_ENUM.NORTH)]),
            CriminalRecord(2, self.villain_02, [Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]),
            CriminalRecord(3, self.villain_01, [Crime(crime_type=CRIME_TYPE.MURDER, region=REGION_ENUM.NORTH)]),
            CriminalRecord(4, self.villain_03, [Crime(crime_type=CRIME_TYPE.GANG_FORMATION, region=REGION_ENUM.NORTH)]),
            CriminalRecord(5, self.villain_03, [Crime(crime_type=CRIME_TYPE.MURDER, region=REGION_ENUM.NORTH)]),
        ]

    def get_all_criminal_records(self):
        return self.criminal_records_list

    def get_criminal_record(self, criminal_record_id:int):
        for record in self.criminal_records_list:
            if record.criminal_record_id == criminal_record_id:
                return record
        raise NoItemsFound("criminal_record_id")

    def get_criminal_record_by_villain(self, villain_id:int):
        recordList = []
        for record in self.criminal_records_list:
            if record.villain.villain_id == villain_id:
                recordList.append(record)
        return recordList

    def create_criminal_record(self, new_criminal_record:CriminalRecord):
        self.criminal_records_list.append(new_criminal_record)
        return new_criminal_record

    def delete_criminal_record(self, criminal_record_id:int):
        for idx, record in enumerate(self.criminal_records_list):
            if record.criminal_record_id == criminal_record_id:
                return self.criminal_records_list.pop(idx)
        raise NoItemsFound("criminal_record_id")

    def update_criminal_record(self, new_criminal_record:CriminalRecord):
        for record in self.criminal_records_list:
            if record.criminal_record_id == new_criminal_record.criminal_record_id:
                record = new_criminal_record
                return record
        raise NoItemsFound("criminal_record_id")