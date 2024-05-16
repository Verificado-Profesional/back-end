from fastapi import Body, Request, HTTPException, status
from app.config.config import get_settings
from app.models.checked_news import CheckedNews

settings = get_settings()


class NewsSimilarityController:

    @staticmethod
    def get(request: Request, text: str = Body(...)):
        if (len(text) > 0):
            return CheckedNews.get_similar(text)
        
        return []
