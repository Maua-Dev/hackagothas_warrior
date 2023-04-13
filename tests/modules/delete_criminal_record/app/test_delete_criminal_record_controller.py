from src.modules.delete_criminal_record.app.delete_criminal_record_controller import DeleteCriminalRecordController
from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_DeleteCriminalRecordController:
    def test_delete_criminal_record_controller(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repository=repo)
        controller = DeleteCriminalRecordController(usecase=usecase)

        request = HttpRequest(body={
            'criminal_record_id': repo.criminal_records_list[0].criminal_record_id
        })

        response = controller(request=request)
        assert response.status_code == 200
        assert response.body['message'] == 'the criminal_record was deleted successfully'

    def test_delete_criminal_record_controller_missing_parameters(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repository=repo)
        controller = DeleteCriminalRecordController(usecase=usecase)

        request = HttpRequest(query_params={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field criminal_record_id is missing'
    
    def test_delete_criminal_record_controller_wrog_type_parameter(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repository=repo)
        controller = DeleteCriminalRecordController(usecase=usecase)

        request = HttpRequest(query_params={
            'criminal_record_id': '1'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field criminal_record_id isn't in the right type.\n Received: str.\n Expected: int"

    def test_delete_criminal_record_controller_no_items_found(self):
        repo = CriminalRecordRepositoryMock()
        usecase = DeleteCriminalRecordUsecase(repository=repo)
        controller = DeleteCriminalRecordController(usecase=usecase)

        request = HttpRequest(query_params={
            'criminal_record_id': 99999
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == 'No items found for criminal_record_id'