import abc
from typing import List
from src.shared.domain.entities.crime import Crime

from src.shared.domain.entities.villain import Villain
from src.shared.helpers.errors.domain_errors import EntityError

class CriminalRecord(abc.ABC):
    criminal_record_id: int
    villain: Villain
    crimes: List[Crime]

    def __init__(self, criminal_record_id: int, villain: Villain, crimes: List[Crime]):
        if type(criminal_record_id) != int:
            raise EntityError("criminal_record_id")
        self.criminal_record_id = criminal_record_id

        if type(villain) != Villain:
            raise EntityError("villain")
        self.villain = villain

        if type(crimes) != List[Crime]:
            raise EntityError("crimes")
        self.crimes = crimes
