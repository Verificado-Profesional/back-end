import uuid
from pydantic import BaseModel, Field

class CheckedNews(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    url: str = Field(...)
    category: str = Field(...)
    source: str = Field(...)
    date: str = Field(...)
    embeddings: list = Field(...)

    @staticmethod
    def get_schema():
        return {"id": str, "title": str, "url": str, "category": str, "source": str, "date": str}


