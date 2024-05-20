from fastapi import Request, HTTPException, status
from app.config.config import get_settings
from app.config.constants import GOOGLE, TWITTER
from app.repositories.tendencies_repository import TendenciesRepository

settings = get_settings()
# Repository
tendencies_repository = TendenciesRepository(settings.db_name, settings.client)


class TendenciesController:

    @staticmethod
    def get_twitter_tendencies(request: Request, date: str, region: str): #TODO validar la region?
        print("aaaaaa")
        if (tendencies := tendencies_repository.get_from(date, TWITTER, region)) is not None:
            print("tendencies return:", tendencies)
            return tendencies
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Date {date} or source {TWITTER} not valid"
        )
    
    @staticmethod
    def get_google_tendencies(request: Request, date: str):
        if (tendencies := tendencies_repository.get_from(date, GOOGLE)) is not None:
            return tendencies
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Date {date} or source {GOOGLE} not valid"
        )
