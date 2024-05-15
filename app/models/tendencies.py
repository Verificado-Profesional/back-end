import uuid
from pydantic import BaseModel, Field

class Tendencies(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    content: str = Field(...)
    classification: str = Field(...)

    @staticmethod
    def get_schema():
        return {"id": str, "content": str, "classification": str}


