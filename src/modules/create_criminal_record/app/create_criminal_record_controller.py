from src.modules.create_criminal_record.app.create_criminal_record_usecase import CreateCriminalRecordUsecase
from src.modules.create_criminal_record.app.create_criminal_record_viewmodel import CreateCriminalRecordViewmodel
from src.shared.domain.entities.criminal_record import CriminalRecord
from src.shared.domain.entities.villain import Villain
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError, NotFound

class CreateCriminalRecordController:
    def __init__(self, usecase: CreateCriminalRecordUsecase):
        self.CreateCriminalRecordUsecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('criminal_record_id') is None:
                raise MissingParameters("criminal_record_id")
            if request.data.get('villain_id') is None:
                raise MissingParameters("villain_id")
            if request.data.get('name') is None:
                raise MissingParameters("name")
            if request.data.get('description') is None:
                raise MissingParameters("description")
            if request.data.get('genre') is None:
                raise MissingParameters("genre")
            if request.data.get('region') is None:
                raise MissingParameters("region")
            if request.data.get('powers') is None:
                raise MissingParameters("powers")
            if request.data.get('is_arrested') is None:
                raise MissingParameters("is_arrested")
            if request.data.get('crimes') is None:
                raise MissingParameters("crimes")
            
            record = CriminalRecord(
                criminal_record_id=request.data.get('criminal_record_id'),
                villain=Villain(
                    villain_id=request.data.get('villain_id'),
                    name=request.data.get('name'),
                    description=request.data.get('description'),
                    genre=request.data.get('genre'),
                    region=request.data.get('region'),
                    powers=request.data.get('powers'),
                    is_arrested=request.data.get('is_arrested')
                ),
                crimes=request.data.get('crimes')
            )
            recordUseCase = self.CreateCriminalRecordUsecase(
                criminal_record=record
            )
            viewmodel = CreateCriminalRecordViewmodel(recordUseCase)

            return Created(viewmodel.to_dict())
        
        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])

    