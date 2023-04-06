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
            'villain': {
                'villain_id': self.villain.villain_id,
                'name': self.villain.name,
                'description': self.villain.description,
                'genre': self.villain.genre,
                'region': self.villain.region,
                'powers': self.villain.powers,
                'is_arrested': self.villain.is_arrested
            },
            'crimes': self.crimes,
            'message': "the criminal_record was retrieved successfully"
        }