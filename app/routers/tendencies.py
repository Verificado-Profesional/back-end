from datetime import datetime
from typing import List
from fastapi import APIRouter, Request
from app.controllers.tendencies_controller import TendenciesController
from app.models.google_tendencies import GoogleTendencies
from app.models.twitter_tendencies import TwitterTendencies

router = APIRouter()

@router.get( #TODO raise exception here
    "/trends/twitter/",
    tags=["twitter_tendencies"],
    response_description="Get twitter's tendencies from specific date ",
    response_model=List[TwitterTendencies],
)
async def list_tendencies(request: Request, date: str = datetime.now().strftime("%d-%m-%Y"), region: str = 'argentina'):
    return TendenciesController.get_twitter_tendencies(request, date, region)

@router.get( #TODO raise exception here
    "/trends/google/",
    tags=["google_tendencies"],
    response_description="Get google's tendencies from specific date and source",
    response_model=List[GoogleTendencies],
)
async def list_tendencies(request: Request, date: str = datetime.now().strftime("%d-%m-%Y")):
    return TendenciesController.get_google_tendencies(request, date)

