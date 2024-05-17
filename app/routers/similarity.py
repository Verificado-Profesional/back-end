from fastapi import APIRouter
from app.controllers.similarity import NewsSimilarityController
from app.models.text import Text

router = APIRouter()

@router.post( "/similarity/",tags=["similarity"],response_description="Get similar news from text")
async def list_similar_news(text: Text):
    return NewsSimilarityController.post(text)

