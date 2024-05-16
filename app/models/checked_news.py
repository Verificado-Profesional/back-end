import uuid
from pydantic import BaseModel, Field

class CheckedNews(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    content: str = Field(...)

    @staticmethod
    def get_schema():
        return {"id": str, "content": str}

    def get_similar(self): #TODO
        return[]

