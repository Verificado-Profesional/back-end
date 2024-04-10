from fastapi import FastAPI
import uvicorn
from .routers import dashboard, veracity, sentiment, news
from app.config.config import get_settings
from app.repositories.news_repository import NewsRepository
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]
app = FastAPI()
app.include_router(dashboard.router)
app.include_router(veracity.router)
app.include_router(sentiment.router)
app.include_router(news.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


def start():
    settings = get_settings()
    news_repository = NewsRepository(settings.db_name, settings.client)
    print("connected database!")
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host=settings.host, port=settings.port, reload=True)


@app.get("/")
def root():
    return {"message": "Hola, Verificados!"}
