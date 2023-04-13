from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.enums.genre_enum import GENRE_ENUM
from src.shared.domain.enums.region_enum import REGION_ENUM
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError


class CreateCriminalRecordUsecase:
    def __init__(self, repository: ICriminalRecordRepository):
        self.repository = repository

    def __call__(self, criminal_record: CriminalRecord) -> CriminalRecord:
        if not criminal_record.criminal_record_id != int:
            raise EntityError("criminal_record_id")
        if not criminal_record.villain.villain_id != int:
            raise EntityError("villain_id")
        if not criminal_record.villain.validate_name(criminal_record.villain.name):
            raise EntityError("name")
        if not criminal_record.villain.description != str:
            raise EntityError("description")
        if not criminal_record.villain.genre != GENRE_ENUM:
            raise EntityError("genre")
        if not criminal_record.villain.region != REGION_ENUM:
            raise EntityError("region")
        if not criminal_record.villain.validate_powers(criminal_record.villain.powers):
            raise EntityError("powers")
        if not criminal_record.villain.is_arrested != bool:
            raise EntityError("is_arrested")
        if not criminal_record.crimes != list:
            raise EntityError("crimes")
        return self.repository.create_criminal_record(criminal_record)