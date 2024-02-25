from fastapi import APIRouter
from app.controllers.veracity import VeracityController


router = APIRouter()


@router.post("/veracity/", tags=["veracity"])
async def post_veracity():
    return VeracityController.post()
