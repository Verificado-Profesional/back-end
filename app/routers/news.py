from typing import List

from fastapi import APIRouter, status, Request, Response

from app.controllers.news_controller import NewsController
from app.models.news import News

from bs4 import BeautifulSoup
from newspaper import Article
import json

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


@router.get("/news/", tags=["news"], response_description="List all news")
async def list_news():
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


@router.post(
    "/news/fetch-data", tags=["news"], response_description="Post an article by url"
)
async def fetch_data(request: Request):
    try:
        # Extraer el contenido del artículo
        body_bytes = await request.body()
        print(body_bytes)
        # Parse the JSON data
        body = json.loads(body_bytes)
        url = body.get("url")
        print(body)
        print(url)
        article_content = await fetch_article_content(url)

        if article_content:
            # Analizar el contenido HTML para obtener solo el texto
            soup = BeautifulSoup(article_content, "html.parser")
            text_content = soup.get_text()

            # Devolver el contenido del artículo
            return text_content
        else:
            return None

    except Exception as e:
        print("Error al obtener el contenido del artículo:", e)
        return None


async def fetch_article_content(url):
    try:
        # Crear un objeto Article
        article = Article(url)

        # Descargar y analizar el artículo
        article.download()
        article.parse()

        # Obtener el contenido del artículo
        content = article.text

        return content

    except Exception as e:
        print("Error al extraer el artículo:", e)
        return None