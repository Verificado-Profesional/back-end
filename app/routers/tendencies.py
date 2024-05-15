from datetime import datetime
from fastapi import APIRouter, Request
from app.controllers.tendencies_controller import TendenciesController
from app.models.tendencies import Tendencies

router = APIRouter()

@router.get(
    "/tendencies/",
    tags=["tendencies"],
    response_description="Get tendencies from specific date and source",
    response_model=Tendencies,
)
async def list_tendencies(request: Request, date: str = datetime.now().strftime("%d-%m-%y"), source: str = 'twitter'):
    return TendenciesController.get(request, date, source)
