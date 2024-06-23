from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/ping/", status_code=200, response_class=JSONResponse, tags=["ping"])
def func_ping():
    return { "message": "pong" }