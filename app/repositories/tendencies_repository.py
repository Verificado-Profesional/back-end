from cpunk_mongo.db import DataBase
from pymongo import MongoClient
from datetime import datetime

DATE_FORMAT='%d-%m-%y'
TWITTER="twitter"
GOOGLE="google"

def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, DATE_FORMAT)
            return True
        except ValueError:
            return False
        
def is_valid_source(source):
    return source == TWITTER or source == GOOGLE

class TendenciesRepository(DataBase):
    def __init__(self, db_name, url):
        if db_name == "test":
            import mongomock  # type: ignore

            self.db = mongomock.MongoClient().db
        else:
            self.client = MongoClient(url)
            self.db = self.client.mongodb_client[db_name]
            self.twitter_collection = self.db[TWITTER]
            self.google_collection = self.db[GOOGLE]

    def get_from(self, date, source):
        if not is_valid_date(date) or not is_valid_source(source):
            return None
        
        query = {"date": datetime.strptime(date, DATE_FORMAT)}
        
        if source == TWITTER:
            result = self.twitter_collection.find(query)
        elif source == GOOGLE:
            result = self.google_collection.find(query)
        else:
            return None
        
        return list(result)