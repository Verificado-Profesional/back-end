from decouple import config
from pydantic import BaseSettings


class Settings(BaseSettings):
    host = config("HOST")
    port = int(config("PORT"))
    client = config("ATLAS_URI")
    db_name = config("DB_NAME")


def get_settings():
    return Settings()
