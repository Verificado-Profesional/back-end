from fastapi import FastAPI
import uvicorn
from .routers import dashboard, veracity, sentiment, news
from app.config.config import get_settings
from app.repositories.news_repository import NewsRepository

app = FastAPI()
app.include_router(dashboard.router)
app.include_router(veracity.router)
app.include_router(sentiment.router)
app.include_router(news.router)


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


def start():
    settings = get_settings()
    news_repository = NewsRepository(settings.db_name, settings.client)
    print("connected database!", news_repository.db)
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host=settings.host, port=settings.port, reload=True)


# @app.on_event("startup")
# def getConfig():
#     host = config("HOST")
#     port = config("PORT")
#     client = config("ATLAS_URI")
#     db_name = config("DB_NAME")

#     print(host, port, client)
#     return host, int(port), client, db_name


@app.get("/")
def root():
    return {"message": "Hola, Verificados!"}
