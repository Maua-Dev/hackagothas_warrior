import json
from src.modules.delete_criminal_record.app.delete_criminal_record_presenter import delete_criminal_record_presenter


class Test_DeleteCriminalRecordPresenter:
    def test_delete_criminal_record_presenter(self):
        event = {
            "body": {
                "criminal_record_id": 1
            }
        }

        response = delete_criminal_record_presenter(event, None)

        expected = {
            "criminal_record_id": 1,
            "villain": {
                "villain_id": 1,
                "name": "Pinguim",
                "description": "Um anão muito GANG GANG BRO",
                "genre": "MALE",
                "region": "NORTH",
                "powers": [
                    "GANGSTER"
                ],
                "is_arrested": True
            },
            "crimes": [
                {
                    "crime_type": "CATCHED_A_ROBIN",
                    "region": "NORTH"
                },
            ],
            'message': 'the criminal_record was deleted successfully'
        }

        assert response['status_code'] == 200
        assert json.loads(response['body']) == expected