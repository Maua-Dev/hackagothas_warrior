from src.modules.get_criminal_record.app.get_criminal_record_controller import GetCriminalRecordController
from src.modules.get_criminal_record.app.get_criminal_record_usecase import GetCriminalRecordUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_user_repo()()
usecase = GetCriminalRecordUsecase(repo)
controller = GetCriminalRecordController(usecase)

def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()