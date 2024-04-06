from fastapi import Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.models.news import News
from app.repositories.news_repository import NewsRepository
from app.config.config import get_settings


settings = get_settings()
# Repository
news_repository = NewsRepository(settings.db_name, settings.client)


class NewsController:
    @staticmethod
    def post(request: Request, news: News = Body(...)):
        news = jsonable_encoder(news)
        new_news = news_repository.insert(news)
        created_news = news_repository.get(new_news.inserted_id)
        return created_news

    @staticmethod
    def list_news():
        news = list(news_repository.get())
        return news

    @staticmethod
    def get(request: Request, id: str):
        if (news := news_repository.get(id)) is not None:
            return news
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"News with ID {id} not found"
        )

    @staticmethod
    def delete(request: Request, id: str, response: Response):
        if news_repository.delete(id):
            response.status_code = status.HTTP_204_NO_CONTENT
            return response
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"News with ID {id} not found"
        )
