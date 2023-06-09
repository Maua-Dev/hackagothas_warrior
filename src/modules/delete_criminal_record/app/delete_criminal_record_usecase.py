from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError


class DeleteCriminalRecordUsecase:
    def __init__(self, repository: ICriminalRecordRepository):
        self.repository = repository
    
    def __call__(self, criminal_record_id: int) -> CriminalRecord:
        if type(criminal_record_id) != int:
            raise EntityError("criminal_record_id")
        return self.repository.delete_criminal_record(criminal_record_id)