import pytest
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.entities.villain import Villain
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.genre_enum import GENRE_ENUM
from src.shared.domain.enums.powers_type_enum import POWERS_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM
from src.shared.helpers.errors.domain_errors import EntityError


class Test_CriminalRecord():
    
    def test_criminal_record(self):
        villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)
        criminalRecord = CriminalRecord(criminal_record_id=1, villain=villain, crimes=[CRIME_TYPE.MURDER])

        assert criminalRecord.criminal_record_id == 1
        assert criminalRecord.villain == villain
        assert criminalRecord.crimes == [CRIME_TYPE.MURDER]
    
    def test_criminal_report_invalid_id(self):
        villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)
        with pytest.raises(EntityError):
            criminalRecord = CriminalRecord(criminal_record_id='1', villain=villain, crimes=[CRIME_TYPE.MURDER])
    
    def test_criminal_report_invalid_villain(self):
        with pytest.raises(EntityError):
            criminalRecord = CriminalRecord(criminal_record_id=1, villain='villain', crimes=[CRIME_TYPE.MURDER])
    
    def test_criminal_report_invalid_crime(self):
        villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)
        with pytest.raises(EntityError):
            criminalRecord = CriminalRecord(criminal_record_id=1, villain=villain, crimes='[CRIME_TYPE.MURDER]')

        