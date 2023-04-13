import pytest
from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_DeleteCriminalRecordUsecase:
    def test_delete_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)
        lenBefore = len(repo.criminal_records_list)

        report = usecase(1)

        assert len(repo.criminal_records_list) == lenBefore - 1
    
    def test_delete_user_not_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)

        with pytest.raises(NoItemsFound):
            report = usecase(69)

    def test_delete_criminal_record_invalid_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            report = usecase("invalid")