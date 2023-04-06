from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CriminalRecordRepositoryMock:
    def test_get_all_criminal_records(self):
        repo = CriminalRecordRepositoryMock()
        criminal_records = repo.get_all_criminal_records()

        assert len(criminal_records) == len(repo.crimialRecordList)
    
    def test_get_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.get_criminal_record(1)

        assert criminal_record.criminal_record_id == 1
    
    def test_get_criminal_record_by_villain(self):
        repo = CriminalRecordRepositoryMock()
        criminal_records = repo.get_criminal_record_by_villain(1)

        assert len(criminal_records) == 2

    def test_create_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        new_criminal_record = repo.create_criminal_record(repo.crimialRecordList[0])

        assert new_criminal_record.criminal_record_id == 1
    
    def test_delete_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.delete_criminal_record(1)

        assert criminal_record.criminal_record_id == 1
    
    def test_update_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.update_criminal_record(repo.crimialRecordList[0])

        assert criminal_record.criminal_record_id == 1