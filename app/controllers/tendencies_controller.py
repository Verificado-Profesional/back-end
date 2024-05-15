from fastapi import Request, HTTPException, status
from app.config.config import get_settings
from app.repositories.tendencies_repository import TendenciesRepository

settings = get_settings()
# Repository
tendencies_repository = TendenciesRepository(settings.db_name, settings.client)


class TendenciesController:

    @staticmethod
    def get(request: Request, date: str, source: str):
        if (tendencies := tendencies_repository.get_from(date, source)):
            return tendencies
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Date {date} or source {source} not valid"
        )
