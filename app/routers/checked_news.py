from datetime import datetime
from fastapi import APIRouter, Request, Response
from app.controllers.similarity_controller import NewsSimilarityController
from app.controllers.tendencies_controller import TendenciesController
from app.models.checked_news import CheckedNews
from app.models.tendencies import Tendencies
import json


router = APIRouter()

@router.get( 
    "/similar_checked_news/",
    tags=["similar_checked_news"],
    response_description="Get similar news from text",
    response_model=CheckedNews,
)
async def list_similar_news(request: Request, response: Response):
    body_bytes = await request.body()
    body = json.loads(body_bytes)
    text = body.get("text")
    return NewsSimilarityController.get(request, text)
