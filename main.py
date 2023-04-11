from fastapi import FastAPI
from src.modules.get_criminal_record.app.get_criminal_record_presenter import get_criminal_record_presenter


app = FastAPI()


@app.get("/get_criminal_record/")
def get_criminal_record_presenter(data: dict = None):
    request = {
        "body": {
            "criminal_record_id": int(data["criminal_record_id"])
        },
        "headers": {},
        "query_params": {},
    }
    
    response = get_criminal_record_presenter(request, None)
    return response