from fastapi import FastAPI
import uvicorn
from .routers import dashboard, veracity, sentiment
import os

app = FastAPI()
app.include_router(dashboard.router)
app.include_router(veracity.router)
app.include_router(sentiment.router)


def start():
    host, port = getConfig()
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host=host, port=port, reload=True)


def getConfig():
    return os.getenv("HOST"), os.getenv("PORT")


@app.get("/")
def root():
    return {"message": "Hola, Verificados!"}
