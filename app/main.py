from fastapi import FastAPI
import uvicorn
from .routers import dashboard, veracity, sentiment
from decouple import config, AutoConfig
from pymongo import MongoClient

app = FastAPI()
app.include_router(dashboard.router)
app.include_router(veracity.router)
app.include_router(sentiment.router)


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


def start():
    host, port, uri, db_name = getConfig()
    print(host, port, uri)
    app.mongodb_client = MongoClient(uri)
    app.database = app.mongodb_client[db_name]
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host=host, port=port, reload=True)


@app.on_event("startup")
def getConfig():
    host = config("HOST")
    port = config("PORT")
    client = config("ATLAS_URI")
    db_name = config("DB_NAME")

    print(host, port, client)
    return host, int(port), client, db_name


@app.get("/")
def root():
    return {"message": "Hola, Verificados!"}
