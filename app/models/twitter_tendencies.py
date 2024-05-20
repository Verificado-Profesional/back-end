import uuid
from bson import ObjectId
from pydantic import BaseModel, Field, json

json.ENCODERS_BY_TYPE[ObjectId] = str

class TwitterTendencies(BaseModel): #TODO
    date: str = Field(...)
    tweet: str = Field(...)
    url: str = Field(...)
    tweet_count: int = Field(...)
    region: str = Field(...)

    @staticmethod
    def get_schema():
        return {"date": str, "tweet": str, "url": str, "tweet_count": int, "region": str}
