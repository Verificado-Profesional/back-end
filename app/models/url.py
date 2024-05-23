from pydantic import BaseModel

class Url(BaseModel):
    url: str

    @staticmethod
    def get_schema():
        return {"url": str}