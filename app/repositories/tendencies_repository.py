from datetime import datetime

from cpunk_mongo.db import DataBase
from pymongo import MongoClient

import app.config.constants as constants


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, constants.DATE_FORMAT)
        return True
    except ValueError:
        return False


def is_valid_source(source):
    return source == constants.TWITTER or source == constants.GOOGLE


class TendenciesRepository(DataBase):
    def __init__(self, db_name, url):
        if db_name == "test":
            import mongomock  # type: ignore

            self.db = mongomock.MongoClient().db
        else:
            self.client = MongoClient(url)
            self.db = self.client.mongodb_client[db_name]
            self.twitter_collection = self.db[constants.TWITTER]
            self.google_collection = self.db[constants.GOOGLE]

    def get_from(self, date, source, region = 'argentina'):
        if not is_valid_date(date) or not is_valid_source(source):
            return None
        
        if source == constants.TWITTER:
            query = {"date": date, "region": region.lower()}
            result = self.twitter_collection.find(query)
        elif source == constants.GOOGLE:
            query = {"date": date}
            result = self.google_collection.find(query)
        else:
            return None

        return list(result)
