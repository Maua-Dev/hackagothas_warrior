import abc
from typing import List

from src.shared.domain.enums.genre_enum import GENRE_ENUM
from src.shared.domain.enums.powers_type_enum import POWERS_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM
from src.shared.helpers.errors.domain_errors import EntityError


class Villain(abc.ABC):
    villain_id: int
    name: str
    description: str
    genre: GENRE_ENUM
    region: REGION_ENUM
    powers: List[POWERS_TYPE]
    is_arrested: bool

    def __init__(self, villain_id: int, name: str, description: str, genre: GENRE_ENUM, region: REGION_ENUM, powers: List[POWERS_TYPE], is_arrested: bool):
        if type(villain_id) != int:
            raise EntityError("villain_id")
        self.villain_id = villain_id

        if type(name) != str:
            raise EntityError("name")
        self.name = name

        if type(description) != str:
            raise EntityError("description")
        self.description = description

        if type(genre) != GENRE_ENUM:
            raise EntityError("genre")
        self.genre = genre

        if type(region) != REGION_ENUM:
            raise EntityError("region")
        self.region = region

        if type(powers) != List[POWERS_TYPE]:
            raise EntityError("powers")
        self.powers = powers

        if type(is_arrested) != bool:
            raise EntityError("is_arrested")
        self.is_arrested = is_arrested