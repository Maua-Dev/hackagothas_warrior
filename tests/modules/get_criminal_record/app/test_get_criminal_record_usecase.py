import pytest
from src.modules.get_criminal_record.app.get_criminal_record_usecase import GetCriminalRecordUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordUsecase:

    def test_get_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repo)
        criminal_record = usecase(criminal_record_id=repo.criminal_records_list[0].criminal_record_id)

        assert repo.criminal_records_list[0] == criminal_record

    def test_get_criminal_record_not_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repo)

        with pytest.raises(NoItemsFound):
           criminal_record = usecase(criminal_record_id=999)
    
    def test_get_criminal_record_invalid_parameter(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            criminal_record = usecase(criminal_record_id="invalid")