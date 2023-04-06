from src.modules.get_criminal_record.app.get_criminal_record_controller import GetCriminalRecordController
from src.modules.get_criminal_record.app.get_criminal_record_usecase import GetCriminalRecordUsecase
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordController:
    def test_get_criminal_record_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repository=repo)
        controller = GetCriminalRecordController(usecase=usecase)

        request = HttpRequest(query_params={
            'criminal_record_id': repo.criminal_records_list[0].criminal_record_id
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['criminal_record_id'] == repo.criminal_records_list[0].criminal_record_id

    def test_get_criminal_record_controller_missing_parameters(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repository=repo)
        controller = GetCriminalRecordController(usecase=usecase)

        request = HttpRequest(query_params={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field criminal_record_id is missing'
    
    def test_get_criminal_record_controller_wrog_type_parameter(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repository=repo)
        controller = GetCriminalRecordController(usecase=usecase)

        request = HttpRequest(query_params={
            'criminal_record_id': '1'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id isn't in the right type.\n Received: str.\n Expected: int"

    def test_get_criminal_record_controller_no_items_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = GetCriminalRecordUsecase(repository=repo)
        controller = GetCriminalRecordController(usecase=usecase)

        request = HttpRequest(query_params={
            'criminal_record_id': 99999
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == 'No items found for criminal_record_id'