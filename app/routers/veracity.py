from fastapi import APIRouter

from app.config.constants import VERACITY_MODEL
from app.controllers.models_controller import ModelController
from app.models.text import Text

router = APIRouter()


@router.post("/veracity/", tags=["veracity"])
async def post_veracity(text: Text):
    return ModelController.post(text, VERACITY_MODEL)
