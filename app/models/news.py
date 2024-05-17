from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field, json


json.ENCODERS_BY_TYPE[ObjectId] = str


class News(BaseModel):
    id_news: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    content: str = Field(...)
    classification: str = Field(...)
    view_count: int = Field(default=1)


class NewsUpdate(BaseModel):
    content: Optional[str]
    classification: Optional[str]
    view_count: Optional[int]
