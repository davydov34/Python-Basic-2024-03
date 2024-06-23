from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/ping/", status_code=200, tags=["ping"])
def func_ping():
    data = {"message": "pong"}
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)