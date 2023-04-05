import abc

from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM
from src.shared.helpers.errors.domain_errors import EntityError


class Crime(abc.ABC):
    crime_id: int
    crime_type: CRIME_TYPE
    region: REGION_ENUM

    def __init__(self, crime_id: int, crime_type: CRIME_TYPE, region: REGION_ENUM):
        if type(crime_id) != int:
            raise EntityError("id")
        self.crime_id = crime_id

        if type(crime_type) != CRIME_TYPE:
            raise EntityError("crime_type")
        self.crime_type = crime_type

        if type(region) != REGION_ENUM:
            raise EntityError("region")
        self.region = region
        