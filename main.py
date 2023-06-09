import json
from src.modules.delete_criminal_record.app.delete_criminal_record_presenter import delete_criminal_record_presenter
from src.modules.get_criminal_record.app.get_criminal_record_presenter import get_criminal_record_presenter
from fastapi import FastAPI


app = FastAPI()


@app.get("/get_criminal_record/")
def get_criminal_record(id_order:str = None):
    request = json.dumps({
        "body": {},
        "headers": {},
        "query_params": {
            "criminal_record_id": int(id_order)
        }
    })
    
    response = get_criminal_record_presenter(request, None)
    return response

@app.post("/delete_criminal_record/")
def delete_criminal_record(data: dict = None):
    request = {
        "body": {
            "criminal_record_id": int(data["criminal_record_id"])
        },
        "headers": {},
        "query_params": {},
    }
    
    response = delete_criminal_record_presenter(request, None)
    return response