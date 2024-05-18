import json
from typing import List
from urllib import response

from bs4 import BeautifulSoup
from fastapi import APIRouter, HTTPException, Request, Response, status
from newspaper import Article

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
async def post_news(news: News, response: Response):
    news = NewsController.post(news)
    response.status_code = status.HTTP_201_CREATED
    return news


@router.get(
    "/news/",
    tags=["news"],
    response_description="List all news",
    response_model=List[News],
)
async def list_news():
    return NewsController.list_news()


@router.get("/news/{id}", tags=["news"], response_description="Get a single news by id")
async def read_news(id: str):
    return NewsController.get(id)


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
async def fetch_data(request: Request, response: Response):
    body = await obtain_body(request)
    url = body.get("url")

    article_content = await fetch_article_content(url)

    if article_content:
        # Analizar el contenido HTML para obtener solo el texto
        soup = BeautifulSoup(article_content, "html.parser")
        text_content = soup.get_text()

        # Devolver el contenido del artículo
        return text_content
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error obtaining article content",
        )


async def obtain_body(request: Request):
    try:
        # Extraer el contenido del artículo
        body_bytes = await request.body()
        body_bytes_decoded = body_bytes.decode("utf-8")
        # Parse the JSON data
        return json.loads(body_bytes_decoded)
    except Exception as e:
        print("Error al obtener el contenido del artículo:", e)
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )


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
