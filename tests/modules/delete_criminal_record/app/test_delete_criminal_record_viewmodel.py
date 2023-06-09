from src.modules.delete_criminal_record.app.delete_criminal_record_viewmodel import DeleteCriminalRecordViewmodel
from src.modules.get_criminal_record.app.get_criminal_record_viewmodel import GetCriminalRecordViewmodel
from src.shared.domain.entities.crime import Crime
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.entities.villain import Villain
from src.shared.domain.enums.crime_type_enum import CRIME_TYPE
from src.shared.domain.enums.genre_enum import GENRE_ENUM
from src.shared.domain.enums.powers_type_enum import POWERS_TYPE
from src.shared.domain.enums.region_enum import REGION_ENUM

class Test_DeleteCriminalRecordViewmodel:
    def test_delete_criminal_record_viewmodel(self):

        villain = Villain(villain_id=1, name="Pinguim", description="Um anão muito GANG GANG BRO", genre=GENRE_ENUM.MALE, region=REGION_ENUM.NORTH, powers=[POWERS_TYPE.GANGSTER], is_arrested=True)
        record = CriminalRecord(criminal_record_id=0, villain=villain, crimes=[Crime(crime_type=CRIME_TYPE.CARRYING_RIDDLES, region=REGION_ENUM.NORTH)])

        recordViewmodel = DeleteCriminalRecordViewmodel(criminal_record=record).to_dict()
        expected = {
            'criminal_record_id': record.criminal_record_id,
            'villain': {
                'villain_id': record.villain.villain_id,
                'name': record.villain.name,
                'description': record.villain.description,
                'genre': record.villain.genre.value,
                'region': record.villain.region.value,
                'powers': [power.value for power in record.villain.powers],
                'is_arrested': record.villain.is_arrested
            },
            'crimes': [
                {
                    'crime_type': record.crimes[0].crime_type.value,
                    'region': record.crimes[0].region.value
                }
            ],
            'message': "the criminal_record was deleted successfully"
        }
       
        assert expected == recordViewmodel