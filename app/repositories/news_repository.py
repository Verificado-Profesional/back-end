from bson import ObjectId
from cpunk_mongo.db import DataBase
from app.models.news import News
from pymongo import MongoClient, ReturnDocument

COLLECTION_NAME = "news"
from pydantic import json


json.ENCODERS_BY_TYPE[ObjectId] = str


class NewsRepository(DataBase):
    def __init__(self, db_name, url):
        if db_name == "test":
            import mongomock  # type: ignore

            self.db = mongomock.MongoClient().db
        else:
            self.client = MongoClient(url)
            self.db = self.client.mongodb_client[db_name]
            self.collection = self.db[COLLECTION_NAME]

    def get(self, id_received=None):
        if id_received is None:
            return list(self.collection.find(limit=100))
        return self.collection.find_one({"_id": id_received})

    def delete_many(self):
        self.collection.delete_many({})

    def insert(self, news: News):
        result = self.collection.find_one_and_update(
            {"content": news["content"]},
            {
                "$inc": {"view_count": 1},
                "$setOnInsert": {
                    "_id": news["_id"],
                    "classification": news["classification"],
                },
            },
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )
        result["_id"] = str(result["_id"])
        return result

    def delete(self, id: str):
        delete_result = self.collection.delete_one({"_id": id})
        return delete_result.deleted_count == 1
