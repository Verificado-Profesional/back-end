from typing import List

from fastapi import APIRouter, HTTPException, status, Request, Response

from app.controllers.news_controller import NewsController
from app.models.news import News


router = APIRouter()


@router.post(
    "/news/",
    tags=["news"],
    response_description="Save a news",
    status_code=status.HTTP_201_CREATED,
    response_model=News,
)
async def post_news(request: Request, news: News):
    return NewsController.post(request, news)


@router.get(
    "/news/",
    tags=["news"],
    response_description="List all news",
    response_model=List[News],
)
async def list_news():
    print("llega hasta aca \n")
    return NewsController.list_news()


@router.get(
    "/news/{id}",
    tags=["news"],
    response_description="Get a single news by id",
    response_model=News,
)
async def read_news(request: Request, id: str):
    return NewsController.get(request, id)


@router.delete(
    "/news/{id}",
    tags=["news"],
    response_description="Delete a single news by id",
    response_model=News,
)
async def delete_news(request: Request, id: str, response: Response):
    return NewsController.delete(request, id, response)
