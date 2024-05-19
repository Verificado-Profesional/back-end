from fastapi import APIRouter

from app.config.constants import SENTIMENT_MODEL
from app.controllers.models_controller import ModelController
from app.models.text import Text

router = APIRouter()


@router.post("/sentiment/", tags=["sentiment"])
async def post_sentiment(text: Text):
    return ModelController.post(text, SENTIMENT_MODEL)
