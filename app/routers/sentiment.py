from fastapi import APIRouter

from app.controllers.models_controller import ModelController
from app.models.text import Text

router = APIRouter()

SENTIMENT_MODEL = "VerificadoProfesional/SaBERT-Spanish-Sentiment-Analysis"


@router.post("/sentiment/", tags=["sentiment"])
async def post_sentiment(text: Text):
    return ModelController.post(text, SENTIMENT_MODEL)
