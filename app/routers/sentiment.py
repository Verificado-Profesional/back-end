from fastapi import APIRouter

router = APIRouter()


@router.post("/sentiment/", tags=["sentiment"])
async def post_sentiment():
    return {
        "status": "success",
        "message": "La noticia ha sido clasificada exitosamente.",
        "data": {
            "title": "Titulo de la noticia",
            "content": "Contenido de la noticia",
            "classification": "Positive",
            "accuracy": 68,
        },
    }
