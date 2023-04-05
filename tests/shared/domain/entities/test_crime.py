import pytest
from src.shared.domain.entities.crime import Crime
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Crime():
    def test_crime(self):
        crime = Crime(crime_id=1, cryme_type=CRIME_TYPE.CATCHED_A_ROBIN, region=REGION_ENUM.NORTH)

        assert crime.crime_id == 1
        assert crime.cryme_type == CRIME_TYPE.CATCHED_A_ROBIN
        assert crime.region == REGION_ENUM.NORTH

    def test_crime_invalid_crime_id(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id='1', cryme_type=CRIME_TYPE.CATCHED_A_ROBIN, region=REGION_ENUM.NORTH)


    def test_crime_invalid_crime_type(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=1, cryme_type='CRIME_TYPE.CATCHED_A_ROBIN', region=REGION_ENUM.NORTH)

        
    def test_crime_invalid_region(self):
        with pytest.raises(EntityError):
            crime = Crime(crime_id=1, cryme_type=CRIME_TYPE.CATCHED_A_ROBIN, region='REGION_ENUM.NORTH')
