from fastapi import Body, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.models.news import News
from app.repositories.news_repository import NewsRepository
from app.config.config import get_settings


settings = get_settings()
# Repository
news_repository = NewsRepository(settings.db_name, settings.client)


class NewsController:
    @staticmethod
    def post(input_news: News = Body(...)):
        news = jsonable_encoder(input_news)
        return news_repository.insert(news)

    @staticmethod
    def list_news():
        return list(news_repository.get())

    @staticmethod
    def get(id_received: str):
        if (news := news_repository.get(id_received)) is not None:
            return news
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"News with ID {id} not found"
        )

    @staticmethod
    def delete(id: str, response: Response):
        if news_repository.delete(id):
            response.status_code = status.HTTP_204_NO_CONTENT
            return response
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"News with ID {id} not found"
        )
