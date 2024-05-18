from fastapi import APIRouter

from app.controllers.models_controller import ModelController
from app.models.text import Text

router = APIRouter()

VERACITY_MODEL = "VerificadoProfesional/SaBERT-Spanish-Fake-News"


@router.post("/veracity/", tags=["veracity"])
async def post_veracity(text: Text):
    return ModelController.post(text, VERACITY_MODEL)
