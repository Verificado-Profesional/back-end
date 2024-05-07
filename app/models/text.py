from pydantic import BaseModel

class Text(BaseModel):
    text: str

    @staticmethod
    def get_schema():
        return {"text": str}