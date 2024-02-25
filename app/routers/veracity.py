from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post("/veracity/", tags=["veracity"])
async def post_veracity():
    return {
        "status": "success",
        "message": "La noticia ha sido clasificada exitosamente.",
        "data": {
            "title": "Titulo de la noticia",
            "content": "Contenido de la noticia",
            "classification": True,
            "accuracy": 68,
        },
    }
