import pytest
from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUsecase
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.entities.villain import Villain
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.genre_enum import GENRE_ENUM
from src.shared.domain.enums.powers_type_enum import POWERS_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordUsecase:
    def test_update_criminal_record(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
        record = CriminalRecord(criminal_record_id=repo.criminal_records_list[1].criminal_record_id, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)])
        record_update = usecase(record)

        assert repo.criminal_records_list[1].villain.name == "Pinguim"
    
    def test_update_criminal_record_invalid_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)

        with pytest.raises(EntityError):
            usecase(CriminalRecord(criminal_record_id="0", villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]))

    def test_update_criminal_record_invalid_villain_id(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            villain = Villain(villain_id="1", name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
            usecase(CriminalRecord(criminal_record_id=0, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]))

    def test_update_criminal_record_invalid_villain_name(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name=0, description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
            usecase(CriminalRecord(criminal_record_id=0, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]))

    def test_update_criminal_record_invalid_villain_description(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description=0, genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
            usecase(CriminalRecord(criminal_record_id=0, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]))

    def test_update_criminal_record_invalid_villain_genre(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=0, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
            usecase(CriminalRecord(criminal_record_id=0, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]))

    def test_update_criminal_record_invalid_villain_region(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=1, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
            usecase(CriminalRecord(criminal_record_id=0, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]))

    def test_update_criminal_record_invalid_villain_powers(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=0, is_arrested=True)
            usecase(CriminalRecord(criminal_record_id=0, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]))


    def test_update_criminal_record_invalid_villain_is_arrested(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=0)
            usecase(CriminalRecord(criminal_record_id=0, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)]))

    def test_update_criminal_record_invalid_crimes(self):
        repo = CriminalRecordRepositoryMock()
        usecase = UpdateCriminalRecordUsecase(repo)

        with pytest.raises(EntityError):
            villain = Villain(villain_id="1", name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
            usecase(CriminalRecord(criminal_record_id=0, villain=villain, crimes=0))
