import uuid
from typing import Optional
from pydantic import BaseModel, Field


class News(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    content: str = Field(...)
    classification: str = Field(...)

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {"id": str, "title": str, "content": str, "classification": str}


class NewsUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    classification: Optional[str]
