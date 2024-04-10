from cpunk_mongo.db import DataBase
from app.models.news import News
from pymongo import MongoClient

COLLECTION_NAME = "news"


class NewsRepository(DataBase):
    def __init__(self, db_name, url):
        if db_name == "test":
            import mongomock  # type: ignore

            self.db = mongomock.MongoClient().db
        else:
            self.client = MongoClient(url)
            self.db = self.client.mongodb_client[db_name]
            self.collection = self.db[COLLECTION_NAME]

    def get(self, id=None):
        if id is None:
            return self.collection.find(limit=100)
        return self.collection.find_one({"_id": id})

    def insert(self, news: News):
        return self.collection.insert_one(news)

    def delete(self, id: str):
        delete_result = self.collection.delete_one({"_id": id})
        return delete_result.deleted_count == 1
