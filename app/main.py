from fastapi import FastAPI
import uvicorn
from .routers import dashboard, veracity, sentiment
import os


app = FastAPI()
app.include_router(dashboard.router)
app.include_router(veracity.router)
app.include_router(sentiment.router)


# Load environment variables from .env file
# env_vars = dotenv_values(".env")


def start():
    host, port = getConfig()
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host=host, port=port, reload=True)


def getConfig():
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    return host, int(port)


@app.get("/")
def root():
    return {"message": "Hola, Verificados!"}
