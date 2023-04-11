from typing import List
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.entities.villain import Villain
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.genre_enum import GENRE_ENUM
from src.shared.domain.enums.powers_type_enum import POWERS_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM


class VillainViewmodel:
    villain_id: int
    name: str
    description: str
    genre: GENRE_ENUM
    region: REGION_ENUM
    powers: List[POWERS_TYPE]
    is_arrested: bool

    def __init__(self, villain: Villain):
        self.villain_id = villain.villain_id
        self.name = villain.name
        self.description = villain.description
        self.genre = villain.genre
        self.region = villain.region
        self.powers = villain.powers
        self.is_arrested = villain.is_arrested

    def to_dict(self):
        return {
            'villain_id': self.villain_id,
            'name': self.name,
            'description': self.description,
            'genre': self.genre.value,
            'region': self.region.value,
            'powers': [power.value for power in self.powers],
            'is_arrested': self.is_arrested
        }
    
class CrimeViewmodel:
    crime_type: CRIME_TYPE
    region: REGION_ENUM

    def __init__(self, crime: Crime):
        self.crime_type = crime.crime_type
        self.region = crime.region


    def to_dict(self):
        return {
            'crime_type': self.crime_type.value,
            'region': self.region.value
        }


class GetCriminalRecordViewmodel:
    criminal_record_id: int
    villain: VillainViewmodel
    crimes: List[CrimeViewmodel]

    def __init__(self, criminal_record: CriminalRecord):
        self.criminal_record_id = criminal_record.criminal_record_id
        self.villain = VillainViewmodel(criminal_record.villain)
        self.crimes = [CrimeViewmodel(crime) for crime in criminal_record.crimes]

    def to_dict(self):
        return {
            'criminal_record_id': self.criminal_record_id,
            'villain': self.villain.to_dict(),
            'crimes': [crime.to_dict() for crime in self.crimes],
            'message': "the criminal_record was retrieved successfully"
        }