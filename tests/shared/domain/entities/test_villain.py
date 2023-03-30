from typing import List
import pytest
from src.shared.domain.entities.villain import Villain
from src.shared.domain.enums.genre_enum import GENRE_ENUM
from src.shared.domain.enums.powers_type_enum import POWERS_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Villain():
    def test_villain(self):
        villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)

        assert villain.villain_id == 1
        assert villain.name == "Pinguim"
        assert villain.description == "Um anão muito GANG GANG BRO"
        assert villain.genre == GENRE_ENUM.MALE
        assert villain.region == REGION_ENUM.NORTH
        assert villain.powers == [POWERS_TYPE.GANGSTER]
        assert villain.is_arrested == False

    def test_villain_invalid_villain_id(self):
        with pytest.raises(EntityError):
            villain = Villain(villain_id="1", name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)
    
    def test_villain_invalid_villain_name(self):
        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name=1, description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)


    def test_villain_invalid_villain_description(self):
        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name='', description=1, genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)

    
    def test_villain_invalid_villain_genre(self):
        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=1, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)
    
    def test_villain_invalid_villain_region(self):
        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=1, powers=[POWERS_TYPE.GANGSTER], is_arrested=False)

    def test_villain_invalid_villain_powers(self):
        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=1, is_arrested=False)


    def test_villain_invalid_villain_is_arrested(self):
        with pytest.raises(EntityError):
            villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=1)

