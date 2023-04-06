from typing import List
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.entities.villain import Villain


class GetCriminalRecordViewmodel:
    criminal_record_id: int
    villain: Villain
    crimes: List[Crime]

    def __init__(self, criminal_record: CriminalRecord):
        self.criminal_record_id = criminal_record.criminal_record_id
        self.villain = criminal_record.villain
        self.crimes = criminal_record.crimes

    def to_dict(self):
        return {
            'criminal_record_id': self.criminal_record_id,
            'villain': self.villain,
            'crimes': self.crimes,
            'message': "the criminal_record was retrieved successfully"
        }